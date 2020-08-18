from django.db import models

from django.db import models

class Programa(models.Model):
    id_prog= models.AutoField(primary_key=True)
    Contenidocbn =  models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=30)


    def __str__(self):
        return '{} {}'.format(self.Contenidocbn, self.Descripcion)