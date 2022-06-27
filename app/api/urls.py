from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views



router = DefaultRouter()
router.register('kingdoms', views.KingdomViewSet, basename='kingdom')
router.register('authors', views.AuthorViewSet, basename='authors_urls')

urlpatterns = [
    path('', include(router.urls))]
