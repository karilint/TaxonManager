from rest_framework import serializers
from front import models


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kingdom
        fields = ['id', 'kingdom_name']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    kingdom = serializers.HyperlinkedRelatedField(view_name='kingdom-detail', queryset=models.Kingdom.objects.all())

    class Meta:
        model = models.TaxonAuthorLkp
        fields = ['taxon_author_id', 'taxon_author', 'kingdom']
