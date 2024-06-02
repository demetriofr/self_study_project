from rest_framework import serializers

from .models import Individual
from .validators import IndividualDataOfBirthValidator


class IndividualSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Individual."""

    class Meta:
        model = Individual
        fields = '__all__'
        extra_kwargs = {'moderator': {'read_only': True}}  # Запрет редактирования модератора
        validators = [
            IndividualDataOfBirthValidator(),
        ]
