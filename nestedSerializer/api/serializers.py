from rest_framework import serializers
from .models import Song, Singer

class SongSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerialzer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sungby']
