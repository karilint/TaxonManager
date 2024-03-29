import csv
import urllib.parse
import requests
from bibtexparser.bparser import BibTexParser
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from front.filters import AuthorFilter, ExpertFilter, RefFilter, TaxonFilter
from front.forms import (AuthorForm, BibtexForm, DoiForm, ExpertForm,
                         JuniorSynonymForm, RefForm, TaxonForm)
from front.models import (Expert, GeographicDiv, Hierarchy, Kingdom, Reference,
                          SynonymLink, TaxonAuthorLkp, TaxonomicUnit,
                          TaxonUnitType)


def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference


def login(request):
    return render(request, 'front/login.html')

def error(request, message):
    return render(request, 'front/error.html', {'message' : message})


def load_rankOfTaxonToBeAdded(request):
    kingdomId = request.GET.get('id')
    kingdomName = Kingdom.objects.get(id=kingdomId)

    rankOfTaxonToBeAdded = TaxonUnitType.objects.exclude(
        rank_name='Kingdom').filter(kingdom=kingdomName)

    return render(request, 'front/rankOfTaxonToBeAdded.html', {'rankOfTaxonToBeAdded': rankOfTaxonToBeAdded})


def load_parentTaxon(request):
    taxonnomicTypeName = request.GET.get('id')
    kingdomId = request.GET.get('kingdomId')
    kingdom = Kingdom.objects.get(pk=kingdomId)

    taxontype = TaxonUnitType.objects.get(
        rank_name=taxonnomicTypeName, kingdom=kingdom)

    all_prev_taxons = TaxonUnitType.objects.filter(rank_id__range=(
        taxontype.req_parent_rank_id, taxontype.dir_parent_rank_id), kingdom=taxontype.kingdom)
    all_prev_taxons_rank = [taxon for taxon in all_prev_taxons]

    parentTaxon = TaxonomicUnit.objects.filter(rank__in=all_prev_taxons_rank)

    return render(request, 'front/parentTaxon.html', {'parentTaxon': parentTaxon})

def load_seniorSynonym(request):
    seniorSynonym = TaxonomicUnit.objects.exclude(name_usage__in=['invalid', 'not accepted'])

    return render(request, 'front/seniorSynonym.html', {'seniorSynonym': seniorSynonym})

def load_juniorSynonym(request):
    juniorSynonym = TaxonomicUnit.objects.exclude(name_usage__in=['invalid', 'not accepted'])

    return render(request, 'front/juniorSynonym.html', {'juniorSynonym': juniorSynonym})

def taxon_add(request, pk = None):
    c = {'pk': pk if pk else ''}
    form = TaxonForm()
    taxon = None
    parent = None

    if request.method == 'POST':
        if pk:
            # Editing an existing taxon
            taxon = TaxonomicUnit.objects.get(pk=pk)
            old_rank = taxon.rank
            # Clear old manyTomany relations
            taxon.expert.clear()
            taxon.geographic_div.clear()
            
        # create a form instance and populate it with data from the request:
        form = TaxonForm(request.POST, instance = taxon)
        # check whether it's valid:
        if form.is_valid():
            try:
                # save names from Modelform, but don't admit new unit to db yet
                new_unit = form.save(commit=False)
                kingdom = Kingdom.objects.get(
                    kingdom_name=form.cleaned_data['kingdom_name'])
                rank_of_new_taxon = TaxonUnitType.objects.get(
                    rank_name=form.cleaned_data['taxonnomic_types'], kingdom=kingdom)

                parent = TaxonomicUnit.objects.get(
                    unit_name1=form.cleaned_data['rank_name'],
                    kingdom=kingdom
                )
                # fill complete_name field
                if rank_of_new_taxon.rank_name.lower() == 'species' and kingdom.kingdom_name.lower() == 'animalia':
                    new_unit.complete_name = new_unit.unit_name1 # TODO genus + species
                elif rank_of_new_taxon.rank_name.lower() == 'subspecies' and kingdom.kingdom_name.lower() == 'animalia':
                    new_unit.complete_name = new_unit.unit_name1 # TODO genus + species + subspecies
                else:
                    new_unit.complete_name = new_unit.unit_name1
                # set new unit's parent
                new_unit.parent_id = parent.taxon_id
                # and kingdom based on parent
                new_unit.kingdom = parent.kingdom

                new_unit.rank = rank_of_new_taxon
                #Synonym stuff:
                if form.cleaned_data["is_junior_synonym"] and form.cleaned_data["senior_synonym"] != "":
                    if kingdom.kingdom_name in ["Chromista", "Fungi", "Plantae"]:
                        new_unit.name_usage = "not accepted"
                        new_unit.unaccept_reason= "synonym"
                    else:
                        new_unit.name_usage = "invalid"
                        new_unit.unaccept_reason= "junior synonym"
                else:
                    if kingdom.kingdom_name in ["Chromista", "Fungi", "Plantae"]:
                        new_unit.name_usage = "accepted"
                    else:
                        new_unit.name_usage = "valid"

                author = form.cleaned_data['taxon_author_id']
                if author:
                    new_unit.taxon_author_id=author.taxon_author_id
                reference = form.cleaned_data['reference']

                new_unit.reference = reference
                new_unit.save()

                #add SynonymLink
                if form.cleaned_data["is_junior_synonym"] and form.cleaned_data["senior_synonym"] != "":
                    SynonymLink.objects.create(synonym_id = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data["unit_name1"]).taxon_id, taxon_id_accepted=TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data["senior_synonym"])).save()
                    new_unit.save()
                
                # refs = form.cleaned_data['references']
                # for ref in refs:
                #     new_unit.references.add(ref)
                geos = form.cleaned_data['geographic_div']
                for geo in geos:
                    new_unit.geographic_div.add(geo)
                experts = form.cleaned_data['expert']
                for expert in experts:
                    new_unit.expert.add(expert)
               
                if pk:
                    #check if hierarchy needs to be updated
                    if Hierarchy.objects.get(taxon=taxon).parent_id != taxon.parent_id or taxon.rank != old_rank:
                        move_taxon_update_hierarchystring(taxon)
                else:
                    create_hierarchystring(new_unit)                                    
            except TaxonomicUnit.DoesNotExist:
                # form was filled incorrectly
                print("saving new unit did not workout; do something")
            if pk is not None:
                return HttpResponseRedirect('/hierarchy/{}'.format(pk)) 
            else:
                return HttpResponseRedirect('/taxa')

    # if a GET (or any other method) we'll create a blank form
    else:
        # edit existing taxon
        try:
            c['title'] = 'Edit'
            taxon = TaxonomicUnit.objects.get(pk=pk)
            parent =TaxonomicUnit.objects.get(pk=taxon.parent_id)

            form = TaxonForm(initial={
            'kingdom_name': taxon.kingdom,
            #rank name and parent name's are initialized by add-taxon.html
            'unit_name1': taxon.unit_name1,
            'unit_name2': taxon.unit_name2,
            'unit_name3': taxon.unit_name3,
            'unit_name4': taxon.unit_name4,
            'geographic_div': taxon.geographic_div.values_list('id', flat=True),
            'expert': taxon.expert.values_list('id', flat=True),
            'taxon_author_id': taxon.taxon_author
             })

        except TaxonomicUnit.DoesNotExist:
            c['title'] = 'Add'
            form = TaxonForm()
    
    c['form'] = form
    c['taxon'] = taxon
    c['parent'] = parent
    return render(request, 'front/add-taxon.html', c)


