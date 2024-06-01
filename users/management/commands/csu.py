from os import getenv
from dotenv import load_dotenv
from django.core.management import BaseCommand

from users.models import User


load_dotenv()


class Command(BaseCommand):
    """Создание суперпользователя (администратора)."""

    def handle(self, *args, **options):
        """Функция создания суперпользователя (администратора)."""

        # Создание суперпользователя
        csu = User.objects.create(
            username=getenv('CSU_USERNAME'),
            password=getenv('CSU_PASSWORD'),

            status_admin=True,
            status_moderator=True,
            status_student=False,

            is_staff=True,
            is_superuser=True,
        )

        # Setting the password for the superuser
        csu.set_password(getenv('CSU_PASSWORD'))

        csu.save()
