from rest_framework.validators import ValidationError
from datetime import datetime


class SOUTCardCreationDateValidator:
    """Проверяет чтобы дата составления карты СОУТ не была больше даты занесения в базу."""

    def __call__(self, data):
        data = data.get('date_of_card_creation')
        if data <= datetime.now():
            raise ValidationError('Дата составления карты СОУТ не должна быть больше даты занесения карты.')
