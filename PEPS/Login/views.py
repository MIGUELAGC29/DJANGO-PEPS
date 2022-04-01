from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse

from django.contrib.auth.views import LoginView, LogoutView
from django.template.context_processors import request
from django.views.generic import *
from django.urls import reverse_lazy
from . import models, forms


class InicioSesion(LoginView):
    template_name = 'login.html'
    #MANTENER AL USUARIO LOGEADO
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home')
        return super().dispatch(request, *args, **kwargs)
    




class CrearUser(CreateView):
    model = models.Usuario
    form_class = forms.FormularioUsuario
    template_name = "crear.html"
    success_url = reverse_lazy('Login')
    
   
        

"""def ListarUser(request):
    counter = 0
    if request.method == "POST" or request.method == "GET":
        users = models.Usuario.objects.all()
        for u in users:
            counter = counter + 1
            if counter != 0:
                return render(request, 'listado.html', {'users': users})
            else:
                return render(request, 'vacio.html')
    return render(request, 'vacio.html')


class EliminarUser(DeleteView):
    model = models.Usuario
    template_name = "delete.html"
    success_url = reverse_lazy('listado_1')

class EditarUser(UpdateView):
    model = models.Usuario
    form_class = forms.FormularioUsuario
    template_name = "edit.html"
    success_url = reverse_lazy('listado_1')"""