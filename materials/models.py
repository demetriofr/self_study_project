from django.db import models

from config.settings import NULLABLE


class AdditionMaterial(models.Model):
    """Модель для хранения дополнительного материала."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор')
    title = models.CharField(max_length=120, verbose_name='название')
    type = models.CharField(max_length=120, verbose_name='вид')
    link = models.URLField(verbose_name='ссылка')
    is_public = models.BooleanField(default=False, verbose_name='публичный')

    # Дата создания и обновления дополнительного материала
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'доп. материал'
        verbose_name_plural = 'доп. материалы'
        ordering = ['title']


class Topic(models.Model):
    """Модель для хранения темы."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор')
    title = models.CharField(max_length=120, verbose_name='название темы')
    description = models.TextField(verbose_name='описание темы', **NULLABLE)

    # Материал, необходимый для подготовки по данной теме
    material = models.TextField(verbose_name='материал')
    additional_materials = models.ManyToManyField('materials.AdditionMaterial', verbose_name='доп. материалы',
                                                  blank=True)

    execution_time = models.PositiveIntegerField(verbose_name='время на выполнение')

    # Дата создания и обновления дополнительного материала
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'
        ordering = ['title']


class Module(models.Model):
    """Модель для хранения модуля."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор')
    title = models.CharField(max_length=120, verbose_name='название модуля')
    description = models.TextField(verbose_name='описание модуля', **NULLABLE)

    list_topics = models.ManyToManyField('materials.Topic', verbose_name='темы', blank=True)

    self_assessment_test = models.ManyToManyField('knowledge_testing.Test', related_name='modules',
                                                  verbose_name='тесты', blank=True)

    # Дата создания и обновления дополнительного материала
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
        ordering = ['title']


class Program(models.Model):
    """Модель для хранения программы."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор')
    title = models.CharField(max_length=120, verbose_name='название программы')
    description = models.TextField(verbose_name='описание программы', **NULLABLE)

    list_modules = models.ManyToManyField('materials.Module', verbose_name='модули', blank=True)
    self_assessment_test = models.ManyToManyField('knowledge_testing.Test', related_name='programs',
                                                  verbose_name='тесты', blank=True)

    is_public = models.BooleanField(default=False, verbose_name='публичный')

    # Дата создания и обновления дополнительного материала
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'программа'
        verbose_name_plural = 'программы'
        ordering = ['title']
