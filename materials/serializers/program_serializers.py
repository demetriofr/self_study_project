from rest_framework import serializers

from ..models import Program
from ..validators.program_validators import (
    ProgramCreationAboveTenValidator
)


class ProgramSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Program."""

    class Meta:
        model = Program
        fields = '__all__'
        extra_kwargs = {'moderator': {'read_only': True}}  # Запрет редактирования модератора
        validators = [
            ProgramCreationAboveTenValidator()
        ]
