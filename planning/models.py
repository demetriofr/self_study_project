from django.db import models


class TrainingMatrix(models.Model):
    """Модель для хранения матрицы обучения."""

    administrator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='администратор')
    position = models.ForeignKey('company.Position', on_delete=models.CASCADE, verbose_name='должность')
    program = models.ForeignKey('materials.Program', on_delete=models.CASCADE, verbose_name='программа')

    # Даты создания и обновления матрицы обучения
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f'{self.position} - {self.program}'

    class Meta:
        verbose_name = 'матрица обучения'
        verbose_name_plural = 'матрицы обучения'
        ordering = ['position']
