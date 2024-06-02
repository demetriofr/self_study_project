from rest_framework.validators import ValidationError

from config.services import comparison_of_dates


class IndividualDataOfBirthValidator:
    """
    Проверяет чтобы дата рождения была меньшей дате,
    полученной вычитанием 18 лет от даты занесения физлица.
    """

    def __call__(self, data):

        if not comparison_of_dates(data['data_of_birth']):
            raise ValidationError('Физическому лицу должно быть больше 18 лет.')
