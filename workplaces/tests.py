import json
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from workplaces.models import SOUTCard


# Определение базовой директории
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Определение путей к файлам с тестовыми данными
file_path_user = os.path.join(base_dir, 'data_for_tests', 'user.json')
file_path_workplace = os.path.join(base_dir, 'data_for_tests', 'workplaces.json')
file_path_reverse = os.path.join(base_dir, 'data_for_tests', 'reverse.json')

# Загрузка тестовых данных пользователя
with open(file_path_user) as f:
    test_data = json.load(f)
    data_test_user_admin_1 = test_data['data_test_user_admin_1']
    data_test_user_moderator_1 = test_data['data_test_user_moderator_1']

# Загрузка тестовых данных приложения
with open(file_path_workplace) as f:
    test_data = json.load(f)
    data_test_workplaces_soutcard_1 = test_data['data_test_workplaces_SOUTCard_1']
    data_test_workplaces_soutcard_2 = test_data['data_test_workplaces_SOUTCard_2']
    data_test_workplaces_soutcard_3 = test_data['data_test_workplaces_SOUTCard_3']

    data_test_workplaces_soutcard__soutcard_creation_date_validator_1 = test_data[
        'data_test_workplaces_SOUTCard_SOUTCardCreationDateValidator_1'
    ]

# Загрузка пути для составления url
with open(file_path_reverse) as f:
    d_r = json.load(f)  # данные для reverse
    url_create = f'{d_r["APP"]["WP"]["name"]}:{d_r["APP"]["WP"]["SOUTCard"]}-{d_r['CRUD']['POST']}'
    url_get = f'{d_r["APP"]["WP"]["name"]}:{d_r["APP"]["WP"]["SOUTCard"]}-{d_r["CRUD"]["GET"]}'
    url_list = f'{d_r["APP"]["WP"]["name"]}:{d_r["APP"]["WP"]["SOUTCard"]}-{d_r["CRUD"]["LIST"]}'
    url_update = f'{d_r["APP"]["WP"]["name"]}:{d_r["APP"]["WP"]["SOUTCard"]}-{d_r["CRUD"]["PUT"]}'
    url_delete = f'{d_r["APP"]["WP"]["name"]}:{d_r["APP"]["WP"]["SOUTCard"]}-{d_r["CRUD"]["DELETE"]}'


def tear_down() -> None:
    """Очистить все таблицы, связанные с тестами."""

    SOUTCard.objects.all().delete()
    User.objects.all().delete()


class SOUTCardUserWithAdminAndAuthenticationTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении SOUTCard пользователем со статуса админ
    с пройденной аутентификацией
    """

    def setUp(self) -> None:
        """Создать тестовые данные."""

        # Очистить все таблицы, связанные с тестами
        tear_down()

        # Создать пользователей для тестов со статусом админ с пройденной аутентификаций
        self.user_admin_1 = User.objects.create(
            username=data_test_user_admin_1['username'],
            status_admin=data_test_user_admin_1['status_admin'],
            status_student=data_test_user_admin_1['status_student'],
        )
        self.user_admin_1.set_password(data_test_user_admin_1['password'])
        self.user_admin_1.save()
        self.client.force_authenticate(user=self.user_admin_1)

        # Создать экземпляры модели SOUTCard для тестов
        self.soutcard_2 = SOUTCard.objects.create(
            admin=self.user_admin_1,
            **data_test_workplaces_soutcard_2
        )
        self.soutcard_3 = SOUTCard.objects.create(
            admin=self.user_admin_1,
            **data_test_workplaces_soutcard_3
        )

    def test_create_soutcard(self) -> None:
        """Тестирование создания SOUTCard."""

        # Создать экземпляр модели SOUTCard
        response = self.client.post(reverse(url_create), data=data_test_workplaces_soutcard_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверить существование объекта
        self.assertTrue(SOUTCard.objects.filter(
            sout_card_number=data_test_workplaces_soutcard_1['sout_card_number']).exists()
        )

        # Проверить наличие данных в одном из обязательных полей
        self.assertEqual(
            response.json()['date_of_card_creation'],
            data_test_workplaces_soutcard_1['date_of_card_creation']
        )

    def test_create_soutcard_with_validation_error(self) -> None:
        """Тестирование создания SOUTCard с ошибкой валидации."""

        # Попытка создать экземпляр модели SOUTCard с датой создания карты в будущем
        response = self.client.post(
            reverse(url_create),
            data=data_test_workplaces_soutcard__soutcard_creation_date_validator_1
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_soutcard(self):
        """Тестирование получения SOUTCard."""

        # Получить экземпляр модели SOUTCard
        response = self.client.get(reverse(url_get, args=[self.soutcard_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['sout_card_number'], self.soutcard_2.sout_card_number)

    def test_list_soutcard(self):
        """Тестирование получения списка SOUTCard."""

        # Получить экземпляр модели SOUTCard
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(len(response.data['results']), 2)

        # Проверить есть ли указание на следующую страницу
        self.assertIsNone(response.data['next'])

    def test_update_soutcard(self):
        """"Тестирование обновления SOUTCard."""

        # Обновить экземпляр модели SOUTCard
        response = self.client.put(
            reverse(url_update, args=[self.soutcard_2.id]),
            data=data_test_workplaces_soutcard_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['sout_card_number'], self.soutcard_2.sout_card_number)

    def test_delete_soutcard(self):
        """Тестирование удаления SOUTCard."""

        # Удалить экземпляр модели SOUTCard
        response = self.client.delete(reverse(url_delete, args=[self.soutcard_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверить существование объекта
        self.assertFalse(SOUTCard.objects.filter(
            sout_card_number=data_test_workplaces_soutcard_2['sout_card_number']).exists()
        )

        # Проверить существование объекта
        self.assertTrue(SOUTCard.objects.filter(
            sout_card_number=data_test_workplaces_soutcard_3['sout_card_number']).exists()
        )


class SOUTCardUserWithoutAdminTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении SOUTCard пользователем без статуса админ
    с пройденной аутентификацией.
    """

    def setUp(self) -> None:
        """Создать тестовые данные."""

        # Очистить все таблицы, связанные с тестами
        tear_down()

        # Создать пользователей без статуса админ для тестов с пройденной аутентификаций
        self.user_moderator_1 = User.objects.create(
            username=data_test_user_moderator_1['username'],
            status_admin=False,
            status_student=data_test_user_moderator_1['status_student'],
        )
        self.user_moderator_1.set_password(data_test_user_moderator_1['password'])
        self.user_moderator_1.save()
        self.client.force_authenticate(user=self.user_moderator_1)

        # Создать экземпляры модели SOUTCard для тестов
        self.soutcard_2 = SOUTCard.objects.create(
            admin=self.user_moderator_1,
            **data_test_workplaces_soutcard_2
        )

    def test_create_soutcard(self):
        """Тестирование создания SOUTCard пользователем со статусом админ."""

        response = self.client.post(reverse(url_create), data=data_test_workplaces_soutcard_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_soutcard(self):
        """Тестирование получения SOUTCard."""

        # Получить экземпляр модели SOUTCard
        response = self.client.get(reverse(url_get, args=[self.soutcard_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_soutcard(self):
        """Тестирование получения списка SOUTCard."""

        # Получить экземпляр модели SOUTCard
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_soutcard(self):
        """"Тестирование обновления SOUTCard."""

        # Обновить экземпляр модели SOUTCard
        response = self.client.put(
            reverse(url_update, args=[self.soutcard_2.id]),
            data=data_test_workplaces_soutcard_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_soutcard(self):
        """Тестирование удаления SOUTCard."""

        # Удалить экземпляр модели SOUTCard
        response = self.client.delete(reverse(url_delete, args=[self.soutcard_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
