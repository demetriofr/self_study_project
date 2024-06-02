from rest_framework import serializers

from ..models import Topic
from ..validators.topic_validators import (
    TopicCreationAboveThirteenValidator,
    TopicExecutionTimeBetweenFiveAndSixtyMinutesValidator
)


class TopicSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Topic."""

    class Meta:
        model = Topic
        fields = '__all__'
        extra_kwargs = {'moderator': {'read_only': True}}  # Запрет редактирования модератора
        validators = [
            TopicCreationAboveThirteenValidator(),
            TopicExecutionTimeBetweenFiveAndSixtyMinutesValidator()
        ]
