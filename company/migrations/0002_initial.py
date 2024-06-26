# Generated by Django 5.0.6 on 2024-06-01 03:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('individuals', '0001_initial'),
        ('materials', '0001_initial'),
        ('workplaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='администратор'),
        ),
        migrations.AddField(
            model_name='organization',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='администратор'),
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.organization', verbose_name='организация'),
        ),
        migrations.AddField(
            model_name='position',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='администратор'),
        ),
        migrations.AddField(
            model_name='position',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='структурное подразделение'),
        ),
        migrations.AddField(
            model_name='position',
            name='programs',
            field=models.ManyToManyField(related_name='positions_materials', to='materials.program', verbose_name='программы'),
        ),
        migrations.AddField(
            model_name='position',
            name='sout_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workplaces.soutcard', verbose_name='СОУТ'),
        ),
        migrations.AddField(
            model_name='worker',
            name='additional_programs',
            field=models.ManyToManyField(blank=True, to='materials.program', verbose_name='доп. программы'),
        ),
        migrations.AddField(
            model_name='worker',
            name='individual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individuals.individual', verbose_name='Физическое лицо'),
        ),
        migrations.AddField(
            model_name='worker',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='модератор'),
        ),
        migrations.AddField(
            model_name='worker',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.position', verbose_name='должность'),
        ),
    ]
