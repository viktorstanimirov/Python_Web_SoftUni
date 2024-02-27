from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.cars.validators import validate_year
from world_of_speed_app.profiles.models import Profile


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 15
    MODEL_MIN_LENGTH = 1
    MIN_PRICE_VALUE = 1.0

    TYPE_CHOICES = (
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),

    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        null=False,
        blank=False,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MODEL_MIN_LENGTH),
        ),
    )

    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_year,
        ),
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        default="https://...",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one.",
        }
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE_VALUE, message="Price cannot be below 1.0."),
        )
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )



