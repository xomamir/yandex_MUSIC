from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from main.models import Genre
from main.serializers import GenreSerializer,GenreCreateSerializer
from rest_framework.validators import ValidationError

class GenreViewSet(viewsets.ViewSet):


    queryset = Genre.objects.all()

    def list(
            self,
            request: Request,
            *args: tuple,
            **kwargs: dict
    ) -> Response:
        serializer = GenreSerializer(
            instance=self.queryset, many= True
        )
        return Response(
            data=serializer.data
        )
        
    def retrieve(
            self,
            request: Request,
            pk: int = None
    ) -> Response:
        try:
            genre = self.queryset.get(pk=pk)
        except Genre.DoesNotExist:
            raise ValidationError('Object not found', code = 404)
        serialazer = GenreSerializer(
            instance=genre
        )
        return Response(
            data=serialazer.data
        )
    
    def create(
            self,
            request: Request,
            *args: tuple,
            **kwargs: dict
    ) -> Response:

        serializer = GenreCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre: Genre = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': f'Genre{Genre.title} is create! Id:{genre.pk}'
            }
        )