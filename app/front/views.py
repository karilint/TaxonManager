from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from refs.models import Ref
from refs.forms import RefForm

from django import forms

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import user_passes_test
from refs.models import Ref, get_ref_from_doi
from .utils import canonicalize_doi
from refs.forms import RefForm
from refs.filters import RefFilter
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference
def login(request):
    return render(request, 'front/login.html')

def view_reference(request):
    refs = Ref.objects.all()
    paginator = Paginator(refs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    c = {'page_obj': page_obj, 'paginator': paginator}
    return render(request, 'front/references.html', c)

def search(request):
    ref_list = Ref.objects.all()
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
            ref = Ref.objects.get(pk=pk)
        form = RefForm(request.POST, instance=ref)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        try:
            ref = Ref.objects.get(pk=pk)
        except Ref.DoesNotExist:
            ref = None
        form = RefForm(instance=ref)

    c['form'] = form
    return render(request, 'front/add_reference.html', c)

#@user_passes_test(user_can_edit)
def delete(request, pk):
    ref = get_object_or_404(Ref, pk=pk)
    ref.delete()
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
                ref = Ref.objects.get(doi=doi)
                return HttpResponseRedirect(f'/front/add_reference/{ref.pk}')
            except Ref.DoesNotExist:
                ref = None
        else:
            ref = get_object_or_404(Ref, pk=pk)
        ref = get_ref_from_doi(doi, ref)
        form = RefForm(instance=ref)
        c = {'form': form, 'pk': pk if pk else ''}
        return render(request, 'front/add_reference.html', c)
    raise Http404