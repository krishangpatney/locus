from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from locus import views
from rest_framework import routers


urlpatterns = [
    path('geocode/', views.geocode),
    path('tracks/', views.tracks),
    path('addTrack/', views.add_track)
]

urlpatterns = format_suffix_patterns(urlpatterns)