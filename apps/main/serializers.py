from rest_framework import serializers
from main.models import Genre,Band,Artist,Album,Song

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



class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    band = BandSerializer()
    logo = serializers.FileField()

class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title','band','logo']




class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    album = AlbumSerializer()
    audio_file = serializers.FileField()
    duration = serializers.IntegerField()
    genre = GenreSerializer(many=True)
    is_favorite = serializers.BooleanField()


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title','album','audio_file','duration','genre','is_favorite']

