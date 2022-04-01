from django import forms
from App.models import Almacen


class FormularioCrearAlmacen(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ('nombre','capacidad')
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre del Almacen',
                }
            ),
            'capacidad' : forms.NumberInput(
                attrs={
                    'placeholder' : 'Cantidad en Unidades',
                }
            ),
        }