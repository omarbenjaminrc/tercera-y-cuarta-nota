from dataclasses import fields
from django import forms
from django_seminario_app.models import Inscripcion



class Form_inscripcion(forms.ModelForm):
    class Meta:
        model   = Inscripcion
        fields = '__all__'