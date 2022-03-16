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
from .models import TaxonomicUnit, TaxonUnitType, Kingdom
from front.utils import canonicalize_doi
from front.forms import RefForm, NameForm
from front.filters import RefFilter
from django.contrib.auth.decorators import login_required
from .models import TaxonomicUnit




def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference
def login(request):
    return render(request, 'front/login.html')

def load_taxonomicUnitTypes(request):
    kingdomId = request.GET.get('id')
    

    kingdomName = Kingdom.objects.get(id=kingdomId)
    taxonLevels = TaxonUnitType.objects.filter(kingdom = kingdomName)
    # kingdom_taxons = kingdomName.taxonomicunit_set.all()
    # print('test {}'.format(kingdomName))
    # taxonomicTypes = TaxonUnitType.objects.filter(kingdom=kingdomId)
    rankTypes = TaxonomicUnit.objects.filter(kingdom=kingdomId)
    # print('testes {}'.format(taxonomicUnits[0].rank_id))
    # # test_unitType = TaxonUnitType.objects.get(id=taxonomicUnits[0].rank_id)
    # test_unitType = TaxonUnitType.objects.get(dir_parent_rank_id=kingdomId)
    # print('tulostus {}'.format(test_unitType))
    # # tulostus Kingdom: Animalia, rank_name: Phylum, rank_id:30

    # TaxonomicUnitsSearchedbyRank = TaxonomicUnit.objects.filter(rank = test_unitType)
    # print('tulostus2 {}'.format(TaxonomicUnitsSearchedbyRank))
    # # tulostus2 <QuerySet [<TaxonomicUnit: Myxozoa, Kingdom: Animalia (taxon_id: 1, parent_id: 10)>, <TaxonomicUnit: Chordata, Kingdom: Animalia (taxon_id: 2, parent_id: 10)>]>

    return render(request, 'front/rankTypes.html', {'rankTypes': taxonLevels})

def load_chosenTaxonLevel(request):
    taxonnomicTypeName = request.GET.get('id')
    kingdomId = request.GET.get('kingdomId')
    kingdom = Kingdom.objects.get(pk=kingdomId)

    taxonnomicType = TaxonUnitType.objects.get(rank_name=taxonnomicTypeName, kingdom=kingdom)
    # print("Taxonomic type: {}".format(taxonnomicType))
    # Taxonomic type: <QuerySet [<TaxonUnitType: Kingdom: Animalia, rank_name: Subkingdom, rank_id:20>]>
    taxontype = TaxonUnitType.objects.get(rank_id=taxonnomicType.rank_id, kingdom=taxonnomicType.kingdom)
    # print('taxontype {}'.format(taxontype.dir_parent_rank_id))
    prev_taxontype = TaxonUnitType.objects.get(rank_id=taxontype.dir_parent_rank_id, kingdom=taxonnomicType.kingdom)
    # print('prev_taxontype {}'.format(prev_taxontype))
    #

    # print(TaxonomicUnit.objects.filter(rank=taxontype.dir_parent_rank_id).filter(kingdom=kingdom))
    previous_taxonomic_unit = TaxonomicUnit.objects.filter(rank=prev_taxontype)
    

    # print('testii {}'.format(previous_taxonomic_unit))

    return render(request,  'front/chosenTaxonLevel.html', {'taxonLevels': previous_taxonomic_unit})


def taxon_add(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
                
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            try:
                # save names from Modelform, but don't admit new unit to db yet
                new_unit = form.save(commit=False)
                # taxonnomic_types dropdown = parent lisättävälle taxonille
                # rank_name = taso, jolla uusi taxon lisätään
                # unit_name1 etc = lisättävän tason nimet yms
                
                # parent: Animalia, Kingdom: Animalia (taxon_id: 5, parent_id: 0)
                # print(new_unit)
                rank_of_new_taxon = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['rank_name'])# new_unit.unit_name1)
                print('chosen_rank: {}'.format(rank_of_new_taxon))
                # chosen_rank: Bilateria, Kingdom: Animalia (taxon_id: 3, parent_id: 10)

                # Get the chosen kingdom
                kingdom = Kingdom.objects.get(kingdom_name=form.cleaned_data['kingdom_name'])
                # Get the taxon unit types related to a given kingdom.
                taxon_unit_types = TaxonUnitType.objects.filter(kingdom_id=kingdom.id)
                print('unit_types: {}'.format(taxon_unit_types))
                # unit_types: <QuerySet [<TaxonUnitType: Kingdom: Animalia, rank_name: Kingdom, rank_id:10>, <TaxonUnitType: Kingdom: Animalia, rank_name: Subkingdom, rank_id:20>, <TaxonUnitType: Kingdom: Animalia, rank_name: Infrakingdom, rank_id:25>, <TaxonUnitType: Kingdom: Animalia, rank_name: Superphylum, rank_id:27>, <TaxonUnitType: Kingdom: Animalia, rank_name: Phylum, rank_id:30>, <TaxonUnitType: Kingdom: Animalia, rank_name: Subphylum, rank_id:40>, <TaxonUnitType: Kingdom: Animalia, rank_name: Infraphylum, rank_id:45>, <TaxonUnitType: Kingdom: Animalia, rank_name: Superclass, rank_id:50>, <TaxonUnitType: Kingdom: Animalia, rank_name: Class, rank_id:60>, <TaxonUnitType: Kingdom: Animalia, rank_name: Subclass, rank_id:70>, <TaxonUnitType: Kingdom: Animalia, rank_name: Infraclass, rank_id:80>, <TaxonUnitType: Kingdom: Animalia, rank_name: Superorder, rank_id:90>, <TaxonUnitType: Kingdom: Animalia, rank_name: Order, rank_id:100>, <TaxonUnitType: Kingdom: Animalia, rank_name: Suborder, rank_id:110>, <TaxonUnitType: Kingdom: Animalia, rank_name: Infraorder, rank_id:120>, <TaxonUnitType: Kingdom: Animalia, rank_name: Section, rank_id:124>, <TaxonUnitType: Kingdom: Animalia, rank_name: Subsection, rank_id:126>, <TaxonUnitType: Kingdom: Animalia, rank_name: Superfamily, rank_id:130>, <TaxonUnitType: Kingdom: Animalia, rank_name: Family, rank_id:140>, <TaxonUnitType: Kingdom: Animalia, rank_name: Subfamily, rank_id:150>, '...(remaining elements truncated)...']>

                # ??????
                # prev_taxon_unit = TaxonomicUnit.objects.filter(rank_id=)

                parent = TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['rank_name'])   
                print('parent: {}'.format(parent))

                # parent: Animalia, Kingdom: Animalia (taxon_id: 5, parent_id: 0)           
                new_unit.parent_id = parent.taxon_id

                # set new unit's kingdom based on parent's kingdom
                new_unit.kingdom = parent.kingdom
            
                #FIX: set author (can be something or null)
                # if it is something:
                # 1. set correct taxon_author_id for new unit by references(and handle publications vs. experts) or what?
                # do here: some db -queries
                # set author here: new_unit.taxon_author_id = SUITABLE FOUND taxon_author_id

                #else if there's no author:
                #get rank by kingdom name and rank name + set rank to new unit
                # rank = TaxonUnitType.objects.get(rank_name = form.cleaned_data['rank_name'], kingdom = new_unit.kingdom)
                new_unit.rank_id = rank_of_new_taxon.taxon_id

                hierarchy_string = str(parent.taxon_id) + str(rank_of_new_taxon.taxon_id)
                print('hierarkia: {}'.format(hierarchy_string))
                # hierarkia: 56

                #save new unit =name
                new_unit.save()
            except TaxonomicUnit.DoesNotExist:
                # form was filled incorrectly
                print("saving new unit did not workout; do something")

            return HttpResponseRedirect('/addName')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'front/add_name.html', {'form': form})


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

# @login_required
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

#@user_passes_test(user_can_edit)
def delete(request, pk):
    ref = get_object_or_404(Reference, pk=pk)
    ref.visible = 0
    ref.doi = ''
    ref.title = ref.title + ' (removed)'
    ref.save()
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


def view_taxons(request):
    taxons = TaxonomicUnit.objects.all()
    context = {'taxons': taxons}
    return render(request, 'front/taxons.html', context)

def view_hierarchy(request, parent_id=None):
    hierarchies = []
    try:
        root = TaxonomicUnit.objects.get(parent_id=parent_id)
        hierarchies.append(root)
        while (root.parent_id != 0):
            root = TaxonomicUnit.objects.get(taxon_id=root.parent_id)
            hierarchies.append(root)
        hierarchies.reverse()
    except:
        pass
    context = {'hierarchies': hierarchies}
    return render(request, 'front/hierarchy.html', context)