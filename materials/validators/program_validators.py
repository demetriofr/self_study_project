from django.core.validators import ValidationError


class ProgramCreationAboveTenValidator:
    """Проверяет чтобы количество тем было между 0 и 10."""

    def __call__(self, data):
        list_modules = data.get('list_modules')
        if list_modules is not None and len(list_modules) > 10:
            raise ValidationError('Тем в программе не должно быть больше 10.')
