import string
from xxlimited import new
from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django import forms

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import user_passes_test
from front.models import Reference, get_ref_from_doi
from .models import Hierarchy, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, Kingdom, Expert, SynonymLink, Reference, GeographicDiv
from front.utils import canonicalize_doi
from front.forms import RefForm, TaxonForm, ExpertForm, AuthorForm, JuniorSynonymForm
from front.filters import RefFilter, TaxonFilter
from django.contrib.auth.decorators import login_required
from datetime import datetime

from front.forms import RefForm, TaxonForm, ExpertForm, AuthorForm, JuniorSynonymForm
from front.filters import RefFilter, TaxonFilter
from django.contrib.auth.decorators import login_required
import csv, urllib.parse


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
            taxon = TaxonomicUnit.objects.get(pk=pk)        
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

                # if rank_of_new_taxon.rank_name=='Subkingdom':
                #   parent = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['kingdom_name'])
                # else:
                parent = TaxonomicUnit.objects.get(
                    unit_name1=form.cleaned_data['rank_name'],
                    kingdom=kingdom
                )

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

                #save new unit =name
                
                # modify old taxon's name validity, if taxon is edited
                #if pk: #& new_unit.unit_name1 != taxon.unit_name1
                    #taxon.n_usage = "invalid"    
                    #taxon.save()    
                #new_unit.n_usage = "valid"

                new_unit.save()

                #add SynonymLink
                if form.cleaned_data["is_junior_synonym"] and form.cleaned_data["senior_synonym"] != "":
                    SynonymLink.objects.create(synonym_id = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data["unit_name1"]).taxon_id, taxon_id_accepted=TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data["senior_synonym"]), update_date = datetime.now()).save()
                        
                new_unit.save()
                refs = form.cleaned_data['references']
                for ref in refs:
                    new_unit.references.add(ref)
                geos = form.cleaned_data['geographic_div']
                for geo in geos:
                    new_unit.geographic_div.add(geo)
                experts = form.cleaned_data['expert']
                for expert in experts:
                    new_unit.expert.add(expert)
                author = form.cleaned_data['taxon_author_id']
                new_unit.taxon_author_id=author
                new_unit.save()
               
                if pk:
                    move_taxon_update_hierarchystring(taxon)
                else:
                    create_hierarchystring(new_unit)                                    
            except TaxonomicUnit.DoesNotExist:
                # form was filled incorrectly
                print("saving new unit did not workout; do something")
            return HttpResponseRedirect('/taxa')

    # if a GET (or any other method) we'll create a blank form
    else:
        # edit existing taxon
        try:
            taxon = TaxonomicUnit.objects.get(pk=pk)
            parent =TaxonomicUnit.objects.get(pk=taxon.parent_id)

            form = TaxonForm(initial={
            'kingdom_name': taxon.kingdom,
            #rank name and parent name's are initialized by add-taxon.html
            'unit_name1': taxon.unit_name1,
            'unit_name2': taxon.unit_name2,
            'unit_name3': taxon.unit_name3,
            'unit_name4': taxon.unit_name4,
            'references': taxon.references.values_list('id', flat=True),
            'geographic_div': taxon.geographic_div.values_list('id', flat=True)
             })

        except TaxonomicUnit.DoesNotExist:
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
    hierarchies= Hierarchy.objects.filter(hierarchy_string__contains=idToBeChanged)
    
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
                newString= currentString.replace(str(idToBeChanged), str(currentHierarchy.parent_id))
                hierarchy.hierarchy_string=newString
                # update hierarchy's parent also
                hierarchy.parent_id = taxon.parent_id
                hierarchy.save()

            # handle child's children and their children and so on forth
            if currentLength > depth:
                # only update string
                newString= currentString.replace(str(idToBeChanged), str(currentHierarchy.parent_id))
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

                taxonunit[0].references.add(dummy_reference)
                taxonunit[0].geographic_div.add(dummy_geographic_div)
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
    refs = Reference.objects.all().filter(visible=1)
    paginator = Paginator(refs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    c = {'page_obj': page_obj, 'paginator': paginator}
    return render(request, 'front/references.html', c)


def search(request):
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
        except Reference.DoesNotExist:
            ref = None
        form = RefForm(instance=ref)

    c['form'] = form
    return render(request, 'front/add-reference.html', c)


def delete(request, pk):
    if request.user.groups.filter(name='contributors').exists():
        ref = get_object_or_404(Reference, pk=pk)
        ref.visible = 0
        ref.doi = ''
        ref.title = ref.title + ' (removed)'
        ref.save()
        return HttpResponseRedirect('/references')
    return HttpResponseRedirect('/references')


def resolve(request, pk=None):
    # Look up DOI and pre-populate form, render to front/add.html
    if request.method == 'GET':
        doi = request.GET.get('doi')
        doi = canonicalize_doi(doi)
        if not pk:
            try:
                # We're trying to add a reference but one with the same DOI
                # is in the database already.
                ref = Reference.objects.get(doi=doi)
                return HttpResponseRedirect(f'/front/add-reference/{ref.pk}')
            except Reference.DoesNotExist:
                ref = None
        else:
            ref = get_object_or_404(Reference, pk=pk)
        ref = get_ref_from_doi(doi, ref)
        form = RefForm(instance=Reference)
        c = {'form': form, 'pk': pk if pk else ''}
        return render(request, 'front/add-reference.html', c)
    raise Http404


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
    # Specify the filter parameter to build to build a querystring together with pagination
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
    print(request.GET)
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
        # Specify the filter parameter to build to build a querystring together with pagination
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
    hierarchyObject = Hierarchy.objects.get(taxon=chosenTaxon)
    # Get the synonym_ids of those taxons, where the accepted_taxon_id matches with
    # chosenTaxon.taxon_id, i.e., the ids of those taxons that are synonyms
    # of the one we are currently looking at. This list will need to be filtered
    # further to match rank, if we consider only those taxons synonyms, which share the
    # the same rank.
    print(chosenTaxon)
    taxonSynonyms = SynonymLink.objects.filter(taxon_id_accepted_id=chosenTaxon.taxon_id)#.only("synonym_id")
    print(taxonSynonyms)
    # List of only ids
    taxonSynonymIds = [x.synonym_id for x in taxonSynonyms]
    print(taxonSynonymIds)
    # Only those taxons where the rank is the same as the rank of the taxon we're currently looking at.
    synonymTaxons = TaxonomicUnit.objects.filter(pk__in=taxonSynonymIds)#.filter(rank=chosenTaxon.rank)

    if len(SynonymLink.objects.filter(synonym_id=chosenTaxon.taxon_id)) > 0:
        seniorSynonym = TaxonomicUnit.objects.get(taxon_id = SynonymLink.objects.get(synonym_id=chosenTaxon.taxon_id).taxon_id_accepted.taxon_id)
    else:
        seniorSynonym = None
    hierarchy = hierarchyObject.hierarchy_string.split('-')

    # TODO result array seems useless?
    # result = []
    name_list = []
    grow = 0

    references = []

    while (len(hierarchy) != 0):
        index = hierarchy.pop(0)
        if len(TaxonomicUnit.objects.filter(taxon_id=index)) == 1:
            root = TaxonomicUnit.objects.get(taxon_id=index)
        else:
            root = None

        if (len(hierarchy) == 0):
            # This takes only the reference for the selected taxon.
            # E.G. User chooses Deuterostomia -> this takes the refenences for deuterostomia and not for the parent taxons
            references.append(root.references.all())

        space = "&nbsp" * grow

        if root is None:
            name_list.append((space + "Missing taxon", None))
        else:
            name = space + root.rank.rank_name
            name_list.append((name, root))
        # result.append(root)
        grow += 2

    context = {
        'taxonomic_unit': chosenTaxon,
        # 'hierarchies': result,
        'name_list': name_list,
        'references': references[0],
        'synonyms': synonymTaxons,
        'seniorSynonym': seniorSynonym,
        'isJunior': seniorSynonym is not None
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
                SynonymLink.objects.create(synonym_id = taxon.taxon_id, taxon_id_accepted = TaxonomicUnit.objects.get(taxon_id = taxon_id), update_date = datetime.now()).save()
                children = TaxonomicUnit.objects.filter(parent_id = taxon.taxon_id)
                if len(children) > 0:
                    for child in children:
                        child.parent_id = taxon_id
                        hierarchyObject = Hierarchy.objects.get(taxon=child)
                        child.save()
                        hierarchy = hierarchyObject.hierarchy_string.split("-")
                        hierarchy[-2] = taxon_id
                        hierarchyObject.hierarchy_string = "-".join(hierarchy)
                        hierarchyObject.save()
                        
            except:
                print("error in adding junior synonym")
            
            return HttpResponseRedirect(f'/hierarchy/{taxon_id}')

    else:
        form = JuniorSynonymForm()
    return render(request, 'front/add_junior_synonym.html', {'form': form})
    
def view_experts(request):
    experts = Expert.objects.all()
    sorted_experts = sorted(
        experts, key=lambda objects: objects.expert.lower())
    paginator = Paginator(sorted_experts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'paginator': paginator, 'page_obj': page_obj}
    return render(request, 'front/experts.html', context)


def add_expert(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST)
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
        form = ExpertForm()
    return render(request, 'front/add-expert.html', {'form': form})

def view_authors(request):
    authors = TaxonAuthorLkp.objects.all()
    sorted_authors = sorted(
        authors, key=lambda objects: objects.taxon_author.lower())
    paginator = Paginator(sorted_authors, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'paginator': paginator, 'page_obj': page_obj}
    return render(request, 'front/authors.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                new_author = form.save(commit=False)
                new_author.save()
            except TaxonAuthorLkp.DoesNotExist:
                print("saving new author did not workout; do something")
            return HttpResponseRedirect('/authors')
    else:
        form = AuthorForm()
    return render(request, 'front/add-author.html', {'form': form})
def view_experts(request):
    experts = Expert.objects.all()
    sorted_experts = sorted(
        experts, key=lambda objects: objects.expert.lower())
    paginator = Paginator(sorted_experts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'paginator': paginator, 'page_obj': page_obj}
    return render(request, 'front/experts.html', context)


def add_expert(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST)
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
        form = ExpertForm()
    return render(request, 'front/add-expert.html', {'form': form})

def view_authors(request):
    authors = TaxonAuthorLkp.objects.all()
    sorted_authors = sorted(
        authors, key=lambda objects: objects.taxon_author.lower())
    paginator = Paginator(sorted_authors, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'paginator': paginator, 'page_obj': page_obj}
    return render(request, 'front/authors.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                new_author = form.save(commit=False)
                new_author.save()
            except TaxonAuthorLkp.DoesNotExist:
                print("saving new author did not workout; do something")
            return HttpResponseRedirect('/authors')
    else:
        form = AuthorForm()
    return render(request, 'front/add-author.html', {'form': form})

def help(request):
    return render(request, 'front/help.html')