def move_taxon_update_hierarchystring(taxon):
    currentHierarchy = Hierarchy.objects.get(taxon = taxon)
    # get the old Hierarchy object's parent's id
    idToBeChanged = currentHierarchy.parent_id 
    # get the old parent for comparison
    oldParent = TaxonomicUnit.objects.get(pk = idToBeChanged)
    # update Hierarchy object's parent's id;
    currentHierarchy.parent_id = taxon.parent_id 
    # establish current depth
    idsInHierarchystring = currentHierarchy.hierarchy_string.split('-')
    depth = len(idsInHierarchystring)
    
    # fetch all the objects that contain the old id in hierarchystring
    hierarchies= Hierarchy.objects.filter(hierarchy_string__contains='-'+str(idToBeChanged)+'-')

    # new parent for comparison below
    parent = TaxonomicUnit.objects.get(pk = taxon.parent_id)

    # levels increase
    if oldParent.rank.rank_id < parent.rank.rank_id:
            hierarchies = Hierarchy.objects.filter(hierarchy_string__contains=taxon.pk)
            parentHierarchyString = Hierarchy.objects.get(taxon = parent)
            parentString = parentHierarchyString.hierarchy_string
            
            for hierarchy in hierarchies:
                parentIds = parentString.split('-')
                currentString= hierarchy.hierarchy_string
                currentArray = currentString.split('-')
                currentLength = len(currentArray)
 
                # manipulate string so that there will be no duplicates
                for id in currentArray:
                    if id not in parentIds:
                        parentIds.append(id)

                newString = '-'.join(parentIds)
                hierarchy.hierarchy_string=newString
                
                if depth == currentLength:
                    #update hierarchy object's parent
                    hierarchy.parent_id = taxon.parent_id    
                hierarchy.save()              
            
    # levels decrease
    elif oldParent.rank.rank_id > parent.rank.rank_id:      
        # old parent info
        oldParentHierarchy = Hierarchy.objects.get(taxon=oldParent)
        oldparentString = oldParentHierarchy.hierarchy_string
        oldParentIds = oldparentString.split('-')

        # new parent info
        parentHierarchy = Hierarchy.objects.get(taxon = parent) 
        parentString = parentHierarchy.hierarchy_string
        parentIds=parentString.split('-')
        for hierarchy in hierarchies:
            delete = []
            parentIds = parentString.split('-')
            currentString= hierarchy.hierarchy_string
            currentArray = currentString.split('-')
            currentLength = len(currentArray)                
             
            # handle current taxon's children
            if currentLength >= depth:
                #determine ids to remove
                for id in currentArray: 
                    if id in oldParentIds: 
                        delete.append(id)

                # remove ids
                for id in delete:
                    if id in currentArray:
                        currentArray.remove(id)

                # determine final ids 
                for id in currentArray:
                    parentIds.append(id)

                newString = '-'.join(parentIds)
                hierarchy.hierarchy_string=newString

                if currentLength == depth:
                    #update hierarchy object's parent
                    hierarchy.parent_id = taxon.parent_id    

                hierarchy.save()

    # child moves on the same level
    elif oldParent.rank.rank_id == parent.rank.rank_id:
        for hierarchy in hierarchies:
            
            currentString= hierarchy.hierarchy_string
            currentArray = currentString.split('-')
            currentLength = len(currentArray)
            
            # handle child
            if currentLength == depth:
                newString= currentString.replace(str(idToBeChanged), str(currentHierarchy.parent_id), 1)
                hierarchy.hierarchy_string=newString
                # update hierarchy's parent also
                hierarchy.parent_id = taxon.parent_id
                hierarchy.save()

            # handle child's children and their children and so on forth
            if currentLength > depth:
                # only update string
                newString= currentString.replace(str(idToBeChanged), str(currentHierarchy.parent_id), 1)
                hierarchy.hierarchy_string=newString      
                hierarchy.save()

