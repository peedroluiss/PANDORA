from django.db import models
from Models.Establecimiento.models import Establecimiento


class Catedratico(models.Model):
        id_catedra= models.AutoField(primary_key=True)
        Nombre =  models.CharField(max_length=30)
        Apellido = models.CharField(max_length=30)
        Direccion =  models.CharField(max_length=30)
        establecimiento_id_esta= models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

        def __str__(self):
                return '{} {}'.format(self.Nombre, self.Apellido)

