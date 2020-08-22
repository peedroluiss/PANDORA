from django.forms import ModelForm
from django.forms import  DateInput
from Models.Inscripcion.models import Inscripcion

class FormularioInscripcion(ModelForm):


    class Meta:
        model = Inscripcion
        fields = [
            'fecha',
            'grado_id_grado',
            'seccion_id_seccion',
            'alumno_id_alumno',
            'establecimiento_id_esta',


        ]

        labels = {
            'fecha': 'Fecha de Inscripcion',
            'seccion_id_seccion': 'seccion',
            'alumno_id_alumno': 'Nombre de alumno',
            'grado_id_grado': 'Grado ',
            'establecimiento_id_esta': 'Establecimiento',


        }
        widgets = {"fecha": DateInput(attrs={'type': 'date'})}