from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_username,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
