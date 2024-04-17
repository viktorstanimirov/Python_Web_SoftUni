from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from TastyRecipesApp.profiles.models import Profile


def validate_unique_recipes_title(value):
    if Recipe.objects.filter(title=value).exists():
        raise ValidationError("We already have a recipe with the same title!")


class Recipe(models.Model):
    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]

    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 10
    CUISINE_MAX_LENGTH = 7

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_unique_recipes_title,
        ],
        unique=True,
        blank=False,
        null=False,
    )

    cuisine_type = models.CharField(
        max_length=CUISINE_MAX_LENGTH,
        choices=CUISINE_CHOICES,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=False,
        blank=False,
        help_text="Provide the cooking time in minutes."
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    # This field should remain hidden in forms and look for on_delete=models.CASCADE!!!
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
