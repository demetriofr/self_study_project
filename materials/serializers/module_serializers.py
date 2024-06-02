from rest_framework import serializers

from ..models import Module
from ..validators.module_validators import (
    ModuleCreationAboveTenValidator
)


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Module."""

    class Meta:
        model = Module
        fields = '__all__'
        extra_kwargs = {'moderator': {'read_only': True}}  # Запрет редактирования модератора
        validators = [
            ModuleCreationAboveTenValidator(),
        ]
