from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from main.models import Genre,Band,Artist
from main.serializers import (
    GenreSerializer,
    GenreCreateSerializer,
    BandSerializer,
    BandCreateSerializer,
    ArtistSerializer,
    ArtistCreateSerializer)
from rest_framework.validators import ValidationError
from rest_framework import filters, generics


# class ProductList(generics.ListCreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (filters.SearchFilter,)
#     # filterset_fields =['price']
#     search_fields =['name']

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
            genre = self.queryset.get(id=pk)
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
    
class BandViewSet(viewsets.ViewSet):
    """ViewSet for Game model."""

    queryset = Band.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: BandSerializer = BandSerializer(
            instance=self.queryset, many=True
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
            band = self.queryset.get(id=pk)
        except Band.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = BandSerializer(instance=band)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = BandCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        band: Band = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Band {Band.title} is create! Id: {band.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Удаление игры."""

        try:
            band = self.queryset.get(id=pk)
        except Band.DoesNotExist:
            raise ValidationError('Такой Игры нет', code=400)
        else:
            name: str = band.title
            band.delete()

        return Response(
            data={
                'status': 'OK',
                'message': f'Band {name} is deleted!'
            }
        )
    

    def update(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Обновление игры."""

        try:
            band = self.queryset.get(id=pk)
        except Band.DoesNotExist:
            raise ValidationError('Game not found', code=400)

        serializer: BandSerializer = \
            BandSerializer(
                instance=band,
                data=request.data
            )
        if not serializer.is_valid():
            return Response(
                data={
                    'status': 'Warning',
                    'message': f'Warning with: {band.title}'
                }
            )
        serializer.save()
        return Response(
            data={
                'status': 'OK',
                'message': f'Band: {band.title} was updated'
            }
        )
    
class ArtistViewSet(viewsets.ViewSet):
    """ViewSet for Game model."""

    queryset = Artist.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: ArtistSerializer = ArtistSerializer(
            instance=self.queryset, many=True
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
            artist = self.queryset.get(id=pk)
        except Artist.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = ArtistSerializer(instance=artist)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = ArtistCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist: Artist = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Band {Artist.nickname} is create! Id: {artist.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Удаление игры."""

        try:
            artist = self.queryset.get(id=pk)
        except Band.DoesNotExist:
            raise ValidationError('Такой Игры нет', code=400)
        else:
            name: str = artist.nickname
            artist.delete()

        return Response(
            data={
                'status': 'OK',
                'message': f'Artist {name} is deleted!'
            }
        )
    

    def update(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Обновление игры."""

        try:
            artist = self.queryset.get(id=pk)
        except Band.DoesNotExist:
            raise ValidationError('Game not found', code=400)

        serializer: ArtistSerializer = \
            ArtistSerializer(
                instance=artist,
                data=request.data
            )
        if not serializer.is_valid():
            return Response(
                data={
                    'status': 'Warning',
                    'message': f'Warning with: {artist.nickname}'
                }
            )
        serializer.save()
        return Response(
            data={
                'status': 'OK',
                'message': f'Artist: {artist.title} was updated'
            }
        )