# Generated by Django 5.0.4 on 2024-04-18 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dueno',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('especie', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.dueno')),
            ],
        ),
        migrations.CreateModel(
            name='desparacitacion',
            fields=[
                ('id_desparacitacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=100)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('razon', models.CharField(max_length=255)),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.dueno')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascota')),
            ],
        ),
    ]
