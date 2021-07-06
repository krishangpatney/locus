from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from geolib import geohash

# Resolution default to use for geocoding
resolution = 8
# Create your views here.

# example -> /geocode/?lat=25.204849&long=55.270782
@api_view(['GET'])
def geocode(request):
    if request.method == 'GET':
        try:
            latitude = request.GET.get('lat', '')
            longitude = request.GET.get('long', '')
            encoded_hash = geohash.encode(latitude, longitude, resolution)
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND)

    # if not in db add in db ? 
    return Response(str(encoded_hash), status=status.HTTP_200_OK)