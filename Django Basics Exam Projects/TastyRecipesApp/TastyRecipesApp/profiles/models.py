from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipesApp.profiles.validators import validate_name_starts_with_capital_letter


class Profile(models.Model):
    NICKNAME_MAX_LENGTH = 20
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    nickname = models.CharField(
        max_length=NICKNAME_MAX_LENGTH,
        unique=True,
        validators=[
            MinLengthValidator(
                2, "Nickname must be at least 2 chars long!"
            )
        ],
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_name_starts_with_capital_letter
        ],
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_name_starts_with_capital_letter
        ],
    )

    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    bio = models.TextField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"