def create_hierarchystring(taxon):
    hierarchystring = []

    hierarchyParentId = str(taxon.parent_id)

    hierarchyTaxonId = taxon
    while (True):
        hierarchystring.append(str(taxon.taxon_id))
        if taxon.parent_id == 0:
            break
        taxon = TaxonomicUnit.objects.get(taxon_id=taxon.parent_id)

    hierarchystring.reverse()
    hierarchystringFinal = '-'.join(hierarchystring)
    hierarchyLevel = len(hierarchystring) - 1

    new_hierarchy = Hierarchy(
        hierarchy_string=hierarchystringFinal,
        taxon=hierarchyTaxonId,
        parent_id=hierarchyParentId,
        level=hierarchyLevel
        # TODO: childrencount?
    )

    new_hierarchy.save()


def import_data_from_excel(request):
    if request.user.groups.filter(name='contributors').exists():
        try:
            taxons = []
            with open('import_excel.csv', encoding='latin-1') as csvfile:
                file = csv.DictReader(csvfile)
                for row in file:
                    pass
                    revisedrow = {}
                    uncertain = False
                    for key in row:
                        if (row[key].__contains__(",") and row[key] != "author") or row[key].__contains__("incertae sedis"):
                            uncertain = True
                        if row[key] == "\\N":
                            revisedrow[key] = None
                        else:
                            revisedrow[key] = row[key]
                    if uncertain:
                        continue
                    taxons.append(revisedrow)

            # Returns a tuple (model, bool) where the bool is true if the model did not previously exist
            animaliatuple = Kingdom.objects.get_or_create(
                kingdom_name="Animalia")
            if animaliatuple[1]:  # Creates entry for the kingdom animalia
                animaliatuple[0].save()
            animaliaunittypes = [(10, "Kingdom", 10, 10), (20, "Subkingdom", 10, 10), (25, "Infrakingdom", 20, 10),
                                 (27, "Superphylum", 25, 10), (30, "Phylum",
                                                               27, 10), (40, "Subphylum", 30, 30),
                                 (45, "Infraphylum", 40, 30), (50,
                                                               "Superclass", 45, 30), (60, "Class", 50, 30),
                                 (70, "Subclass", 60, 60), (80, "Infraclass",
                                                            70, 60), (90, "Superorder", 80, 60),
                                 (100, "Order", 90, 60), (110, "Suborder",
                                                          100, 100), (120, "Infraorder", 110, 100),
                                 (124, "Section", 120, 100), (126, "Subsection",
                                                              124, 100), (130, "Superfamily", 126, 100),
                                 (140, "Family", 130, 100), (150, "Subfamily",
                                                             140, 140), (160, "Tribe", 150, 140),
                                 (170, "Subtribe", 160, 140), (180, "Genus",
                                                               170, 140), (190, "Subgenus", 180, 180),
                                 (220, "Species", 190, 180), (230, "Subspecies",
                                                              220, 220), (240, "Variety", 220, 220),
                                 (245, "Form", 220, 220), (250, "Race",
                                                           220, 220), (255, "Stirp", 220, 220),
                                 (260, "Morph", 220, 220), (265, "Aberration", 220, 220), (300, "Unspecified", 220, 220)]
            for tut in animaliaunittypes:
                tutple = TaxonUnitType.objects.get_or_create(kingdom=Kingdom.objects.get(kingdom_name="Animalia"), rank_id=tut[0],
                                                             rank_name=tut[1], dir_parent_rank_id=tut[2], req_parent_rank_id=tut[3])

                if tutple[1]:
                    tutple[0].save()  # Creates taxon unit types
            rankorder = {}
            for row in animaliaunittypes:
                rankorder[row[1].lower()] = row[0]
            taxons.sort(key=lambda a: rankorder[a["taxon_level"]])
            # Here we create the top few levels of the hierarchy, since our database doesn't have it
            taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1="Animalia", kingdom=Kingdom.objects.get(kingdom_name="Animalia"),
                                                            parent_id=0, rank=TaxonUnitType.objects.get(kingdom=Kingdom.objects.get(kingdom_name="Animalia"), rank_name="Kingdom"))
            if taxonunit[1]:
                taxonunit[0].save()
                create_hierarchystring(taxonunit[0])

            tophierarchy = [("Bilateria", "Animalia", "Subkingdom"), ("Deuterostomia", "Bilateria", "Infrakingdom"),
                            ("Chordata", "Deuterostomia",
                             "Phylum"), ("Vertebrata", "Chordata", "Subphylum"),
                            ("Gnathostomata", "Vertebrata", "Infraphylum"), ("Tetrapoda",
                                                                             "Gnathostomata", "Superclass"),
                            ("Mammalia", "Tetrapoda", "Class")]

            for taxon in tophierarchy:
                taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1=taxon[0], kingdom=Kingdom.objects.get(kingdom_name="Animalia"),
                                                                parent_id=getattr(TaxonomicUnit.objects.get(
                                                                    unit_name1=taxon[1]), "taxon_id"),
                                                                rank=TaxonUnitType.objects.get(kingdom=Kingdom.objects.get(kingdom_name="Animalia"), rank_name=taxon[2]))
                if taxonunit[1]:
                    taxonunit[0].save()
                    create_hierarchystring(taxonunit[0])

            # Here we create a dummy reference and geographic region
            dummy_reference = Reference.objects.get_or_create(authors = "dummy author", title = "dummy reference")[0].save()
            dummy_geographic_div = GeographicDiv.objects.get_or_create(geographic_value = "dummy geographic division")[0].save()

            # Here we handle the actual taxons
            for taxon in taxons:
                namelist = [taxon["class_name"], taxon["subclass_or_superorder_name"], taxon["order_name"],
                            taxon["suborder_name"], taxon["superfamily_name"], taxon["family_name"],
                            taxon["subfamily_name"], taxon["tribe_name"], taxon["genus_name"], taxon["species_name"]]
                parent_level_list = ["class", "subclass", "order", "suborder", "superfamily", "family", "subfamily", "tribe",
                                "genus", "species"]
                parent_level = None
                level = None
                place = 0
                for i in reversed(range(len(namelist))):
                    if namelist[i] is not None:
                        place += 1
                        if place == 1:
                            level = TaxonUnitType.objects.get(kingdom=Kingdom.objects.get(kingdom_name="Animalia"),
                                                              rank_name = parent_level_list[i].capitalize())
                        if place == 2:
                            parent_level = TaxonUnitType.objects.get(kingdom=Kingdom.objects.get(kingdom_name="Animalia"),
                                                                     rank_name = parent_level_list[i].capitalize())
                            
                namelist = [i.lower().capitalize() for i in namelist if i is not None]

                if len(namelist) >= 2 and len(TaxonomicUnit.objects.filter(unit_name1=namelist[-2], rank=parent_level)) > 1:
                    print(namelist[-2], namelist[-1])

                # Makes sure there is a unique parent
                if len(namelist) >= 2 and len(TaxonomicUnit.objects.filter(unit_name1=namelist[-2], rank=parent_level)) != 1:
                    continue

                taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1=namelist[-1],
                                                                parent_id=TaxonomicUnit.objects.get(unit_name1=namelist[-2], rank = parent_level).taxon_id,
                                                                kingdom=Kingdom.objects.get(kingdom_name="Animalia"),
                                                                rank=level,
                                                                name_usage = "valid",
                                                                complete_name=taxon["taxon_name"].lower().capitalize())

                if level == TaxonUnitType.objects.get(kingdom=Kingdom.objects.get(kingdom_name="Animalia"), rank_name = "Species"):
                    taxonunit[0].unit_name1 = namelist[-2]
                    taxonunit[0].unit_name2 = namelist[-1]
                    
                #taxonunit[0].references.add(dummy_reference)
                #taxonunit[0].geographic_div.add(dummy_geographic_div)
                if taxonunit[1]:
                    taxonunit[0].save()
                    create_hierarchystring(taxonunit[0])

            return HttpResponseRedirect('/admin')
        except Exception as e:
            print(e)
            e = urllib.parse.quote(str(e), safe="")
            return HttpResponseRedirect('/error/' + e)
    return HttpResponseRedirect('/')


def view_reference(request):
    ref_list = Reference.objects.all().filter(visible=1)
    ref_filter = RefFilter(request.GET, queryset=ref_list)
    nresults = ref_filter.qs.count()
    filtered_qs = sorted(ref_filter.qs, key=lambda objects: objects.pk)

    paginator = Paginator(filtered_qs, 20)

    context = {}

    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    querydict = request.GET.copy()

    try:
        del querydict['page']
    except KeyError:
        pass
    context['querystring'] = '&' + querydict.urlencode()

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': ref_filter,
                    'nresults': nresults})
    return render(request, 'front/references.html', context)

def view_reference_details(request, id):
    """ View for individual reference """
    chosenRef = Reference.objects.get(id=id)
    
    # Get reference's history as records
    records = chosenRef.history.all()
    history = {}
    history = _create_history_records(history, records)

    context = {'reference': chosenRef, 'history': history}
    return render(request, 'front/ref-details.html', context)


def search_references(request):
    ref_list = Reference.objects.all().filter(visible=1)
    ref_filter = RefFilter(request.GET, queryset=ref_list)
    nresults = ref_filter.qs.count()
    filtered_qs = sorted(ref_filter.qs, key=lambda objects: objects.pk)

    paginator = Paginator(filtered_qs, 10)

    c = {}
    if request.GET:
        page = request.GET.get('page')
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        querydict = request.GET.copy()
        try:
            del querydict['page']
        except KeyError:
            pass
        c['querystring'] = '&' + querydict.urlencode()
    else:
        response = None

    c.update({'filter': ref_filter,
              'page_obj': response,
              'nresults': nresults,
              'paginator': paginator})
    return render(request, 'front/reference-search.html', c)


def refs_add(request, pk=None):
    c = {'pk': pk if pk else ''}
    if request.method == 'POST':
        ref = None
        if pk:
            ref = Reference.objects.get(pk=pk)
        form = RefForm(request.POST, instance=ref)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        try:
            ref = Reference.objects.get(pk=pk)
            c['title'] = 'Edit'
        except Reference.DoesNotExist:
            ref = None
            c['title'] = 'Add'
        form = RefForm(instance=ref)
    doi_form = DoiForm(initial={'doi':'10.'})
    bibtex_form = BibtexForm(initial={'bib':'@'})
    c['doiform'] = doi_form
    c['bibtexform'] = bibtex_form
    c['form'] = form
    return render(request, 'front/add-reference.html', c)

def _fill_form_with_initial_values(parsed_bibtex: dict, bibtex: dict):
    """Fills RefForm with initial values by bibtex"""
    initial_values = {'author': '', 'title':'', 'doi':'',
     'journal':'', 'year':'', 'volume':'', 'number':'',
     'url':'', 'bibtex':'', 'page_start':'', 'page_end':''}

    for key in initial_values.keys():
        if key in parsed_bibtex.keys():
            initial_values[key] = parsed_bibtex[key]
    if 'pages' in parsed_bibtex.keys():
        splitted = parsed_bibtex['pages'].split('-')
        pages = []
        for c in splitted:
            try:
                pages.append(int(c))
            except:
                continue
        initial_values['page_start'] = pages[0]
        initial_values['page_end'] = pages[len(pages)-1]       

    form = RefForm(initial={
    'authors': initial_values['author'],
    'title': initial_values['title'],
    'doi': initial_values['doi'],
    'journal': initial_values['journal'],
    'year': initial_values['year'],
    'volume': initial_values['volume'],
    'article_number': initial_values['number'],
    'url': initial_values['url'],
    'page_start': initial_values['page_start'],
    'page_end': initial_values['page_end'],
    'bibtex':bibtex
    })

    return form

def _parse_bibtex(bibtex_string):
    """ Parses bibtex string to a dictionary """
    bp = BibTexParser(interpolate_strings=False)
    bib_database = bp.parse(bibtex_string)
    return bib_database.entries[0]

def doi_auto_fill(request):
    """ Autofills reference details using bibtex
    information fetched from dx.doi API.

    Args:
        request (GET): http://dx.doi.org/10.1038/nrd842

    Returns:
        string: reference information in bibtex format
    """
    
    doi_form = DoiForm(request.POST)
    bibtex_form = BibtexForm(initial={'bib':'@'})
    form = RefForm()

    if doi_form.is_valid():

        url = 'https://dx.doi.org/{}'.format(doi_form.cleaned_data.get("doi"))
        payload={}
        headers = {'Accept': 'application/x-bibtex'}
        try:   
            response = requests.request("GET", url, headers=headers, data=payload)
            bib = _parse_bibtex(response.text)
            form = _fill_form_with_initial_values(bib, response.text)
                       
        except:
            messages.error(request, 'Data could not be retrieved')

    context= {'form': form, 'doiform': doi_form, 'bibtexform': bibtex_form}
    return render(request, 'front/add-reference.html', context)

def bibtex_auto_fill(request):
    """ Autofills reference details using bibtex
    information fetched from dx.doi API.

    Args:
        request (GET): http://dx.doi.org/10.1038/nrd842

    Returns:
        string: reference information in bibtex format
    """
    
    doi_form = DoiForm(initial={'doi':'10.'})
    bibtex_form = BibtexForm(request.POST)
    form = RefForm()

    if bibtex_form.is_valid():
        bibtex_string = bibtex_form.cleaned_data.get("bib")
        try:
            bib = _parse_bibtex(bibtex_string)
            form = _fill_form_with_initial_values(bib, bibtex_string)
        except IndexError:
            messages.error(request, 'BibTex not in the correct format.')

    context= {'form': form, 'doiform': doi_form, 'bibtexform': bibtex_form}
    return render(request, 'front/add-reference.html', context)

def delete(request, pk):
    if request.user.groups.filter(name='contributors').exists():
        ref = get_object_or_404(Reference, pk=pk)
        ref.visible = 0
        ref.doi = ''
        ref.title = ref.title + ' (removed)'
        ref.save()
        return HttpResponseRedirect('/references')
    return HttpResponseRedirect('/references')

def view_taxa(request):
    # Get all the taxa
    taxa_all = TaxonomicUnit.objects.all()
    # Set up filter
    taxon_filter = TaxonFilter(request.GET, queryset=taxa_all)
    # Total amount of results
    nresults = taxon_filter.qs.count()
    # Sort by taxon's unit name1
    filtered_qs = sorted(
        taxon_filter.qs, key=lambda objects: objects.unit_name1.lower())
    # Set up Pagination, 20 taxa per page
    paginator = Paginator(filtered_qs, 20)

    context = {}

    # Track current page
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    querydict = request.GET.copy()

    try:
        del querydict['page']
    except KeyError:
        pass
    # Specify the filter parameter to build a querystring together with pagination
    context['querystring'] = '&' + querydict.urlencode()

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': taxon_filter,
                    'nresults': nresults})

    return render(request, 'front/taxa.html', context)


def search_taxa(request):
    # Get all the taxa
    taxa_all = TaxonomicUnit.objects.all()
    # Set up filter
    taxon_filter = TaxonFilter(request.GET, queryset=taxa_all)
    # Total amount of results
    nresults = taxon_filter.qs.count()
    # Sort by taxon's unit name1

    filtered_qs = sorted(
        taxon_filter.qs, key=lambda objects: objects.unit_name1.lower())
    # Set up Pagination, 10 taxa per page
    paginator = Paginator(filtered_qs, 10)

    context = {}
    if request.GET:
        page = request.GET.get('page')
        try:
            # Track current page
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        querydict = request.GET.copy()
        try:
            del querydict['page']
        except KeyError:
            pass
        # Specify the filter parameter to build a querystring together with pagination
        context['querystring'] = '&' + querydict.urlencode()
    else:
        response = None

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': taxon_filter,
                    'nresults': nresults})

    return render(request, 'front/taxa-search.html', context)

def view_hierarchy(request, parent_id=None):
    """ View for individual taxon """
    chosenTaxon = TaxonomicUnit.objects.get(taxon_id=parent_id)
    childTaxa = TaxonomicUnit.objects.filter(parent_id=chosenTaxon.taxon_id)

    # Get taxon's history as records
    records = chosenTaxon.history.all()
    history = {}
    
    # Get the first reference related to the taxon
    first_ref = ""
    try:
        first_ref = f"{records[0].reference.authors}. {records[0].reference.title}."
    except:
        print("Couldn't get initial reference.")

    # Add update history to 'history' dict, one update (record) at a time
    try:
        for record in records:
            if record.prev_record:
                timestamp = record.history_date
                history[timestamp] = {}
                history[timestamp]['user'] = record.history_user.username
                history[timestamp]['changes'] = ''
                history[timestamp]['reference'] = f"{record.reference.authors}. {record.reference.title}."
                delta = record.diff_against(record.prev_record)
                for change in delta.changes:
                    if change.field != 'reference':
                        if len(history[timestamp]['changes']) == 0:
                            history[timestamp]['changes'] = "{} changed from {} to {}".format(change.field.capitalize(), change.old, change.new)
                        else:
                            (history[timestamp]['changes']) += ",\n{} changed from {} to {}".format(change.field.capitalize(), change.old, change.new)
                if len(history[timestamp]['changes']) == 0:
                    history[timestamp]['changes'] = "Not available."
    except:
        print("An error occured while fetching taxon history records.")
        
    # Select experts
    percentage = '%'
    taxon_experts = Expert.objects.raw("""
        SELECT DISTINCT e.id, e.expert
        FROM front_expert e
        JOIN front_taxonomicunit_expert et ON et.expert_id=e.id
        JOIN front_expert_geographic_div eg ON eg.expert_id=e.id
        JOIN front_taxonomicunit tu ON tu.taxon_id=et.taxonomicunit_id
        JOIN front_hierarchy h ON h.hierarchy_string LIKE CONCAT(%s,'-', tu.taxon_id ,'-',%s)
        or h.hierarchy_string LIKE CONCAT(%s,'-', tu.taxon_id)
        JOIN front_taxonomicunit tu2 ON tu2.taxon_id=h.taxon_id
        JOIN front_geographicdiv g ON g.id=eg.geographicdiv_id
        JOIN front_taxonomicunit_geographic_div tug ON tug.taxonomicunit_id=tu2.taxon_id
        AND tug.geographicdiv_id=eg.geographicdiv_id
        WHERE tu2.taxon_id = %s
        """, [percentage, percentage, percentage, chosenTaxon.taxon_id])

    # taxon_experts = chosenTaxon.expert.all()

    hierarchyObject = Hierarchy.objects.get(taxon=chosenTaxon)
    # Get the synonym_ids of those taxons, where the accepted_taxon_id matches with
    # chosenTaxon.taxon_id, i.e., the ids of those taxons that are synonyms
    # of the one we are currently looking at. This list will need to be filtered
    # further to match rank, if we consider only those taxons synonyms, which share the
    # the same rank.
    taxonSynonyms = SynonymLink.objects.filter(taxon_id_accepted_id=chosenTaxon.taxon_id)#.only("synonym_id")
    # List of only ids
    taxonSynonymIds = [x.synonym_id for x in taxonSynonyms]
    # Only those taxons where the rank is the same as the rank of the taxon we're currently looking at.
    synonymTaxons = TaxonomicUnit.objects.filter(pk__in=taxonSynonymIds)#.filter(rank=chosenTaxon.rank)

    if len(SynonymLink.objects.filter(synonym_id=chosenTaxon.taxon_id)) > 0:
        seniorSynonym = TaxonomicUnit.objects.get(taxon_id = SynonymLink.objects.get(synonym_id=chosenTaxon.taxon_id).taxon_id_accepted.taxon_id)
    else:
        seniorSynonym = None
    hierarchy = hierarchyObject.hierarchy_string.split('-')

    name_list = []
    grow = 0

    while (len(hierarchy) != 0):
        index = hierarchy.pop(0)
        if len(TaxonomicUnit.objects.filter(taxon_id=index)) == 1:
            root = TaxonomicUnit.objects.get(taxon_id=index)
        else:
            root = None

        # if (len(hierarchy) == 0):
        #     # This takes only the reference for the selected taxon.
        #     # E.G. User chooses Deuterostomia -> this takes the refenences for deuterostomia and not for the parent taxons
        #     references.append(root.references.all())

        space = "&nbsp" * grow

        if root is None:
            name_list.append((space + "Missing taxon", None))
        else:
            name = space + root.rank.rank_name
            name_list.append((name, root))
        grow += 2

    context = {
        'taxonomic_unit': chosenTaxon,
        'taxon_experts': taxon_experts,
        'childTaxa': childTaxa,
        'name_list': name_list,
        # 'references': references[0],
        'synonyms': synonymTaxons,
        'seniorSynonym': seniorSynonym,
        'isJunior': seniorSynonym is not None,
        'history': history,
        'first_ref': first_ref
    }

    return render(request, 'front/hierarchy.html', context)

def add_junior_synonym(request, taxon_id=None):
    #works similiarly to add_name
    if request.method == 'POST':
        form = JuniorSynonymForm(request.POST)

        if form.is_valid():
            try:
                taxon = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['synonym_id'])
                if taxon.kingdom in ["Chromista", "Fungi", "Plantae"]:
                    taxon.name_usage = "not accepted"
                    taxon.unaccept_reason = "synonym"
                else:
                    taxon.name_usage = "invalid"
                    taxon.unaccept_reason= "junior synonym"
                taxon.save()
                SynonymLink.objects.create(synonym_id = taxon.taxon_id, taxon_id_accepted = TaxonomicUnit.objects.get(taxon_id = taxon_id)).save()
                children = TaxonomicUnit.objects.filter(parent_id = taxon.taxon_id)
                if len(children) > 0:
                    for child in children:
                        child.parent_id = taxon_id
                        #hierarchyObject = Hierarchy.objects.get(taxon=child)
                        child.save()
                        #hierarchy = hierarchyObject.hierarchy_string.split("-")
                        #hierarchy[-2] = taxon_id
                        #hierarchyObject.hierarchy_string = "-".join(hierarchy)
                        #hierarchyObject.save()
                        
            except:
                print("error in adding junior synonym")
            
            return HttpResponseRedirect(f'/hierarchy/{taxon_id}')

    else:
        form = JuniorSynonymForm()
    return render(request, 'front/add_junior_synonym.html', {'form': form})


def view_experts(request):
    experts = Expert.objects.all()
    expert_filter = ExpertFilter(request.GET, queryset=experts)
    nresults = expert_filter.qs.count()
    filtered_qs = sorted(
        expert_filter.qs, key=lambda objects: objects.expert.lower())

    paginator = Paginator(filtered_qs, 20)
    context = {}

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    querydict = request.GET.copy()

    try:
        del querydict['page']
    except KeyError:
        pass

    context['querystring'] = '&' + querydict.urlencode()

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': expert_filter,
                    'nresults': nresults})
    return render(request, 'front/experts.html', context)

def view_expert_details(request, id):
    """ View for individual expert """
    chosenExpert = Expert.objects.get(id=id)
    geo_divs = chosenExpert.geographic_div.all()
    
    # Get expert's history as records
    records = chosenExpert.history.all()
    history = {}
    history = _create_history_records(history, records)

    context = {'expert': chosenExpert, 'history': history, 'geos': geo_divs}
    return render(request, 'front/expert-details.html', context)

