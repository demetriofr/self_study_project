from django.db import models


class SOUTCard(models.Model):
    """Модель для хранения реквизитов данных карты специальной оценки условий труда (СОУТ)."""

    labor_conditions_class = [
        (10, 'optimal'),
        (20, 'permissible'),
        (31, 'harmful labor conditions of the 1'),
        (32, 'harmful labor conditions of the 2'),
        (33, 'harmful labor conditions of the 3'),
        (34, 'harmful labor conditions of the 4'),
        (40, 'hazardous labor conditions')
    ]

    admin = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='администратор')
    sout_card_number = models.CharField(max_length=120, verbose_name='номер карты СОУТ')
    date_of_card_creation = models.DateTimeField(verbose_name='дата создания карты СОУТ')
    ut_class = models.CharField(max_length=2, choices=labor_conditions_class, verbose_name='класс УТ')

    # Дата создания и обновления
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'Карта СОУТ'
        verbose_name_plural = 'Карты СОУТ'

    def __str__(self):
        return self.sout_card_number
