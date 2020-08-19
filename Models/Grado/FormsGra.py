from django import forms
from django.forms import  DateInput

from Models.Grado.models import Grado


class FormularioGrado(forms.ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'