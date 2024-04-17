from django.core.exceptions import ValidationError


def validate_name_starts_with_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")