# Generated by Django 4.1.1 on 2022-09-09 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_grado_id_alumno_remove_grado_id_materia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='id_grado',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='id_grado',
        ),
        migrations.AddField(
            model_name='grado',
            name='id_alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno'),
        ),
        migrations.AddField(
            model_name='grado',
            name='id_materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.materia'),
        ),
    ]