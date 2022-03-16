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
    print('test {}'.format(kingdomName))
    # taxonomicTypes = TaxonUnitType.objects.filter(kingdom=kingdomId)
    taxonomicUnits = TaxonomicUnit.objects.filter(kingdom=kingdomId)
    print('testes {}'.format(taxonomicUnits))
    return render(request, 'front/taxonomic_unit_types.html', {'taxonomicTypes': taxonomicUnits})

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
                
                # handle custom fields and db dependencies:
                # get parent id by parent's name + set it to be the new unit's parent
                parent =TaxonomicUnit.objects.get(unit_name1 = form.cleaned_data['parent_name'])                
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
                rank = TaxonUnitType.objects.get(rank_name = form.cleaned_data['rank_name'], kingdom = new_unit.kingdom)
                new_unit.rank_id = rank

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