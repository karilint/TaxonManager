from rest_framework import serializers
from front import models


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kingdom
        fields = ['id', 'kingdom_name']
