from rest_framework import serializers 
from locus.models import Track
 
 
class TrackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Track
        fields = ('id',
                  'track_title',
                  'track_author',
                  'track_url')
