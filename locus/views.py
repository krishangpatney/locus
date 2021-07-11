from django.shortcuts import render
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    if request.method == 'GET':
        try:
            latitude = request.GET.get('lat', '')
            longitude = request.GET.get('long', '')
            encoded_hash = geohash.encode(latitude, longitude, resolution)
        except: 
            # no_response data  
            no_response ={  
                "status" : "fail",
                "data" : { "response" : "Geohash error" }
            }  

            return JsonResponse(no_response, safe=False)

    # response data  
    response ={  
        "status" : "success",
        "data" : { "response" : encoded_hash }
    }  

    return JsonResponse(response, safe=False)


# example -> /tracks/?geocode=thrrgc7g
@api_view(['GET'])
def tracks(request):
    if request.method == 'GET':
        geocode = request.GET.get('geocode', '')
        # If hashcode exists it finds tracks to reply with
        if Geocode.objects.filter(hash_code=geocode).count()!=0:
            geocode_model = Geocode.objects.get(hash_code=geocode)
            linked_tracks = Track.objects.filter(geohash_link=geocode_model)
            serialized_track_list = TrackSerializer(linked_tracks, many=True)
            return JsonResponse(serialized_track_list.data, safe=False)
       
    # no_response data  
    no_response ={  
        "status" : "fail",
        "data" : { "response" : "No Tracks Found" }
    }  
        
    return JsonResponse(no_response, safe=False)


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
