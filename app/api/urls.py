from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('get-data/', views.getData)]
