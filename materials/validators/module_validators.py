from django.core.validators import ValidationError


class ModuleCreationAboveTenValidator:
    """Проверяет чтобы количество тем было между 0 и 10."""

    def __call__(self, data):
        list_topics = data.get('list_topics')
        if list_topics is not None and len(list_topics) > 10:
            raise ValidationError('Тем в модуле не должно быть больше 10.')
