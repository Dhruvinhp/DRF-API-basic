from django.shortcuts import render
from .serializers import SongSerialzer, SingerSerializer
from .models import Song, Singer
from rest_framework import viewsets, permissions

# Create your views here.
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = (permissions.IsAuthenticated,)

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerialzer
