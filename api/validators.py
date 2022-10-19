from rest_framework.validators import ValidationError


def length_validator(length: int):
    if not 5 <= length <= 1000:
        raise ValidationError('5 <= length <= 1000')
