from users.models import User


def default_data_user_status_admin():
    """Функция для создания данных пользователя в роли администратора используемых по умолчанию в случае их удаления."""

    return User.objects.create_user(
        username='default_admin',
        password='default_admin',
        status_admin=True,
        status_student=False,
    )


def default_data_user_status_moderator():
    """Функция для создания данных пользователя в роли модератора используемых по умолчанию в случае их удаления."""

    return User.objects.create_user(
        username='default_moderator',
        password='default_moderator',
        status_moderator=True,
        status_student=False,
    )


def default_data_user_status_student():
    """Функция для создания данных пользователя в роли обучающегося используемых по умолчанию в случае их удаления."""

    return User.objects.create_user(
        username='default_student',
        password='default_student',
        status_student=True,
    )
