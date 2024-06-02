# Generated by Django 5.0.6 on 2024-06-01 03:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('knowledge_testing', '0001_initial'),
        ('materials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='модератор'),
        ),
        migrations.AddField(
            model_name='test',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='модератор'),
        ),
        migrations.AddField(
            model_name='test',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.module', verbose_name='модуль'),
        ),
        migrations.AddField(
            model_name='test',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.program', verbose_name='программа'),
        ),
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(blank=True, to='knowledge_testing.question', verbose_name='вопросы'),
        ),
        migrations.AddField(
            model_name='testing',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='обучающийся'),
        ),
        migrations.AddField(
            model_name='testing',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge_testing.test', verbose_name='тест'),
        ),
    ]
