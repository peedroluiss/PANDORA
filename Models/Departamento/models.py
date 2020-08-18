from django.db import models


class Departamento(models.Model):

    id_depa = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre