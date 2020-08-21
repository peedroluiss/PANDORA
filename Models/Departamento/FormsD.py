from django import forms

from Models.Departamento.models import Departamento


class FormularioDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

