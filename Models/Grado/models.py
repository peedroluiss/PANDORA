from django.db import models
from Models.Programa.models import Programa
from Models.Calendario.models import Calendario
from Models.Horario.models import Horario


class Grado(models.Model):
    id_grado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    programa_id_prog = models.ForeignKey(Programa, on_delete=models.CASCADE)
    horario_id_hora = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_grado


    #def __str__(self):
        #return self.Nombre
