from django import forms
from django.forms import  DateInput
from Models.Catedratico.models import Catedratico

class FormularioCatedratico(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = '__all__'