from rest_framework import serializers

from ..models import AdditionMaterial
from ..validators.addition_material_validators import AdditionMaterialCorrectURLValidator


class AdditionMaterialSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AdditionMaterial."""

    class Meta:
        model = AdditionMaterial
        fields = '__all__'
        extra_kwargs = {'moderator': {'read_only': True}}  # Запрет редактирования модератора
        validators = [
            AdditionMaterialCorrectURLValidator()
        ]
