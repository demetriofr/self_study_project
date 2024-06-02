from rest_framework.validators import ValidationError
from datetime import datetime


class SOUTCardCreationDateValidator:
    """Проверяет чтобы дата составления карты СОУТ не была больше даты занесения в базу."""

    def __call__(self, data):
        date_of_card_creation = data.get('date_of_card_creation')
        if date_of_card_creation > datetime.now().date():
            raise ValidationError('Дата составления карты СОУТ не должна быть больше даты занесения карты.')
