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
        print('--------------------')
        nombre_productos = {}
        
        for almacen in almacenes:
            lista_nombre_productos = []
            lista_precio_productos = []
            lista_costo_productos = []
            lista_unidades_productos = []
            lista_descripcion_productos = []
            lista_proveedor_productos = []
            #print(almacen.id)
            producto_almacen = Producto.objects.filter(Almacen_id = almacen.id)
            for producto in producto_almacen:
                lista_nombre_productos.append(producto.nombre)
                lista_precio_productos.append(producto.precio)
                lista_costo_productos.append(producto.costo)
                lista_unidades_productos.append(producto.unidades)
                lista_descripcion_productos.append(producto.descripcion)
                
                
            nombre_productos[almacen.id] = (lista_nombre_productos)
        print(nombre_productos.values())
            

    
        return render(request, 'home1.html', {'username':username,
                                             'almacenes':almacenes,
                                             'nombre_productos':nombre_productos})
           
        
    else:
        print(('Soy muy trsite'))
    
    """def listar_todo(request)
		articulos = articles.objects.all()
		return render(request, 'articulos.html', {'articulos':articulos})"""
    
    #return render(request, 'home1.html', {'almacenes':almacenes})
    #return render(request, 'home1.html')