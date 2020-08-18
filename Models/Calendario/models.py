from django.db import models

class Calendario(models.Model):
    id_calendario= models.AutoField(primary_key=True)
    Descripcion =  models.CharField(max_length=30)




    def __str__(self):
        return '{} {}'.format(self.Descripcion)