def search_experts(request):

    experts = Expert.objects.all()
    expert_filter = ExpertFilter(request.GET, queryset=experts)
    
    filtered_qs = sorted(
        expert_filter.qs, key=lambda objects: objects.expert.lower())
    nresults = len(filtered_qs)

    paginator = Paginator(filtered_qs, 10)

    context = {}
    if request.GET:
        page = request.GET.get('page')
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        querydict = request.GET.copy()
        try:
            del querydict['page']
        except KeyError:
            pass

        context['querystring'] = '&' + querydict.urlencode()
    else:
        response = None

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': expert_filter,
                    'nresults': nresults})

    return render(request, 'front/expert-search.html', context)


def add_expert(request, pk=None):
    context = {'pk': pk if pk else ''}
    if request.method == 'POST':
        expert = None
        if pk:
            expert = Expert.objects.get(pk=pk)
        form = ExpertForm(request.POST, instance=expert)
        if form.is_valid():
            try:
                new_expert = form.save(commit=False)
                new_expert.save()

                geos = form.cleaned_data['geographic_div']
                for geo in geos:
                    new_expert.geographic_div.add(geo)
            except Expert.DoesNotExist:
                print("Saving a new expert did not workout; do something")
            return HttpResponseRedirect('/experts')
    else:
        try:
            expert = Expert.objects.get(pk=pk)
            context['title'] = 'Edit'
        except Expert.DoesNotExist:
            expert = None
            context['title'] = 'Add'
        form = ExpertForm(instance=expert)
    context['form'] = form
    return render(request, 'front/add-expert.html', context)

def view_authors(request):
    authors = TaxonAuthorLkp.objects.all()
    author_filter = AuthorFilter(request.GET, queryset=authors)
    nresults = author_filter.qs.count()
    filtered_qs = sorted(
        author_filter.qs, key=lambda objects: objects.taxon_author.lower())

    paginator = Paginator(filtered_qs, 20)
    context = {}
    
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    querydict = request.GET.copy()

    try:
        del querydict['page']
    except KeyError:
        pass

    context['querystring'] = '&' + querydict.urlencode()

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': author_filter,
                    'nresults': nresults})

    return render(request, 'front/authors.html', context)

def view_author_details(request, id):
    """ View for individual author """
    chosenAuthor = TaxonAuthorLkp.objects.get(taxon_author_id=id)
    
    # Get author's history as records
    records = chosenAuthor.history.all()
    history = {}
    history = _create_history_records(history, records)

    context = {'author': chosenAuthor, 'history': history}
    return render(request, 'front/author-details.html', context)

def search_authors(request):

    authors = TaxonAuthorLkp.objects.all()
    author_filter = AuthorFilter(request.GET, queryset=authors)
    
    filtered_qs = sorted(
        author_filter.qs, key=lambda objects: objects.taxon_author.lower())
    nresults = len(filtered_qs)

    paginator = Paginator(filtered_qs, 10)

    context = {}
    if request.GET:
        page = request.GET.get('page')
        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        querydict = request.GET.copy()
        try:
            del querydict['page']
        except KeyError:
            pass

        context['querystring'] = '&' + querydict.urlencode()
    else:
        response = None

    context.update({'page_obj': response,
                    'paginator': paginator,
                    'filter': author_filter,
                    'nresults': nresults})

    return render(request, 'front/author-search.html', context)

def add_author(request, pk=None):
    context = {'pk': pk if pk else ''}
    if request.method == 'POST':
        author = None
        if pk:
            author = TaxonAuthorLkp.objects.get(pk=pk)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            try:
                new_author = form.save(commit=False)
                new_author.save()
            except TaxonAuthorLkp.DoesNotExist:
                print("Saving a new author did not workout; do something")
            return HttpResponseRedirect('/authors')
    else:
        try:
            author = TaxonAuthorLkp.objects.get(pk=pk)
            context['title'] = 'Edit'
        except TaxonAuthorLkp.DoesNotExist:
            author = None
            context['title'] = 'Add'
        form = AuthorForm(instance=author)
    context['form'] = form
    return render(request, 'front/add-author.html', context)

def help(request):
    return render(request, 'front/help.html')

def _create_history_records(history, records):
    # Add update history to 'history' dict, one update (record) at a time
    try:
        for record in records:
            if record.prev_record:
                timestamp = record.history_date
                history[timestamp] = {}
                history[timestamp]['user'] = record.history_user.username
                history[timestamp]['changes'] = ''
                delta = record.diff_against(record.prev_record)
                for change in delta.changes:
                    if len(history[timestamp]['changes']) == 0:
                        history[timestamp]['changes'] = "{} changed from {} to {}".format(change.field.capitalize(), change.old, change.new)
                    else:
                        (history[timestamp]['changes']) += ",\n{} changed from {} to {}".format(change.field.capitalize(), change.old, change.new)
                if len(history[timestamp]['changes']) == 0:
                    history[timestamp]['changes'] = "Not available."
    except:
        print("An error occured while fetching reference history records.")
    return history
