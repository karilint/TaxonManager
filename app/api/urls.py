from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('references', views.ReferenceViewSet, basename='reference')

router.register('kingdoms', views.KingdomViewSet, basename='kingdom')
router.register('taxonunitypes', views.TaxonUnitTypeViewSet,
                basename='taxonunittype')
router.register('geographicdivs', views.GeoGraphicDivViewSet,
                basename='geographicdiv')
router.register('authors', views.TaxonAuthorLkpViewSet, basename='author')
router.register('experts', views.ExpertViewSet, basename='expert')

router.register('taxonomicunits', views.TaxonomicUnitViewSet,
                basename='taxonomicunit')
router.register('hierarchys', views.HierarchyViewSet,
                basename='hierarchy')
router.register('synonymlinks', views.SynonymLinkViewSet,
                basename='synonymlink')
# router.register('comments', views.CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls))]
