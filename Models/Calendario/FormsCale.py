from django import forms
from django.forms import  DateInput

from Models.Calendario.models import Calendario


class FormularioCalendario(forms.ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'