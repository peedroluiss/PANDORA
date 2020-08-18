# Generated by Django 3.1 on 2020-08-17 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catedratico',
            fields=[
                ('id_catedra', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=30)),
                ('establecimiento_id_esta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Establecimiento.establecimiento')),
            ],
        ),
    ]
