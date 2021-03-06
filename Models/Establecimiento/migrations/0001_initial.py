# Generated by Django 3.1 on 2020-08-17 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Director', '0001_initial'),
        ('Municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id_esta', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('director_id_direct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Director.director')),
                ('municipio_id_muni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Municipio.municipio')),
            ],
        ),
    ]
