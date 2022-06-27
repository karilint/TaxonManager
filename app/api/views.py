from rest_framework import viewsets
from front import models
from api import serializers


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
