from django.db import models

from config.settings import NULLABLE


class Individual(models.Model):
    """Модель для хранения данных физлица."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор', **NULLABLE)
    last_name = models.CharField(max_length=120, verbose_name='фамилия')
    first_name = models.CharField(max_length=120, verbose_name='имя')
    middle_name = models.CharField(max_length=120, verbose_name='отчество')
    data_of_birth = models.DateField(verbose_name='дата рождения')
    SNILS = models.CharField(max_length=14, verbose_name='СНИЛС', **NULLABLE)

    # Контактные данные
    phone_number = models.CharField(max_length=20, verbose_name='номер телефона', **NULLABLE)
    email = models.EmailField(verbose_name='электронная почта', **NULLABLE)

    avatar = models.ImageField(upload_to='individuals/', verbose_name='аватар', **NULLABLE)

    # Даты создания и обновления данных физлица
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'
        ordering = ['moderator']
