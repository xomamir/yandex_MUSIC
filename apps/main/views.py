from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from main.models import Genre,Band,Artist,Album,Song
from main.serializers import (
    GenreSerializer,
    GenreCreateSerializer,
    BandSerializer,
    BandCreateSerializer,
    ArtistSerializer,
    ArtistCreateSerializer,
    AlbumSerializer,
    AlbumCreateSerializer,
    SongSerializer,
    SongCreateSerializer)
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
        serializer: GenreSerializer = GenreSerializer(
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
            genre = self.queryset.get(id=pk)
        except Genre.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = GenreSerializer(instance=genre)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = GenreCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song: Genre = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Genre {Genre.title} is create! Id: {song.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Удаление игры."""

        try:
            genre = self.queryset.get(id=pk)
        except Genre.DoesNotExist:
            raise ValidationError('Такой Игры нет', code=400)
        else:
            name: str = genre.title
            genre.delete()

        return Response(
            data={
                'status': 'OK',
                'message': f'Genre {name} is deleted!'
            }
        )
    

    def update(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Обновление игры."""

        try:
            genre = self.queryset.get(id=pk)
        except Genre.DoesNotExist:
            raise ValidationError('Genre not found', code=400)

        serializer: GenreSerializer = \
            GenreSerializer(
                instance=genre,
                data=request.data
            )
        if not serializer.is_valid():
            return Response(
                data={
                    'status': 'Warning',
                    'message': f'Warning with: {genre.title}'
                }
            )
        serializer.save()
        return Response(
            data={
                'status': 'OK',
                'message': f'Genre: {genre.title} was updated'
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
    

class AlbumViewSet(viewsets.ViewSet):
    """ViewSet for Game model."""

    queryset = Album.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: AlbumSerializer = AlbumSerializer(
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
            album = self.queryset.get(pk=pk)
        except Album.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = AlbumSerializer(instance=album)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = AlbumCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        album: Album = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Album {Album.title} is create! Id: {album.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Удаление игры."""

        try:
            album = self.queryset.get(id=pk)
        except Album.DoesNotExist:
            raise ValidationError('Такой Игры нет', code=400)
        else:
            name: str = album.title
            album.delete()

        return Response(
            data={
                'status': 'OK',
                'message': f'Album {name} is deleted!'
            }
        )
    

    def update(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Обновление игры."""

        try:
            album = self.queryset.get(id=pk)
        except Album.DoesNotExist:
            raise ValidationError('Game not found', code=400)

        serializer: AlbumSerializer = \
            AlbumSerializer(
                instance=album,
                data=request.data
            )
        if not serializer.is_valid():
            return Response(
                data={
                    'status': 'Warning',
                    'message': f'Warning with: {album.title}'
                }
            )
        serializer.save()
        return Response(
            data={
                'status': 'OK',
                'message': f'Album: {album.title} was updated'
            }
        )
    

class SongViewSet(viewsets.ViewSet):
    """ViewSet for Game model."""

    queryset = Song.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: SongSerializer = SongSerializer(
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
            song = self.queryset.get(id=pk)
        except Song.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = SongSerializer(instance=song)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = SongCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song: Song = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Song {Song.title} is create! Id: {song.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Удаление игры."""

        try:
            song = self.queryset.get(id=pk)
        except Song.DoesNotExist:
            raise ValidationError('Такой Игры нет', code=400)
        else:
            name: str = song.title
            song.delete()

        return Response(
            data={
                'status': 'OK',
                'message': f'Song {name} is deleted!'
            }
        )
    

    def update(
        self,
        request: Request,
        pk: str
    ) -> Response:
        """Обновление игры."""

        try:
            song = self.queryset.get(id=pk)
        except Song.DoesNotExist:
            raise ValidationError('Song not found', code=400)

        serializer: SongSerializer = \
            SongSerializer(
                instance=song,
                data=request.data
            )
        if not serializer.is_valid():
            return Response(
                data={
                    'status': 'Warning',
                    'message': f'Warning with: {song.title}'
                }
            )
        serializer.save()
        return Response(
            data={
                'status': 'OK',
                'message': f'Song: {song.title} was updated'
            }
        )