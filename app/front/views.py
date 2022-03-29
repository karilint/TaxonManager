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
from .models import Hierarchy, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, Kingdom
from front.utils import canonicalize_doi
from front.forms import RefForm, NameForm, AuthorForm
from front.filters import RefFilter, TaxonFilter
from django.contrib.auth.decorators import login_required
from .models import TaxonomicUnit
import csv



def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference
def login(request):
    return render(request, 'front/login.html')


def load_rankOfTaxonToBeAdded(request):
    kingdomId = request.GET.get('id')
    kingdomName = Kingdom.objects.get(id=kingdomId)

    rankOfTaxonToBeAdded = TaxonUnitType.objects.exclude(rank_name='Kingdom').filter(kingdom = kingdomName)

    return render(request, 'front/rankOfTaxonToBeAdded.html', {'rankOfTaxonToBeAdded': rankOfTaxonToBeAdded})

def load_parentTaxon(request):
    taxonnomicTypeName = request.GET.get('id')
    kingdomId = request.GET.get('kingdomId')
    kingdom = Kingdom.objects.get(pk=kingdomId)

    taxontype = TaxonUnitType.objects.get(rank_name=taxonnomicTypeName, kingdom=kingdom)

    all_prev_taxons = TaxonUnitType.objects.filter(rank_id__range=(taxontype.req_parent_rank_id, taxontype.dir_parent_rank_id), kingdom=taxontype.kingdom)
    all_prev_taxons_rank = [taxon for taxon in all_prev_taxons]

    parentTaxon = TaxonomicUnit.objects.filter(rank__in=all_prev_taxons_rank)

    return render(request, 'front/parentTaxon.html', {'parentTaxon': parentTaxon})


def taxon_add(request):   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():  
            try:
                # save names from Modelform, but don't admit new unit to db yet
                new_unit = form.save(commit=False)
                kingdom = Kingdom.objects.get(kingdom_name=form.cleaned_data['kingdom_name'])
                rank_of_new_taxon = TaxonUnitType.objects.get(rank_name = form.cleaned_data['taxonnomic_types'], kingdom = kingdom)

                #if rank_of_new_taxon.rank_name=='Subkingdom':
                 #   parent = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['kingdom_name'])
                #else:
                
                parent = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['rank_name'])   
                
                # set new unit's parent
                new_unit.parent_id = parent.taxon_id
                # and kingdom based on parent
                new_unit.kingdom = parent.kingdom

                
            
                #FIX: set author (can be something or null)
                # if it is something:
                # 1. set correct taxon_author_id for new unit by references(and handle publications vs. experts) or what?
                # do here: some db -queries
                # set author here: new_unit.taxon_author_id = SUITABLE FOUND taxon_author_id

                #else if there's no author:
                #get rank by kingdom name and rank name + set rank to new unit
                new_unit.rank = rank_of_new_taxon

                new_unit.save()
                refs = form.cleaned_data['references']
                for ref in refs:
                    new_unit.references.add(ref)
                create_hierarchystring(new_unit)
            except TaxonomicUnit.DoesNotExist:
                # form was filled incorrectly
                print("saving new unit did not workout; do something")
            return HttpResponseRedirect('/taxa')
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'front/add_name.html', {'form': form})

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
        #TODO: childrencount?
    )
    
    new_hierarchy.save()
    
def import_data_from_excel(request):
    try:
        taxons = []
        with open('import_excel.csv', encoding='latin-1') as csvfile:
            file = csv.DictReader(csvfile)
            for row in file:
                pass
                revisedrow = {}
                uncertain = False
                for key in row:
                    if (row[key].__contains__(",")  and row[key] != "author") or row[key].__contains__("incertae sedis"):
                        uncertain = True
                    if row[key] == "\\N":
                        revisedrow[key] = None
                    else:
                        revisedrow[key] = row[key]
                if uncertain:
                    continue
                taxons.append(revisedrow)


        animaliatuple = Kingdom.objects.get_or_create(kingdom_name="Animalia") #Returns a tuple (model, bool) where the bool is true if the model did not previously exist
        if animaliatuple[1]:# Creates entry for the kingdom animalia
            animaliatuple[0].save()
        animaliaunittypes = [(10, "Kingdom", 10, 10), (20, "Subkingdom", 10, 10), (25, "Infrakingdom", 20, 10),
                             (27, "Superphylum", 25, 10), (30, "Phylum", 27, 10), (40, "Subphylum", 30, 30),
                             (45, "Infraphylum", 40, 30), (50, "Superclass", 45, 30), (60, "Class", 50, 30),
                             (70, "Subclass", 60, 60), (80, "Infraclass", 70, 60), (90, "Superorder", 80, 60),
                             (100, "Order", 90, 60), (110, "Suborder", 100, 100), (120, "Infraorder", 110, 100),
                             (124, "Section", 120, 100), (126, "Subsection", 124, 100), (130, "Superfamily", 126, 100),
                             (140, "Family", 130, 100), (150, "Subfamily", 140, 140), (160, "Tribe", 150, 140),
                             (170, "Subtribe", 160, 140), (180, "Genus", 170, 140), (190, "Subgenus", 180, 180),
                             (220, "Species", 190, 180), (230, "Subspecies", 220, 220), (240, "Variety", 220, 220),
                             (245, "Form", 220, 220), (250, "Race", 220, 220), (255, "Stirp", 220, 220),
                             (260, "Morph", 220, 220), (265, "Aberration", 220, 220), (300, "Unspecified", 220, 220)]
        for tut in animaliaunittypes:
            tutple = TaxonUnitType.objects.get_or_create(kingdom=Kingdom.objects.get(kingdom_name = "Animalia"), rank_id=tut[0],
                                                         rank_name=tut[1], dir_parent_rank_id=tut[2], req_parent_rank_id=tut[3])


            if tutple[1]:
                tutple[0].save() #Creates taxon unit types
        rankorder = {}
        for row in animaliaunittypes:
            rankorder[row[1].lower()] = row[0]
        taxons.sort(key=lambda a : rankorder[a["taxon_level"]])
        # Here we create the top few levels of the hierarchy, since our database doesn't have it
        taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1="Animalia", kingdom=Kingdom.objects.get(kingdom_name = "Animalia"),
                                                    parent_id=0, rank=TaxonUnitType.objects.get(rank_name = "Kingdom"))
        if taxonunit[1]:
            taxonunit[0].save()
            create_hierarchystring(taxonunit[0])

        
        tophierarchy = [("Bilateria", "Animalia", "Subkingdom"), ("Deuterostomia", "Bilateria", "Infrakingdom"),
                        ("Chordata", "Deuterostomia", "Phylum"), ("Vertebrata", "Chordata", "Subphylum"),
                        ("Gnathostomata", "Vertebrata", "Infraphylum"), ("Tetrapoda", "Gnathostomata", "Superclass"),
                        ("Mammalia", "Tetrapoda", "Class")]

        for taxon in tophierarchy:
            taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1=taxon[0], kingdom=Kingdom.objects.get(kingdom_name = "Animalia"),
                                                        parent_id=getattr(TaxonomicUnit.objects.get(unit_name1=taxon[1]),"taxon_id"),
                                                        rank=TaxonUnitType.objects.get(rank_name = taxon[2]))
            if taxonunit[1]:
                taxonunit[0].save()
                create_hierarchystring(taxonunit[0])

        for taxon in taxons:
            namelist = [taxon["class_name"], taxon["subclass_or_superorder_name"], taxon["order_name"],
                        taxon["suborder_name"], taxon["superfamily_name"], taxon["family_name"],
                        taxon["subfamily_name"], taxon["tribe_name"], taxon["genus_name"], taxon["species_name"]]
            namelist = [i.lower().capitalize() for i in namelist if i is not None]

            if len(namelist) >= 2 and len(TaxonomicUnit.objects.filter(unit_name1=namelist[-2])) > 1:
                print(namelist[-2], namelist[-1])

            if len(namelist) >= 2 and len(TaxonomicUnit.objects.filter(unit_name1=namelist[-2])) != 1: #Makes sure there is a unique parent
                continue

            taxonunit = TaxonomicUnit.objects.get_or_create(unit_name1=namelist[-1], parent_id=getattr(TaxonomicUnit.objects.get_or_create(unit_name1=namelist[-2])[0],"taxon_id"),
                                                        kingdom=Kingdom.objects.get(kingdom_name = "Animalia"),
                                                        rank=TaxonUnitType.objects.get(rank_name=taxon["taxon_level"].capitalize()),
                                                        complete_name=taxon["taxon_name"].lower().capitalize())

            if taxonunit[1]:
                taxonunit[0].save()
                create_hierarchystring(taxonunit[0])
            
        
        return HttpResponseRedirect('/admin')
    except:
        return HttpResponseRedirect('/')

