from rest_framework import serializers
from main.models import Genre,Band,Artist

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']




class BandSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    country = serializers.CharField()

class BandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['title','country']



class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nickname = serializers.CharField()
    band = BandSerializer()

class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['nickname','band']

