# Generated by Django 5.0.2 on 2024-04-17 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duenos',
            old_name='dueno_pk',
            new_name='id_dueno',
        ),
    ]
