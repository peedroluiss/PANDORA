# Generated by Django 3.1 on 2020-08-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id_direct', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=30)),
                ('Correo', models.CharField(max_length=30)),
            ],
        ),
    ]
