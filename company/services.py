from .models import Worker
from individuals.services import default_data_individual
from users.services import default_data_user_status_moderator


def default_data_position():
    """Функция для создания данных должности используемых по умолчанию в случае их удаления."""

    return Worker.objects.create(
        moderator=default_data_user_status_moderator,
        name='Дефолтова',
    )


def default_data_worker():
    """Функция для создания данных работника используемых по умолчанию в случае их удаления."""

    return Worker.objects.create(
        moderator=default_data_user_status_moderator,
        individual=default_data_individual,
        position=default_data_position,
    )
