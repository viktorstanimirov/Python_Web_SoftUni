from django.core.validators import MinLengthValidator
from django.db import models

from MyPlant_App.profiles.validators import validate_name_capital_letter


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(
                USERNAME_MIN_LENGTH
            )
        ]
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_name_capital_letter,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_name_capital_letter,
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
