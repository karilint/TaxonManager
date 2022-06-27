from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from front import models
from api import serializers


# @api_view(['GET'])
# def getData(request):
#     kingdoms = models.Kingdom.objects.all()
#     serializer = serializers.KingdomSerializer(kingdoms, many=True)
#     return Response(serializer.data)

class KingdomViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.KingdomSerializer
    queryset = models.Kingdom.objects.all()

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.TaxonAuthorLkp.objects.all()