from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.core import serializers

from geolib import geohash

from locus.models import Geocode, Track
from locus.serializers import TrackSerializer

import json

# https://bezkoder.com/django-rest-api/#6_Configure_CORS_for_a_Rest_Api_Resource

# Resolution default to use for geocoding
resolution = 8
# Create your views here.

# example -> /geocode/?lat=25.204849&long=55.270782
@api_view(['GET'])
def geocode(request):
    """
    View to return the geocode of a user.
    """
    try:
        latitude = request.query_params.get('lat', '')
        longitude = request.query_params.get('long', '')
        encoded_hash = geohash.encode(latitude, longitude, resolution)
    except: 
        # no_response data  
        return Response(None, status.HTTP_400_BAD_REQUEST)

    # response data  
    return Response(encoded_hash, status.HTTP_200_OK)


# example -> /tracks/?geocode=thrrgc7g
@api_view(['GET'])
def tracks(request):
    if request.method == 'GET':
        geocode = request.query_params.get('geocode', '')
        # If hashcode exists it finds tracks to reply with
        if Geocode.objects.filter(hash_code=geocode).count()!=0:
            geocode_model = Geocode.objects.get(hash_code=geocode)
            linked_tracks = Track.objects.filter(geohash_link=geocode_model)
            serialized_track_list = TrackSerializer(linked_tracks, many=True)
            return Response(serialized_track_list.data, status.HTTP_200_OK)
               
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_track(request):
    # Create a new track with geocode location 
    # 1. Check if GEOCODE exists 
    # 2. If not create model for geocode
    # 3. Use link-logic and add data to a track, which is linked to geocode model
    # Ask for Geocode, track_url, (track_expiry_time)
    if request.method == 'POST':
        data = json.rearequest.data
        print(data)
    return Response(data, status=status.HTTP_200_OK)
