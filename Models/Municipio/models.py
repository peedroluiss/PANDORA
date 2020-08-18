from django.db import models
from Models.Departamento.models import  Departamento

# Create your models here.
class Municipio(models.Model):

    id_muni = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    departamento_id_depa= models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre