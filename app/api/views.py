from rest_framework import viewsets
from front import models
from api import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAdminUser


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAdminUser]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter]

    class Meta:
        abstract = True


class ReferenceViewSet(BaseViewSet):
    serializer_class = serializers.ReferenceSerializer
    queryset = models.Reference.objects.all()
    filter_fields = ['id', 'authors', 'title', 'journal',
                     'volume', 'page_start', 'page_end', 'doi', 'url', 'bibtex']
    search_fields = ['id', 'authors', 'title', 'journal',
                     'volume', 'page_start', 'page_end', 'doi', 'url', 'bibtex']
    ordering_fields = ['id', 'authors', 'title', 'journal',
                       'volume', 'doi', 'url']


class KingdomViewSet(BaseViewSet):
    serializer_class = serializers.KingdomSerializer
    queryset = models.Kingdom.objects.all()
    filter_fields = ['id', 'kingdom_name']
    search_fields = ['id', 'kingdom_name']
    ordering_fields = ['id', 'kingdom_name']


class TaxonUnitTypeViewSet(BaseViewSet):
    serializer_class = serializers.TaxonUnitTypeSerializer
    queryset = models.TaxonUnitType.objects.all()
    filter_fields = ['id', 'kingdom', 'rank_id', 'rank_name',
                     'dir_parent_rank_id', 'req_parent_rank_id']
    search_fields = ['id', 'kingdom__kingdom_name', 'rank_id', 'rank_name',
                     'dir_parent_rank_id', 'req_parent_rank_id']
    ordering_fields = ['id', 'kingdom__kingdom_name', 'rank_id', 'rank_name',
                       'dir_parent_rank_id', 'req_parent_rank_id']


class GeoGraphicDivViewSet(BaseViewSet):
    serializer_class = serializers.GeoGraphicDivSerializer
    queryset = models.GeographicDiv.objects.all()
    filter_fields = ['id', 'geographic_value']
    search_fields = ['id', 'geographic_value']
    ordering_fields = ['id', 'geographic_value']


class TaxonAuthorLkpViewSet(BaseViewSet):
    serializer_class = serializers.TaxonAuthorLkpSerializer
    queryset = models.TaxonAuthorLkp.objects.all()
    filter_fields = ['taxon_author_id', 'taxon_author', 'kingdom']
    search_fields = ['taxon_author_id',
                     'taxon_author', 'kingdom__kingdom_name']
    ordering_fields = ['taxon_author_id',
                       'taxon_author', 'kingdom__kingdom_name']


class ExpertViewSet(BaseViewSet):
    serializer_class = serializers.ExpertSerializer
    queryset = models.Expert.objects.all()
    filter_fields = ['id', 'expert', 'geographic_div']
    search_fields = ['id', 'expert', 'geographic_div__geographic_value']
    ordering_fields = ['id', 'expert', 'geographic_div__geographic_value']


class TaxonomicUnitViewSet(BaseViewSet):
    serializer_class = serializers.TaxonomicUnitSerializer
    queryset = models.TaxonomicUnit.objects.all()
    filter_fields = ['taxon_id', 'unit_name1', 'unit_name2',
                     'unit_name3', 'unit_name4', 'kingdom',
                     'rank', 'complete_name', 'expert',
                     'taxon_author', 'geographic_div']
    search_fields = ['taxon_id', 'unit_name1', 'unit_name2',
                     'unit_name3', 'unit_name4', 'kingdom__kingdom_name',
                     'rank__rank_name', 'complete_name', 'expert__expert',
                     'taxon_author__taxon_author', 'geographic_div__geographic_value']
    ordering_fields = ['taxon_id', 'unit_name1', 'unit_name2',
                       'unit_name3', 'kingdom__kingdom_name',
                       'rank__rank_name', 'complete_name', 'expert__expert',
                       'taxon_author__taxon_author', 'geographic_div__geographic_value']


class HierarchyViewSet(BaseViewSet):
    serializer_class = serializers.HiearchySerializer
    queryset = models.Hierarchy.objects.all()
    filter_fields = ['id', 'hierarchy_string', 'taxon', 'parent_id', 'level']
    search_fields = ['id', 'hierarchy_string',
                     'taxonomicunit__taxon_id', 'parent_id', 'level']
    ordering_fields = ['id', 'hierarchy_string',
                       'taxonomicunit__taxon_id', 'parent_id', 'level']


class SynonymLinkViewSet(BaseViewSet):
    serializer_class = serializers.SynonymLinkSerializer
    queryset = models.SynonymLink.objects.all()
    filter_fields = ['id', 'synonym_id', 'taxon_id_accepted']
    search_fields = ['id', 'synonym_id', 'taxonomicunit__taxon_id']
    ordering_fields = ['id', 'synonym_id', 'taxonomicunit__taxon_id']
