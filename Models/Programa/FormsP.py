from django import forms
from django.forms import  DateInput

from Models.Programa.models import Programa


class FormularioPrograma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
