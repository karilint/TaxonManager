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
    path('addName/', views.taxon_add, name ='addName'),
    # path('addName/<int:pk>', views.load_taxonomicUnitTypes, name ='addName_changelist'),
    path('taxa/', views.view_taxa, name='taxa'),
    path('taxa-search/', views.search_taxa, name='taxa-search'),
    re_path(r'hierarchy/(?:(?P<parent_id>\d+))?$', views.view_hierarchy, name='hierarchy'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('load_rankOfTaxonToBeAdded/', views.load_rankOfTaxonToBeAdded, name='load_rankOfTaxonToBeAdded'),
    path('load_parentTaxon/', views.load_parentTaxon, name='load_parentTaxon'),
    path('import_data_from_excel/', views.import_data_from_excel, name='import_data_from_excel')

]
