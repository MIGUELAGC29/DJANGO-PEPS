from django.forms import *
from . import models



class FormuluarioCrear(ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        