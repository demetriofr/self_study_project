from django.db import models

from config.settings import NULLABLE, AUTH_USER_MODEL
from users.models import User


class Question(models.Model):
    """Модель для хранения вопросов."""

    option = (
        ('option_a', 'вариант A'),
        ('option_b', 'вариант B'),
        ('option_c', 'вариант C'),
        ('option_d', 'вариант D'),
    )

    moderator = models.ForeignKey(AUTH_USER_MODEL, default=User.objects.first().pk,
                                  on_delete=models.CASCADE, verbose_name='модератор')
    question_text = models.CharField(max_length=400, verbose_name='вопрос')
    description = models.CharField(max_length=120, verbose_name='пояснения к вопросу', **NULLABLE)
    option_a = models.CharField(max_length=250, verbose_name='вариант A')
    option_b = models.CharField(max_length=250, verbose_name='вариант B')
    option_c = models.CharField(max_length=250, verbose_name='вариант C', **NULLABLE)
    option_d = models.CharField(max_length=250, verbose_name='вариант D', **NULLABLE)
    correct_option = models.CharField(max_length=8, choices=option, verbose_name='правильный вариант')
    topic = models.CharField(max_length=120, verbose_name='тема')
    explanation = models.TextField(verbose_name='пояснение', **NULLABLE)

    # дата создания и обновления
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ['question_text']

    def __str__(self):
        return self.question_text


class Test(models.Model):
    """Модель для хранения тестов."""

    moderator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='модератор')
    title = models.CharField(max_length=120, verbose_name='название теста')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    module = models.ForeignKey('materials.Module', on_delete=models.CASCADE, verbose_name='модуль', **NULLABLE)
    program = models.ForeignKey('materials.Program', on_delete=models.CASCADE, verbose_name='программа', **NULLABLE)
    questions = models.ManyToManyField('knowledge_testing.Question', verbose_name='вопросы', blank=True)
    self_assessment = models.BooleanField(default=False, verbose_name='самопроверка')
    execution_time = models.PositiveIntegerField(verbose_name='время на выполнение')

    # дата создания и обновления
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = ['title']

    def __str__(self):
        return self.title


class Testing(models.Model):
    """Модель для хранения тестирования."""

    results = (
        (0, 'не сдал'),
        (1, 'сдал'),
    )

    student = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='обучающийся')
    test = models.ForeignKey('knowledge_testing.Test', on_delete=models.CASCADE, verbose_name='тест')
    answers_to_questions = models.JSONField(verbose_name='ответы на вопросы')
    score = models.PositiveIntegerField(verbose_name='количество правильных ответов')
    result = models.CharField(max_length=1, choices=results, verbose_name='результат')

    # дата создания и обновления
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'тестирование'
        verbose_name_plural = 'тестирования'
        ordering = ['result']

    def __str__(self):
        return f'{self.student} - {self.test} - {self.score} - {self.result}'
