from django.db import models


class Director(models.Model):

    id_direct = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre