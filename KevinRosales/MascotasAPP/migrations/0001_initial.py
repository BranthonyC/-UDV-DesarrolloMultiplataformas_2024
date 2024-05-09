# Generated by Django 5.0.4 on 2024-04-18 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('historial', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('Raza', models.CharField(max_length=50)),
                ('Especie', models.CharField(max_length=50)),
                ('Fecha_nacimiento', models.DateField()),
                ('Edad', models.IntegerField()),
                ('Sexo', models.CharField(max_length=10)),
                ('Color', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('propie_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
        migrations.CreateModel(
            name='Desparasitacion',
            fields=[
                ('cartilla_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tratamiento', models.CharField(max_length=100)),
                ('tipo_medicamento', models.CharField(max_length=255)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MascotasAPP.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('cita_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_y_hora', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=255)),
                ('lugar', models.CharField(max_length=255)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MascotasAPP.mascota')),
            ],
        ),
        migrations.AddConstraint(
            model_name='propietario',
            constraint=models.UniqueConstraint(fields=('nombre', 'correo'), name='unique_cita'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MascotasAPP.propietario'),
        ),
    ]
