from django.urls import path

from . import views # pylint:disable=E0401

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('references/', views.view_reference, name='references'),
    path('add_reference/', views.add_reference, name='add-references'),
    path('refs_add/', views.refs_add, name="add-references2"),
]
