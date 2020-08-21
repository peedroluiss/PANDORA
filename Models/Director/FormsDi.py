from django import forms
from Models.Director.models import Director


class FormularioDirector(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
