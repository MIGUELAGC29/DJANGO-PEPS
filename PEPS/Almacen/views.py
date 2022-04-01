from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from App.models import Almacen
from Login.models import Usuario
from . import forms


# Create your views here.
"""class CrearAlmacen(CreateView):
    model = Almacen
    form_class = forms.FormularioCrearAlmacen
    template_name = "crear_almacen.html"
    succes_url = reverse_lazy('Home')"""


def Vista_Formulario_Almacen(request):
    return render(request, 'crear_almacen.html')

def Mostrar_Formulario(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        username = request.user.username

    else:
        return HttpResponse("<h2> NO SE PUDO GUARDAR AL USUARIO </h2>")

    return render(request, 'mostrar.html', {
        'nombre':nombre,
        'cantidad': cantidad,
        'username': username,
    })
    
    
    