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
    kingdom = serializers.SlugRelatedField(
        queryset=models.Kingdom.objects.all(), slug_field='kingdom_name')

    class Meta:
        model = models.TaxonUnitType
        fields = ['id', 'kingdom', 'rank_id', 'rank_name',
                  'dir_parent_rank_id', 'req_parent_rank_id']


class GeoGraphicDivSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeographicDiv
        fields = ['id', 'geographic_value']


class TaxonAuthorLkpSerializer(serializers.ModelSerializer):
    kingdom = serializers.SlugRelatedField(
        queryset=models.Kingdom.objects.all(), slug_field='kingdom_name')

    class Meta:
        model = models.TaxonAuthorLkp
        fields = ['taxon_author_id', 'taxon_author', 'kingdom']


class ExpertSerializer(serializers.ModelSerializer):
    geographic_div = serializers.SlugRelatedField(
        many=True, queryset=models.GeographicDiv.objects.all(), slug_field='geographic_value')

    class Meta:
        model = models.Expert
        fields = ['id', 'expert', 'geographic_div']


class TaxonomicUnitSerializer(serializers.ModelSerializer):
    kingdom = serializers.SlugRelatedField(
        queryset=models.Kingdom.objects.all(), slug_field='kingdom_name')
    taxon_author = serializers.SlugRelatedField(
        queryset=models.TaxonAuthorLkp.objects.all(), slug_field='taxon_author')
    rank = serializers.SlugRelatedField(
        queryset=models.TaxonUnitType.objects.all(), slug_field='rank_name')
    geographic_div = serializers.SlugRelatedField(
        many=True, queryset=models.GeographicDiv.objects.all(), slug_field='geographic_value')
    expert = serializers.SlugRelatedField(
        many=True, queryset=models.Expert.objects.all(), slug_field='expert')
    references = serializers.SlugRelatedField(
        many=True, queryset=models.Reference.objects.all(), slug_field='title')

    class Meta:
        model = models.TaxonomicUnit
        fields = ['taxon_id', 'unit_name1', 'unit_name2', 'unit_name3', 'unit_name4', 'parent_id',
                  'taxon_author', 'kingdom', 'rank', 'complete_name', 'references', 'geographic_div', 'expert']

    def create(self, validated_data):
        taxon = super().create(validated_data)
        views.create_hierarchystring(taxon)
        return taxon


class HiearchySerializer(serializers.ModelSerializer):
    taxon = serializers.SlugRelatedField(
        queryset=models.TaxonomicUnit.objects.all(), slug_field='complete_name')

    class Meta:
        model = models.Hierarchy
        fields = ['id', 'hierarchy_string', 'taxon', 'parent_id', 'level']


class SynonymLinkSerializer(serializers.ModelSerializer):

    taxon_id_accepted = serializers.SlugRelatedField(
        queryset=models.TaxonomicUnit.objects.all(), slug_field='complete_name')

    class Meta:
        model = models.SynonymLink
        fields = ['id', 'synonym_id', 'taxon_id_accepted']


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Comment
#         fields = ['id', 'commentator', 'comment_detail']
