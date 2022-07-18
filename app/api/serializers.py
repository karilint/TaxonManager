from rest_framework import serializers
from front import models, views


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = ['id', 'authors', 'title', 'journal',
                  'volume', 'page_start', 'page_end', 'doi', 'url', 'bibtex']


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kingdom
        fields = ['id', 'kingdom_name']


class TaxonUnitTypeSerializer(serializers.ModelSerializer):
    kingdom = serializers.PrimaryKeyRelatedField(
        queryset=models.Kingdom.objects.all())

    class Meta:
        model = models.TaxonUnitType
        fields = ['id', 'kingdom', 'rank_id', 'rank_name',
                  'dir_parent_rank_id', 'req_parent_rank_id']


class GeoGraphicDivSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeographicDiv
        fields = ['id', 'geographic_value']


class TaxonAuthorLkpSerializer(serializers.ModelSerializer):
    kingdom = serializers.PrimaryKeyRelatedField(
        queryset=models.Kingdom.objects.all())

    class Meta:
        model = models.TaxonAuthorLkp
        fields = ['taxon_author_id', 'taxon_author', 'kingdom']


class ExpertSerializer(serializers.ModelSerializer):
    geographic_div = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.GeographicDiv.objects.all())

    class Meta:
        model = models.Expert
        fields = ['id', 'expert', 'geographic_div']


class TaxonomicUnitSerializer(serializers.ModelSerializer):
    kingdom = serializers.PrimaryKeyRelatedField(
        queryset=models.Kingdom.objects.all())
    taxon_author = serializers.PrimaryKeyRelatedField(
        queryset=models.TaxonAuthorLkp.objects.all())
    rank = serializers.PrimaryKeyRelatedField(
        queryset=models.TaxonUnitType.objects.all())
    geographic_div = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.GeographicDiv.objects.all())
    expert = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Expert.objects.all())
    reference = serializers.PrimaryKeyRelatedField(
        queryset=models.Reference.objects.all())

    class Meta:
        model = models.TaxonomicUnit
        fields = ['taxon_id', 'unit_name1', 'unit_name2', 'unit_name3', 'unit_name4', 'parent_id',
                  'taxon_author', 'kingdom', 'rank', 'complete_name', 'reference', 'geographic_div', 'expert']

    def create(self, validated_data):
        taxon = super().create(validated_data)
        views.create_hierarchystring(taxon)
        return taxon


class HiearchySerializer(serializers.ModelSerializer):
    taxon = serializers.PrimaryKeyRelatedField(
        queryset=models.TaxonomicUnit.objects.all())

    class Meta:
        model = models.Hierarchy
        fields = ['id', 'hierarchy_string', 'taxon', 'parent_id', 'level']


class SynonymLinkSerializer(serializers.ModelSerializer):

    taxon_id_accepted = serializers.PrimaryKeyRelatedField(
        queryset=models.TaxonomicUnit.objects.all())

    class Meta:
        model = models.SynonymLink
        fields = ['id', 'synonym_id', 'taxon_id_accepted']
