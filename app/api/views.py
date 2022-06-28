from rest_framework import viewsets
from front import models
from api import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# settings.py :    'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ]


class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReferenceSerializer
    queryset = models.Reference.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class KingdomViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.KingdomSerializer
    queryset = models.Kingdom.objects.all()


class TaxonUnitTypeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaxonUnitTypeSerializer
    queryset = models.TaxonUnitType.objects.all()


class GeoGraphicDivViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GeoGraphicDivSerializer
    queryset = models.GeographicDiv.objects.all()


class TaxonAuthorLkpViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaxonAuthorLkpSerializer
    queryset = models.TaxonAuthorLkp.objects.all()


class ExpertViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpertSerializer
    queryset = models.Expert.objects.all()


class TaxonomicUnitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaxonomicUnitSerializer
    queryset = models.TaxonomicUnit.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['taxon_id', 'unit_name1', 'unit_name2',
                     'unit_name3', 'unit_name4', 'kingdom',
                     'rank', 'complete_name', 'expert',
                     'taxon_author', 'geographic_div']
    search_fields = ['taxon_id', 'unit_name1', 'unit_name2',
                     'unit_name3', 'unit_name4', 'kingdom__kingdom_name',
                     'rank__rank_name', 'complete_name', 'expert__expert',
                     'taxon_author__taxon_author', 'geographic_div__geographic_value']


class HierarchyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HiearchySerializer
    queryset = models.Hierarchy.objects.all()


class SynonymLinkViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SynonymLinkSerializer
    queryset = models.SynonymLink.objects.all()
