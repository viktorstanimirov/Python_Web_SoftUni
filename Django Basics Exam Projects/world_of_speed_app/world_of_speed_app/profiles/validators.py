from django.core.exceptions import ValidationError


def validate_username(username):
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_age(age):
    if age < 21:
        raise ValidationError("Age must be 21 or above!")