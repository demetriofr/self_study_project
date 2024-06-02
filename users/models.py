from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    """Модель для хранения данных о пользователе в роли обучающегося, модератора или администратора."""

    # Уникальный номер пользователя в статусе "Администратор" или "Модератора", который добавил пользователя,
    # модератора и обучающегося соответственно (добавляется уникальный номер активного пользователя).
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)

    # Имя пользователя для обучающегося создаётся автоматически из данных физлица (фамилия, инициалы, год рождения),
    # для администратора и модератора должен быть произвольное допустимое имя пользователя.
    username = models.CharField(max_length=150, unique=True, verbose_name='имя пользователя')

    # Пароль, создаётся автоматически из данных работника (табельный номер) и данных физлица (дата рождения),
    # для администратора и модератора должен быть произвольный допустимый пароль.
    password = models.CharField(max_length=128, verbose_name='пароль')

    data_worker = models.ForeignKey('company.Worker', on_delete=models.CASCADE,
                                    verbose_name='данные работника', **NULLABLE)

    status_admin = models.BooleanField(default=False, verbose_name='статус администратора')
    status_moderator = models.BooleanField(default=False, verbose_name='статус модератора')
    status_student = models.BooleanField(default=True, verbose_name='статус обучающегося')

    #  Поле для мягкого удаления пользователя из базы
    is_deleted = models.BooleanField(default=False, verbose_name='удален')

    groups_users = models.ManyToManyField('users.UserGroup', related_name='users_groups',
                                          verbose_name='группы пользователей', blank=True)
    additional_programs = models.ManyToManyField('materials.Program', related_name='users',
                                                 verbose_name='доп. программы', blank=True)
    additional_tests = models.ManyToManyField('knowledge_testing.Test', related_name='users',
                                              verbose_name='доп. тесты', blank=True)

    is_anonymous = models.BooleanField(default=False, verbose_name='анонимный')

    # Дата создания и обновления пользователя
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']


class UserGroup(models.Model):
    """Модель для хранения групп пользователей."""

    status = (
        ('A', 'администратор'),
        ('M', 'модератор'),
        ('S', 'обучающийся')
    )

    group_name = models.CharField(max_length=120, verbose_name='название группы')
    description = models.TextField(verbose_name='описание группы', **NULLABLE)
    is_status = models.BooleanField(max_length=1, choices=status, verbose_name='статус группы')
    users = models.ManyToManyField('users.User', related_name='users_groups', verbose_name='пользователи', blank=True)
    programs = models.ManyToManyField('materials.Program', verbose_name='программы', blank=True)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='создатель')

    #  Поле для мягкого удаления группы из базы
    is_deleted = models.BooleanField(default=False, verbose_name='удален')

    # Дата создания и обновления группы
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'группа пользователей'
        verbose_name_plural = 'группы пользователей'
        ordering = ['group_name']
