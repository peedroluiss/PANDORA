# Generated by Django 3.1 on 2020-08-19 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grado',
            old_name='calendario_id_calendario',
            new_name='ca_id_calendario',
        ),
    ]
