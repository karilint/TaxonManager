from front.models import Reference, TaxonomicUnit, SynonymLink
from front.utils import canonicalize_doi
from django.db.models import Q
import django_filters
from django_filters import ModelChoiceFilter

class RefFilter(django_filters.FilterSet):

    doi = django_filters.CharFilter(field_name='doi', label='Publication DOI',
                    method='filter_by_doi')
    bibcode = django_filters.CharFilter(field_name='bibcode',
                    label='Publication Bibcode', lookup_expr='exact')
    title = django_filters.CharFilter(field_name='title', label='Title',
                    lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='authors', label='Author',
                    lookup_expr='icontains')

    def filter_by_doi(self, queryset, name, value):
        return queryset.filter(doi=canonicalize_doi(value))

    class Meta:
        model = Reference
        fields = []

class TaxonFilter(django_filters.FilterSet):

    unit_name1 = django_filters.CharFilter(field_name='unit_name1', label='Unit name 1',
                    lookup_expr='icontains')
    unit_name2 = django_filters.CharFilter(field_name='unit_name2', label='Unit name 2',
                    lookup_expr='icontains')
    unit_name3 = django_filters.CharFilter(field_name='unit_name3', label='Unit name 3',
                    lookup_expr='icontains')
    unit_name4 = django_filters.CharFilter(field_name='unit_name4', label='Unit name 4',
                    lookup_expr='icontains')
    kingdom = django_filters.CharFilter(field_name='kingdom__kingdom_name', label='Kingdom',
                    lookup_expr='icontains')
    rank_name = django_filters.CharFilter(field_name='rank__rank_name', label='Rank name',
                    lookup_expr='icontains')
    expert_name = django_filters.CharFilter(field_name='expert__expert', label='Expert',
                    lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='taxon_author__taxon_author', label='Author',
                    lookup_expr='icontains')
    geo_location = django_filters.CharFilter(field_name='geographic_div__geographic_value', label='Geographic location',
                    lookup_expr='icontains')
    any_field = django_filters.CharFilter(method='filter_by_any_field', label='Search', lookup_expr='icontains')
    synonyms = django_filters.CharFilter(method='filter_synonyms', label='Synonyms', lookup_expr='icontains')

    def filter_synonyms(self, queryset, name, value):
        taxons = TaxonomicUnit.objects.all()

        taxon = TaxonomicUnit.objects.filter(
            Q(unit_name1__icontains=value) |
            Q(unit_name2__icontains=value) |
            Q(unit_name3__icontains=value) |
            Q(unit_name4__icontains=value)
        )
        taxon_ids = [synonym.taxon_id for synonym in taxon]
        print(taxon_ids)
        senior_synonyms = SynonymLink.objects.filter(taxon_id_accepted__in=taxon_ids).only("taxon_id_accepted")
        junior_synonyms = SynonymLink.objects.filter(synonym_id__in=taxon_ids).only("synonym_id")
        seniors_of_juniors = SynonymLink.objects.filter(synonym_id__in=taxon_ids).only("taxon_id_accepted")
        
        print("Junior synonyms: ", junior_synonyms)
        print("Senior synonyms: ", seniors_of_juniors)
        search_results0 = TaxonomicUnit.objects.filter(taxon_id__in=seniors_of_juniors)
        search_results1 = TaxonomicUnit.objects.filter(taxon_id__in=junior_synonyms)
        search_results = search_results0 | search_results1
        return search_results

    def filter_by_any_field(self, queryset, name, value):
        return queryset.filter(
            Q(unit_name1__icontains=value) | Q(unit_name2__icontains=value) | Q(unit_name3__icontains=value) | Q(unit_name4__icontains=value)
            | Q(kingdom__kingdom_name__icontains=value) | Q(rank__rank_name__icontains=value)
            )

    class Meta:
        model = TaxonomicUnit
        fields = []
