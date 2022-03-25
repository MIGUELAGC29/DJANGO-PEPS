from django.shortcuts import render
from django.http import HttpResponse
from . import models
from App.models import Almacen, Producto, Proveedor

# Create your views here.
def Home(request):
    #nombre del usuario
    #cuantos almacenes tiene
    #obtener los productos de cada almacen
    if request.method == "POST" or request.method == "GET":
        print('Holi soy muy feliz')
        username = request.user.username
        print(username)
        ide = request.user.id
        print('ide: ' + str(ide))
        almacenes = Almacen.objects.filter(usuario_id = ide)
        num_almacen = len(almacenes)
        print(num_almacen)
        print(almacen.id)
        productos = Producto.objects.filter(Almacen_id = almacen.id)
        return render(request, 'home1.html', {'username':username,
                                             'almacenes':almacenes,
                                             'productos':productos})
           
        
    else:
        print(('Soy muy trsite'))
    
    """def listar_todo(request)
		articulos = articles.objects.all()
		return render(request, 'articulos.html', {'articulos':articulos})"""
    
    #return render(request, 'home1.html', {'almacenes':almacenes})
    #return render(request, 'home1.html')