# Generated by Django 5.0.2 on 2024-04-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0005_mascotas_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='Sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1),
        ),
    ]
