from django import forms
from django.forms import DateInput
from Models.Seccion.models import Seccion

class FormularioSeccion(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = '__all__'