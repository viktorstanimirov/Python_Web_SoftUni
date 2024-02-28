from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profiles.models import Profile


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_NAME_LENGTH = 30
    MIN_PRICE = 0.0

    GENRE_CHOICES = [
        ("POP", "Pop Music"),
        ("JAZZ", "Jazz Music"),
        ("R_AND_B", "R&B Music",),
        ("ROCK", "Rock Music"),
        ("COUNTRY", "Country Music"),
        ("DANCE", "Dance Music"),
        ("HIP_HOP", "Hip Hop Music"),
        ("OTHER", "Other"),
    ]

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_NAME_LENGTH,
        blank=False,
        null=False,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

