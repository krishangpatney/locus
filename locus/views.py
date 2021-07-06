from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from geolib import geohash
from locus.models import Geocode, Track
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

# example -> /tracks/?geocode=thrrgc7g
@api_view(['GET'])
def tracks(request):
    if request.method == 'GET':
        geocode = request.GET.get('geocode', 'thrrgc7g')
        geocode_model = Geocode.objects.get(hash_code=geocode)
        linked_tracks = Track.objects.filter(geohash_link=geocode_model)
        track_list = serializers.serialize('json', linked_tracks)

    return Response(track_list, status=status.HTTP_200_OK)