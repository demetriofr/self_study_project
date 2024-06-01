from rest_framework import serializers

from .models import SOUTCard
from .validators import SOUTCardCreationDateValidator


class SOUTCardSerializer(serializers.ModelSerializer):
    """Сериализатор для модели SOUTCard."""

    class Meta:
        model = SOUTCard
        fields = '__all__'
        extra_kwargs = {'admin': {'read_only': True}}  # Запрет редактирования администратор
        validators = [SOUTCardCreationDateValidator()]
