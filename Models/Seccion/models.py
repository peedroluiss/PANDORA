from django.db import models

# Create your models here.


class Seccion(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre