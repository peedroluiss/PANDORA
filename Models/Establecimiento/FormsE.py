from django.forms import ModelForm

from Models.Establecimiento.models import Establecimiento

class FormsEstablecimiento(ModelForm):
    class Meta:
        model = Establecimiento
        fields = [
            'Nombre',
            'director_id_direct',
            'municipio_id_muni',
        ]

        labels = {
            'Nombre': 'Nombre de establecimiento',
            'director_id_direct': 'Director',
            'municipio_id_muni': 'Municipio',
        }
