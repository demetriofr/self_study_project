from individuals.models import Individual
from users.services import default_data_user_status_moderator


def default_data_individual():
    """Функция для создания данных физлица в используемого по умолчанию в случае их удаления."""
    return Individual.objects.create(
        moderator=default_data_user_status_moderator(),
        last_name='Дефолтов',
        first_name='Дефолт',
        middle_name='Дефолтович',
        data_of_birth='2000-01-01',
    )
