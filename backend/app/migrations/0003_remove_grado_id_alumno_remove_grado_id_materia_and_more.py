# Generated by Django 4.1.1 on 2022-09-09 16:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_update_at_alumno_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grado',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='grado',
            name='id_materia',
        ),
        migrations.AddField(
            model_name='alumno',
            name='id_grado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.grado'),
        ),
        migrations.AddField(
            model_name='materia',
            name='id_grado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.grado'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(21), django.core.validators.MaxValueValidator(60)]),
        ),
    ]