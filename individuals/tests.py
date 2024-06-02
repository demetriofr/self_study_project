import json
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Individual


# Определение базовой директории
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Определение путей к файлам с тестовыми данными
file_path_user = os.path.join(base_dir, 'data_for_tests', 'user.json')
file_path_workplace = os.path.join(base_dir, 'data_for_tests', 'individuals.json')
file_path_reverse = os.path.join(base_dir, 'data_for_tests', 'reverse.json')

# Загрузка тестовых данных пользователя
with open(file_path_user) as f:
    test_data = json.load(f)
    data_test_user_admin_1 = test_data['data_test_user_admin_1']
    data_test_user_moderator_1 = test_data['data_test_user_moderator_1']

# Загрузка тестовых данных приложения
with open(file_path_workplace) as f:
    test_data = json.load(f)
    data_test_individuals_individual_1 = test_data['data_test_individuals_Individual_1']
    data_test_individuals_individual_2 = test_data['data_test_individuals_Individual_2']
    data_test_individuals_individual_3 = test_data['data_test_individuals_Individual_3']

    data_test_individuals_individual__is_public_of_moderators_4 = test_data[
        'data_test_individuals_Individual_is_public_of_moderators_4'
    ]
    
    data_test_individuals_individual__IndividualDataOfBirthValidator_5 = test_data[
        'data_test_individuals_Individual_IndividualDataOfBirthValidator_5'
    ]

# Загрузка пути для составления url
with open(file_path_reverse) as f:
    d_r = json.load(f)  # данные для reverse
    url_create = f'{d_r["APP"]["ID"]["name"]}:{d_r["APP"]["ID"]["Individual"]}-{d_r['CRUD']['POST']}'
    url_get = f'{d_r["APP"]["ID"]["name"]}:{d_r["APP"]["ID"]["Individual"]}-{d_r["CRUD"]["GET"]}'
    url_list = f'{d_r["APP"]["ID"]["name"]}:{d_r["APP"]["ID"]["Individual"]}-{d_r["CRUD"]["LIST"]}'
    url_update = f'{d_r["APP"]["ID"]["name"]}:{d_r["APP"]["ID"]["Individual"]}-{d_r["CRUD"]["PUT"]}'
    url_delete = f'{d_r["APP"]["ID"]["name"]}:{d_r["APP"]["ID"]["Individual"]}-{d_r["CRUD"]["DELETE"]}'


def tear_down() -> None:
    """Очистить все таблицы, связанные с тестами."""

    Individual.objects.all().delete()
    User.objects.all().delete()


class IndividualUserWithAdminAndAuthenticationTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении Individuals пользователем со статуса админ
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
            status_moderator=data_test_user_admin_1['status_moderator'],
            status_student=data_test_user_admin_1['status_student'],
        )
        self.user_admin_1.set_password(data_test_user_admin_1['password'])
        self.user_admin_1.save()
        self.client.force_authenticate(user=self.user_admin_1)

        # Создать экземпляры модели Individual для тестов
        self.individual_2 = Individual.objects.create(
            moderator=self.user_admin_1,
            **data_test_individuals_individual_2
        )
        self.individual_3 = Individual.objects.create(
            moderator=self.user_admin_1,
            **data_test_individuals_individual_3
        )

    def test_create_individual(self) -> None:
        """Тестирование создания Individual."""

        # Создать экземпляр модели Individual
        response = self.client.post(reverse(url_create), data=data_test_individuals_individual_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверить существование объекта
        self.assertTrue(Individual.objects.filter(
            last_name=data_test_individuals_individual_1['last_name']).exists()
        )

        # Проверить наличие данных в одном из обязательных полей
        self.assertEqual(
            response.json()['first_name'],
            data_test_individuals_individual_1['first_name']
        )

    def test_create_individual_with_validation_error(self) -> None:
        """Тестирование создания Individual с ошибкой валидации."""

        # Попытка создать экземпляр модели Individual с датой создания карты в будущем
        response = self.client.post(
            reverse(url_create),
            data=data_test_individuals_individual__IndividualDataOfBirthValidator_5
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_individual(self):
        """Тестирование получения Individual."""

        # Получить экземпляр модели Individual
        response = self.client.get(reverse(url_get, args=[self.individual_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['last_name'], self.individual_2.last_name)

    def test_list_individual(self):
        """Тестирование получения списка Individual."""

        # Получить экземпляр модели Individual
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(len(response.data['results']), 2)

        # Проверить есть ли указание на следующую страницу
        self.assertIsNone(response.data['next'])

    def test_update_individual(self):
        """"Тестирование обновления Individual."""

        # Обновить экземпляр модели Individual
        response = self.client.put(
            reverse(url_update, args=[self.individual_2.id]),
            data=data_test_individuals_individual_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['last_name'], self.individual_2.last_name)

    def test_delete_individual(self):
        """Тестирование удаления Individual."""

        # Удалить экземпляр модели Individual
        response = self.client.delete(reverse(url_delete, args=[self.individual_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверить существование объекта
        self.assertFalse(Individual.objects.filter(
            last_name=data_test_individuals_individual_2['last_name']).exists()
        )

        # Проверить существование объекта
        self.assertTrue(Individual.objects.filter(
            first_name=data_test_individuals_individual_3['first_name']).exists()
        )


class IndividualUserWithoutAdminTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении Individual пользователем без статуса админ
    с пройденной аутентификацией.
    """

    def setUp(self) -> None:
        """Создать тестовые данные."""

        # Очистить все таблицы, связанные с тестами
        tear_down()

        # Создать пользователей без статуса админ для тестов с пройденной аутентификаций
        self.user_moderator_1 = User.objects.create(
            username=data_test_user_moderator_1['username'],
            status_moderator=False,
            status_student=data_test_user_moderator_1['status_student'],
        )
        self.user_moderator_1.set_password(data_test_user_moderator_1['password'])
        self.user_moderator_1.save()
        self.client.force_authenticate(user=self.user_moderator_1)

        # Создать экземпляры модели Individual для тестов
        self.individual_2 = Individual.objects.create(
            moderator=self.user_moderator_1,
            **data_test_individuals_individual_2
        )

    def test_create_individual(self):
        """Тестирование создания Individual пользователем со статусом админ."""

        response = self.client.post(reverse(url_create), data=data_test_individuals_individual_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_individual(self):
        """Тестирование получения Individual."""

        # Получить экземпляр модели Individual
        response = self.client.get(reverse(url_get, args=[self.individual_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_individual(self):
        """Тестирование получения списка Individual."""

        # Получить экземпляр модели Individual
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_individual(self):
        """"Тестирование обновления Individual."""

        # Обновить экземпляр модели Individual
        response = self.client.put(
            reverse(url_update, args=[self.individual_2.id]),
            data=data_test_individuals_individual_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_individual(self):
        """Тестирование удаления Individual."""

        # Удалить экземпляр модели Individual
        response = self.client.delete(reverse(url_delete, args=[self.individual_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
