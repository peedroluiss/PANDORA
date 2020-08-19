from django.forms import ModelForm
from Models.Municipio.models import Municipio


class FormsMunicipio(ModelForm):
    class Meta:
        model = Municipio
        fields = [
            'Nombre',
            'departamento_id_depa',
        ]

        labels = {
            'Nombre': 'Nombre de municipio',
            'departamento_id_depa': 'Departamento',
        }
