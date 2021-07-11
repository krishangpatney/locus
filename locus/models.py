from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Geocode(models.Model):
    hash_code = models.CharField(max_length=8 ,default='')

class Track(models.Model):
    time_added = models.DateTimeField(auto_now_add=True)
    expiry_time = models.DateTimeField(default = datetime.now() + timedelta(hours=10))
    geohash_link = models.ForeignKey(Geocode, on_delete=models.CASCADE, default=None)
    track_title = models.CharField(max_length=100, default='')
    track_author = models.CharField(max_length=100, default='')
    track_url = models.URLField(default='')

    # This should be the queue
    class Meta:
        ordering = ('time_added', )