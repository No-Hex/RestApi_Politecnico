# Generated by Django 4.1.1 on 2022-09-09 15:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('matricula', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(14)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('seccion', models.CharField(max_length=1)),
                ('capacidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre_materia', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(21)])),
                ('numero_telefonico', models.CharField(max_length=35)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('hora_de_inicio', models.TimeField()),
                ('hora_de_finalizacion', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_aula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.aula')),
                ('id_materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
                ('id_profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='id_profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profesor'),
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('grado', models.CharField(max_length=20)),
                ('id_alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('id_materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='id_grado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.grado'),
        ),
    ]
