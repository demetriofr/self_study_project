from django.db import models

from config.settings import NULLABLE


class Organization(models.Model):
    """Модель для хранения данных об организации."""

    administrator = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                      verbose_name='администратор')
    full_name = models.CharField(max_length=220, verbose_name='полное название')
    short_name = models.CharField(max_length=120, verbose_name='сокращенное название', **NULLABLE)
    tin = models.CharField(max_length=9, verbose_name='ИНН', **NULLABLE)

    # Даты создания и обновления данных организации
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        ordering = ['full_name']


class Department(models.Model):
    """Модель для хранения данных структурного подразделения."""

    administrator = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                      verbose_name='администратор')

    name = models.CharField(max_length=120, verbose_name='название')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='организация')

    # Даты создания и обновления данных структурного подразделения
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'структурное подразделение'
        verbose_name_plural = 'структурные подразделения'
        ordering = ['name']


class Position(models.Model):
    """Модель для хранения данных о должности."""

    administrator = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                      verbose_name='администратор')
    name = models.CharField(max_length=120, verbose_name='название')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='структурное подразделение')
    quantity = models.PositiveIntegerField(verbose_name='количество сотрудников', **NULLABLE)
    sout_card = models.ForeignKey('workplaces.SOUTCard', on_delete=models.SET_NULL, verbose_name='СОУТ', **NULLABLE)
    programs = models.ManyToManyField('materials.Program', related_name='positions_materials', verbose_name='программы')

    # Даты создания и обновления данных должности
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'
        ordering = ['name']


class Worker(models.Model):
    """Модель для хранения данных о работнике."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                  verbose_name='модератор')
    individual = models.ForeignKey('individuals.Individual', on_delete=models.CASCADE,
                                   verbose_name='Физическое лицо')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='должность')
    personal_number = models.CharField(max_length=120, verbose_name='табельный номер', **NULLABLE)
    hire_date = models.DateField(verbose_name='дата приема на работу', **NULLABLE)
    dismissal_date = models.DateField(verbose_name='дата увольнения c работы', **NULLABLE)
    additional_programs = models.ManyToManyField('materials.Program', verbose_name='доп. программы', blank=True)

    # Даты создания и обновления данных работника
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.moderator

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'работники'
        ordering = ['moderator']
