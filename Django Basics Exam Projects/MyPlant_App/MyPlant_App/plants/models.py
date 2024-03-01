from django.db import models

from MyPlant_App.profiles.validators import validate_plant_name


class Plant(models.Model):
    PLANT_TYPE_MAX_LENGTH = 14
    PLANT_NAME_MAX_LENGTH = 20

    PLANT_TYPE_CHOICES = [
        ("OUTDOOR", "Outdoor Plants"),
        ("INDOOR", "Indoor Plants"),
    ]

    plant_type = models.CharField(
        max_length=PLANT_TYPE_MAX_LENGTH,
        blank=False,
        null=False,
        choices=PLANT_TYPE_CHOICES,
    )

    name = models.CharField(
        max_length=PLANT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_plant_name,
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )