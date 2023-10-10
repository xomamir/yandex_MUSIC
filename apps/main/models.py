# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.db import models

from abstracts.models import AbsctractDateTime
from abstracts.utils import normalize_time




class Band(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    country = models.CharField(
        verbose_name='страна',
        max_length=50

    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        if not self.title:
            return 'Без названия'
        return f'Группа: {self.title}'


class Artist(models.Model):
    """
    Artist model.
    """

    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа',
        null=True,
        blank=True
    )

    nickname = models.CharField(
        verbose_name='псевдоним',
        default='',
        max_length=50
    )


    class Meta:
        ordering = ('id',)
        verbose_name = 'музыкант'
        verbose_name_plural = 'музыканты'

    def __str__(self) -> str:
        if not self.nickname:
            return 'Без имени'

        return f'Музыкант: {self.nickname}'


class AlbumQuerySet(models.QuerySet):

    def not_deleted(self):
        return self.filter(is_deleted=False)


class AlbumManager(models.Manager):

    def get_queryset(self) -> models.query.QuerySet['Album']:
        return AlbumQuerySet(
            self.model,
            using=self._db
        )

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Album(models.Model):
    """
    Album model.
    """

    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа'
    )
    title = models.CharField(
        verbose_name='название альбома',
        max_length=150
    )

    logo = models.ImageField(
        verbose_name='логотип',
        upload_to='posters',
        null=True,
        blank=True
    )


    objects = AlbumManager()

    def __str__(self) -> str:
        return f'{self.band}: {self.title} '


    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'


class Genre(models.Model):
    """Genre model."""

    title = models.CharField(
        max_length=50,
        verbose_name='жанр'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        ordering = ('-id',) 


class Song(models.Model):
    """Song model."""

    title = models.CharField(
        verbose_name='название песни',
        max_length=50
    )
    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        verbose_name='альбом',
        related_name='songs'
    )
    audio_file = models.FileField(
        verbose_name='аудио файл',
        upload_to='songs/%Y/%m/%d/'
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name='длительность трека',
        default=False
    )
    genre = models.ManyToManyField(
        to=Genre,
        verbose_name='жанр'
    )

    is_favorite = models.BooleanField(
        verbose_name='избранное',
        default=False
    )


    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'
        ordering = ('id',)
