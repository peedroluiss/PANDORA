from django.db import models

class Alumno(models.Model):
    id_alumno= models.AutoField(primary_key=True)
    Nombre =  models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=30)
    Tutelar = models.CharField(max_length=30)
    Telefono= models.IntegerField()



    def __str__(self):
        return '{} {}'.format(self.Nombre, self.Apellido)