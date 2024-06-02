from django.core.validators import ValidationError


class TopicCreationAboveThirteenValidator:
    """Проверяет чтобы количество допматериала было между 0 и 13."""

    def __call__(self, data):
        addition_materials = data.get('addition_materials')
        if addition_materials is not None and len(addition_materials) > 13:
            raise ValidationError('Количество допматериала не должно быть больше 13.')


class TopicExecutionTimeBetweenFiveAndSixtyMinutesValidator:
    """Проверяет чтобы время выполнения было между 5 и 60 минутами."""

    def __call__(self, data):
        execution_time = data.get('execution_time')
        if not (5 <= execution_time <= 60):
            raise ValidationError('Количество минут для прохождения темы не должно быть меньше 5 и больше 60 минут.')
