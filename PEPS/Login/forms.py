from django.forms import *
from . import models


SEXO = ['Masculino', 'Femenino', 'No Binario']


class FormuluarioCrear(ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        labels = {
            'nombre':'Nombre',
            'a_paterno':'Apellido Paterno',
            'a_Materno':'Apellido Materno',
        }
