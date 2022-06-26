from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    taxon = {'name':'Homo Sapiens', 'author':'Darwin'}
    return Response(taxon)
