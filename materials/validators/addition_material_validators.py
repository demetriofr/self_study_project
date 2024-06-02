import requests

from django.core.validators import URLValidator
from rest_framework.exceptions import ValidationError


class AdditionMaterialCorrectURLValidator:
    """Проверяет корректность URL в модели AdditionMaterial."""

    def __call__(self, data):

        value = data.get('link')

        # Проверка корректности URL
        validator = URLValidator()
        try:
            validator(value)
        except ValidationError:
            raise ValidationError('Некорректный URL')

        # Дополнительная проверка доступности URL
        try:
            response = requests.get(value)
            if response.status_code != 200:
                raise ValidationError('URL недоступен')
        except requests.exceptions.RequestException:
            raise ValidationError('URL недоступен')
