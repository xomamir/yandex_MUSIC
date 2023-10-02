from rest_framework import serializers
from main.models import Genre

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']

