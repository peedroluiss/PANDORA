from django.db import models
from Models.Municipio.models import Municipio
from Models.Director.models import Director

# Create your models here.

class Establecimiento(models.Model):
    id_esta = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    director_id_direct = models.ForeignKey(Director, on_delete=models.CASCADE)
    municipio_id_muni= models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)