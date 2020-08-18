from django.db import models

class Horario(models.Model):
    id_hora= models.AutoField(primary_key=True)
    Descripcion= models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre