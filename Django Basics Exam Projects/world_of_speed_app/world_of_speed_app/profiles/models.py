from django.core.validators import MinLengthValidator
from django.db import models

from world_of_speed_app.profiles.validators import validate_username, validate_age


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 15
    MAX_PASSWORD_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25
    MIN_AGE_VALUE = 21

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, message="Username must be at least 3 chars long!"),
            validate_username,
        ),
        unique=True,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_age,
        ),
        help_text=("Age requirement: 21 years and above."
                   ),
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None
