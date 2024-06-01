# Generated by Django 5.0.6 on 2024-06-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_testing', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['question_text'], 'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='пояснения к вопросу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(choices=[('option_a', 'вариант A'), ('option_b', 'вариант B'), ('option_c', 'вариант C'), ('option_d', 'вариант D')], max_length=8, verbose_name='правильный вариант'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=400, verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='result',
            field=models.CharField(choices=[(0, 'не сдал'), (1, 'сдал')], max_length=1, verbose_name='результат'),
        ),
    ]
