# Generated by Django 3.1 on 2020-08-19 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grado', '0002_auto_20200818_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grado',
            old_name='ca_id_calendario',
            new_name='calendario_id_ca',
        ),
    ]
