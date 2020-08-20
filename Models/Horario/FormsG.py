from django import forms
from django.forms import  DateInput
from Models.Horario.models import Horario


class FormularioHorario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'