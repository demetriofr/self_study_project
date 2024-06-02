import json
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from ..models import Module

# Определение базовой директории
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Определение путей к файлам с тестовыми данными
file_path_user = os.path.join(base_dir, 'data_for_tests', 'user.json')
file_path_workplace = os.path.join(base_dir, 'data_for_tests', 'materials', 'module.json')
file_path_reverse = os.path.join(base_dir, 'data_for_tests', 'reverse.json')

# Загрузка тестовых данных пользователя
with open(file_path_user) as f:
    test_data = json.load(f)
    data_test_user_admin_1 = test_data['data_test_user_admin_1']
    data_test_user_moderator_1 = test_data['data_test_user_moderator_1']
    data_test_user_student_1 = test_data['data_test_user_student_1']

# Загрузка тестовых данных приложения
with open(file_path_workplace) as f:
    test_data = json.load(f)
    data_test_module_1 = test_data['data_test_materials_Module_1']
    data_test_module_2 = test_data['data_test_materials_Module_2']
    data_test_module_3 = test_data['data_test_materials_Module_3']

    data_test_module__ModuleExecutionTimeBetweenFiveAndSixtyMinutesValidator_4 = test_data[
        'data_test_materials_Module_ModuleExecutionTimeBetweenFiveAndSixtyMinutesValidator_4'
    ]

# Загрузка пути для составления url
with open(file_path_reverse) as f:
    d_r = json.load(f)  # данные для reverse
    url_create = f'{d_r["APP"]["MA"]["name"]}:{d_r["APP"]["MA"]["Module"]}-{d_r['CRUD']['POST']}'
    url_get = f'{d_r["APP"]["MA"]["name"]}:{d_r["APP"]["MA"]["Module"]}-{d_r["CRUD"]["GET"]}'
    url_list = f'{d_r["APP"]["MA"]["name"]}:{d_r["APP"]["MA"]["Module"]}-{d_r["CRUD"]["LIST"]}'
    url_update = f'{d_r["APP"]["MA"]["name"]}:{d_r["APP"]["MA"]["Module"]}-{d_r["CRUD"]["PUT"]}'
    url_delete = f'{d_r["APP"]["MA"]["name"]}:{d_r["APP"]["MA"]["Module"]}-{d_r["CRUD"]["DELETE"]}'


def tear_down() -> None:
    """Очистить все таблицы, связанные с тестами."""

    Module.objects.all().delete()
    User.objects.all().delete()


class ModuleUserWithAdminAndAuthenticationTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении Modules пользователем со статуса админ
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

        # Создать экземпляры модели Module для тестов
        self.module_2 = Module.objects.create(
            moderator=self.user_admin_1,
            **data_test_module_2
        )
        self.module_3 = Module.objects.create(
            moderator=self.user_admin_1,
            **data_test_module_3
        )

    def test_create_module(self) -> None:
        """Тестирование создания Module."""

        # Создать экземпляр модели Module
        response = self.client.post(reverse(url_create), data=data_test_module_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверить существование объекта
        self.assertTrue(Module.objects.filter(
            title=data_test_module_1['title']).exists()
                        )

        # Проверить наличие данных в одном из обязательных полей
        self.assertEqual(
            response.json()['title'],
            data_test_module_1['title']
        )

    def test_create_module_with_validation_error(self) -> None:
        """Тестирование создания Module с ошибкой валидации."""

        # Попытка создать экземпляр модели Module с датой создания карты в будущем
        response = self.client.post(
            reverse(url_create),
            data=data_test_module__ModuleExecutionTimeBetweenFiveAndSixtyMinutesValidator_4
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_module(self):
        """Тестирование получения Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_get, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['title'], self.module_2.title)

    def test_list_module(self):
        """Тестирование получения списка Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(len(response.data['results']), 2)

        # Проверить есть ли указание на следующую страницу
        self.assertIsNone(response.data['next'])

    def test_update_module(self):
        """Тестирование обновления Module."""

        # Обновить экземпляр модели Module
        response = self.client.put(
            reverse(url_update, args=[self.module_2.id]),
            data=data_test_module_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверить данные
        self.assertEqual(response.data['title'], self.module_2.title)

    def test_delete_module(self):
        """Тестирование удаления Module."""

        # Удалить экземпляр модели Module
        response = self.client.delete(reverse(url_delete, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверить существование объекта
        self.assertFalse(Module.objects.filter(
            title=data_test_module_2['title']).exists()
        )

        # Проверить существование объекта
        self.assertTrue(Module.objects.filter(
            title=data_test_module_3['title']).exists()
        )


class ModuleUserWithoutAdminAndAuthenticationTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении Module пользователем без статуса админ
    с пройденной аутентификацией.
    """

    def setUp(self) -> None:
        """Создать тестовые данные."""

        # Очистить все таблицы, связанные с тестами
        tear_down()

        # Создать пользователей без статуса админ для тестов с пройденной аутентификаций
        self.user_moderator_1 = User.objects.create(
            username=data_test_user_moderator_1['username'],
            status_moderator=data_test_user_moderator_1['status_moderator'],
            status_student=data_test_user_moderator_1['status_student'],
        )
        self.user_moderator_1.set_password(data_test_user_moderator_1['password'])
        self.user_moderator_1.save()
        self.client.force_authenticate(user=self.user_moderator_1)

        # Создать экземпляры модели Module для тестов
        self.module_2 = Module.objects.create(
            moderator=self.user_moderator_1,
            **data_test_module_2
        )

    def test_create_module(self):
        """Тестирование создания Module пользователем со статусом админ."""

        response = self.client.post(reverse(url_create), data=data_test_module_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_module(self):
        """Тестирование получения Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_get, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_module(self):
        """Тестирование получения списка Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_module(self):
        """Тестирование обновления Module."""

        # Обновить экземпляр модели Module
        response = self.client.put(
            reverse(url_update, args=[self.module_2.id]),
            data=data_test_module_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_module(self):
        """Тестирование удаления Module."""

        # Удалить экземпляр модели Module
        response = self.client.delete(reverse(url_delete, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ModuleUserWithoutAdminAndModerationAndAuthenticationTestCase(APITestCase):
    """
    Тесты операций CRUD в приложении Module пользователем без статуса админ и модератора
    с пройденной аутентификацией.
    """

    def setUp(self) -> None:
        """Создать тестовые данные."""

        # Очистить все таблицы, связанные с тестами
        tear_down()

        # Создать пользователей без статуса админ для тестов с пройденной аутентификаций
        self.user_student_1 = User.objects.create(
            username=data_test_user_student_1['username'],
            status_moderator=data_test_user_student_1['status_moderator'],
            status_student=data_test_user_student_1['status_student'],
        )
        self.user_student_1.set_password(data_test_user_student_1['password'])
        self.user_student_1.save()
        self.client.force_authenticate(user=self.user_student_1)

        # Создать экземпляры модели Module для тестов
        self.module_2 = Module.objects.create(
            moderator=self.user_student_1,
            **data_test_module_2
        )

    def test_create_module(self):
        """Тестирование создания Module пользователем со статусом админ."""

        response = self.client.post(reverse(url_create), data=data_test_module_1)

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_module(self):
        """Тестирование получения Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_get, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_module(self):
        """Тестирование получения списка Module."""

        # Получить экземпляр модели Module
        response = self.client.get(reverse(url_list))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_module(self):
        """Тестирование обновления Module."""

        # Обновить экземпляр модели Module
        response = self.client.put(
            reverse(url_update, args=[self.module_2.id]),
            data=data_test_module_2
        )

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_module(self):
        """Тестирование удаления Module."""

        # Удалить экземпляр модели Module
        response = self.client.delete(reverse(url_delete, args=[self.module_2.id]))

        # Проверить статус запроса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
