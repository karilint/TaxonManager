from django.urls import path, re_path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

from . import views # pylint:disable=E0401

app_name='front'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('references/', views.view_reference, name='references'),
    path('search/', views.search, name='search'),
    re_path(r'^add-references/(?:(?P<pk>\d+))?$', views.refs_add, name='add-references'),
    re_path(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    re_path(r'^resolve/(?:(?P<pk>\d+))?$', views.resolve, name='resolve'),
    re_path(r'^add-taxon/(?:(?P<pk>\d+))?$', views.taxon_add, name ='add-taxon'),
    # path('addName/<int:pk>', views.load_taxonomicUnitTypes, name ='addName_changelist'),
    path('taxa/', views.view_taxa, name='taxa'),
    path('taxa-search/', views.search_taxa, name='taxa-search'),
    re_path(r'hierarchy/(?:(?P<parent_id>\d+))?$', views.view_hierarchy, name='hierarchy'),
    re_path(r'add_junior_synonym/(?:(?P<taxon_id>\d+))?$', views.add_junior_synonym, name='add_junior_synonym'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('load_rankOfTaxonToBeAdded/', views.load_rankOfTaxonToBeAdded, name='load_rankOfTaxonToBeAdded'),
    path('load_parentTaxon/', views.load_parentTaxon, name='load_parentTaxon'),
    path('import_data_from_excel/', views.import_data_from_excel, name='import_data_from_excel'),
    path('load_seniorSynonym/', views.load_seniorSynonym, name='load_seniorSynonym'),
    path('load_juniorSynonym/', views.load_juniorSynonym, name='load_juniorSynonym'),
    path('experts/', views.view_experts, name='view-experts'),
    path('add-expert/', views.add_expert, name='add-expert'),
    path('authors/', views.view_authors, name='view-authors'),
    path('add-author/', views.add_author, name='add-author'),
    path('error/<str:message>', views.error, name='error')
]

