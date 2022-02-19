from django.urls import path, re_path

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
]
