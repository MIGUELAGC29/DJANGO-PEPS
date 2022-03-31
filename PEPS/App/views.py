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
        username = request.user.username
        ide = request.user.id
        almacenes = Almacen.objects.filter(usuario_id = ide)
        num_almacen = len(almacenes)
        d = {}
        precio = {}
        costo = {}
        
        
        for almacen in almacenes:
            productos = Producto.objects.filter(Almacen_id = almacen.id)
            d[almacen] = productos
            lista_precio = []
            lista_costo = []
            resultado_precio = 0
            resultado_costo = 0
            for producto in productos:
                lista_precio.append(producto.precio)
                lista_costo.append(producto.costo)
            for pre in lista_precio:
                resultado_precio += int(pre)
            for prec in lista_costo:
                resultado_costo += int(prec)
            precio[almacen] = resultado_precio
            costo[almacen] = resultado_costo
            lista_precio.clear()
            lista_costo.clear()
        return render(request, 'home1.html', {'username':username,
                                             'almacenes':almacenes,
                                             'd':d,
                                             'precio':precio,
                                             'costo':costo})
        