def view_reference(request):
    refs = Reference.objects.all().filter(visible=1)
    paginator = Paginator(refs, 10)
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
              'filtered_refs': response,
              'nresults': nresults,
              'paginator': paginator})
    return render(request, 'front/search.html', c)


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
    return render(request, 'front/add_reference.html', c)

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
                return HttpResponseRedirect(f'/front/add_reference/{ref.pk}')
            except Reference.DoesNotExist:
                ref = None
        else:
            ref = get_object_or_404(Reference, pk=pk)
        ref = get_ref_from_doi(doi, ref)
        form = RefForm(instance=Reference)
        c = {'form': form, 'pk': pk if pk else ''}
        return render(request, 'front/add_reference.html', c)
    raise Http404

#TEMPORARILY SHOWS ONLY THE FIRST 20 SEARCH RESULTS BECAUSE PAGINATOR NOT FULLY IMPLEMENTED
def view_taxa(request):
    # Get all the taxa
    taxa_all = TaxonomicUnit.objects.all()
    # Set up Pagination, 20 taxa per page
    paginator = Paginator(taxa_all, 20)
    # Track current page
    page_number = request.GET.get('page')
    taxa = paginator.get_page(page_number)

    # Set up filter
    taxon_filter = TaxonFilter(request.GET, queryset=taxa_all)
    filtered_taxa = taxon_filter.qs[:20]
    # Total amount of results
    nresults = filtered_taxa.count()

    context = {'taxa': filtered_taxa,
     'page_number': page_number, 
     'filter': taxon_filter,
     'nresults': nresults}
    return render(request, 'front/taxa.html', context)

#TEMPORARILY SHOWS ONLY THE FIRST 20 SEARCH RESULTS BECAUSE PAGINATOR NOT FULLY IMPLEMENTED
def search_taxa(request):
    # Get all the taxa
    taxa_all = TaxonomicUnit.objects.all()
    # Set up filter
    taxon_filter = TaxonFilter(request.GET, queryset=taxa_all)
    # Total amount of results
    nresults = taxon_filter.qs.count()
    # Sort by pk
    filtered_qs = sorted(taxon_filter.qs, key=lambda objects: objects.pk)
    # Set up Pagination, 20 taxa per page
    paginator = Paginator(filtered_qs, 20)


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

    context.update({'filter': taxon_filter,
              'filtered_taxa': response,
              'nresults': nresults,
              'paginator': paginator})
    return render(request, 'front/taxa-search.html', context)

def view_hierarchy(request, parent_id=None):
    chosenTaxon = TaxonomicUnit.objects.get(taxon_id=parent_id)
    hierarchyObject = Hierarchy.objects.get(taxon=chosenTaxon)

    hierarchy = hierarchyObject.hierarchy_string.split('-')

    hierarchies = []
    references = []

    while (len(hierarchy) != 0):
        index = hierarchy.pop(0)
        root = TaxonomicUnit.objects.get(taxon_id=index)
        if (len(hierarchy) == 0):
            # This takes only the reference for the selected taxon. 
            # E.G. User chooses Deuterostomia -> this takes the refenences for deuterostomia and not for the parent taxons
            references.append(root.references.all())
        # if root.references.all():
        #     references.append(root.references.all())
        hierarchies.append(root)

    context = {'hierarchies': hierarchies, 'references': references[0]}
    return render(request, 'front/hierarchy.html', context)

def view_authors(request):
    authors = TaxonAuthorLkp.objects.all()
    paginator = Paginator(authors, 10)
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

                geos = form.cleaned_data['geographic_div']
                for geo in geos:
                    new_author.geographic_div.add(geo)
            except TaxonAuthorLkp.DoesNotExist:
                print("saving new author did not workout; do something")
            return HttpResponseRedirect('/add_author')
    else:
        form = AuthorForm()
    return render(request, 'front/add_author.html', {'form': form})