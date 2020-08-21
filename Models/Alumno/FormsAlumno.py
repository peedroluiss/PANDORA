from django import forms
from django.forms import  DateInput
from Models.Alumno.models import Alumno

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'