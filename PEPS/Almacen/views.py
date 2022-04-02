from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from App.models import Almacen
from Login.models import Usuario
from App.models import Producto, Proveedor
from . import forms


# Create your views here.
"""class CrearAlmacen(CreateView):
    model = Almacen
    form_class = forms.FormularioCrearAlmacen
    template_name = "crear_almacen.html"
    succes_url = reverse_lazy('Home')"""


def Vista_Formulario_Almacen(request):
    
    return render(request, 'crear_almacen.html')

def Guardar_Almacen(request):
    if request.method == "POST" or request.method == "GET":
        nombre = request.POST['nombre']
        capacidad = request.POST['cantidad']
        user_id = request.user.id
        almacen = Almacen(
            nombre=nombre,
            capacidad= capacidad,
            usuario_id = user_id,
        )
        almacen.save()
        
        username = request.user.username #se obtiene el username del usuario que entro en sesión
        ide = request.user.id #se obtiene el id del ususario
        almacenes = Almacen.objects.filter(usuario_id = ide) #obtenemos que almacenes tiene cada usuario 
        print(almacenes)
        num_almacen = len(almacenes) #obtenemos el numero de almacenes
        
        d = {} #diccionario para extraer los productos: la key del diccionario es el numero de almacen y el valor son todos los productos
        precio = {} #diccionario para obtener precios de los productos: la key del diccionario es el almacen y el valor son todos los precios de los productos en el almacen
        costo = {} #diccionario para obtener costos de los productos: la key del diccionario es el almacen y el valor son todos los costos de los productos en el almacen
        unidades = {} #diccionario para obtener las unidades de los productos: la key del diccionario es el almacen y el valor son todas las unidades de los productos en el almacen
        
        
        for almacen in almacenes: #recorremos almacen por almacen 
            productos = Producto.objects.filter(Almacen_id = almacen.id) #obtenemos los productos de el almacen
            d[almacen] = productos #agregamos la key y el value al diccionario {almacen1:prodicto1}
            lista_precio = [] #array donde se guardan los precios
            lista_costo = [] #array donde se guardan los costos
            lista_unidades = [] #array donde se guardan las unidades
            resultado_unidades = 0 #variable para ir acumulando el total
            resultado_precio = 0 #variable para ir acumulando el total
            resultado_costo = 0 #variable para ir acumulando el total
            
            for producto in productos: #recorremos producto por producto para obtener cada valor de cada producto
                lista_precio.append(producto.precio) #vamos agregando los valores al array
                lista_costo.append(producto.costo)
                lista_unidades.append(producto.unidades)
                
            for pre in lista_precio: #recorremos cada elemento en la lista para irlo sumando
                resultado_precio += int(pre) 
            for prec in lista_costo:
                resultado_costo += int(prec)
            for precu in lista_unidades:
                resultado_unidades += int(precu)
                
            unidades[almacen] = resultado_unidades #agregamos los valores al diccionario 
            precio[almacen] = resultado_precio
            costo[almacen] = resultado_costo
            
            lista_precio.clear() #limpiamos cada array para el proximo almacen
            lista_costo.clear()
            lista_unidades.clear()
        

    else:
        return HttpResponse("<h2> NO SE PUDO GUARDAR EL ALMACÉN</h2>")

    return render(request, 'home.html', {'username':username,
                                             'almacenes':almacenes,
                                             'd':d,
                                             'precio':precio,
                                             'costo':costo,
                                             'unidades':unidades,}) #mandamos todo lo necesario al template
    
    


def Eliminar_Almacen(request, id):
    if request.method == "POST" or request.method == "GET":
        id_almacen = id
        almacen = Almacen.objects.get(id=id_almacen)
        almacen.delete()
        
        username = request.user.username #se obtiene el username del usuario que entro en sesión
        ide = request.user.id #se obtiene el id del ususario
        almacenes = Almacen.objects.filter(usuario_id = ide) #obtenemos que almacenes tiene cada usuario 
        print(almacenes)
        num_almacen = len(almacenes) #obtenemos el numero de almacenes
        
        d = {} #diccionario para extraer los productos: la key del diccionario es el numero de almacen y el valor son todos los productos
        precio = {} #diccionario para obtener precios de los productos: la key del diccionario es el almacen y el valor son todos los precios de los productos en el almacen
        costo = {} #diccionario para obtener costos de los productos: la key del diccionario es el almacen y el valor son todos los costos de los productos en el almacen
        unidades = {} #diccionario para obtener las unidades de los productos: la key del diccionario es el almacen y el valor son todas las unidades de los productos en el almacen
        
        
        for almacen in almacenes: #recorremos almacen por almacen 
            productos = Producto.objects.filter(Almacen_id = almacen.id) #obtenemos los productos de el almacen
            d[almacen] = productos #agregamos la key y el value al diccionario {almacen1:prodicto1}
            lista_precio = [] #array donde se guardan los precios
            lista_costo = [] #array donde se guardan los costos
            lista_unidades = [] #array donde se guardan las unidades
            resultado_unidades = 0 #variable para ir acumulando el total
            resultado_precio = 0 #variable para ir acumulando el total
            resultado_costo = 0 #variable para ir acumulando el total
            
            for producto in productos: #recorremos producto por producto para obtener cada valor de cada producto
                lista_precio.append(producto.precio) #vamos agregando los valores al array
                lista_costo.append(producto.costo)
                lista_unidades.append(producto.unidades)
                
            for pre in lista_precio: #recorremos cada elemento en la lista para irlo sumando
                resultado_precio += int(pre) 
            for prec in lista_costo:
                resultado_costo += int(prec)
            for precu in lista_unidades:
                resultado_unidades += int(precu)
                
            unidades[almacen] = resultado_unidades #agregamos los valores al diccionario 
            precio[almacen] = resultado_precio
            costo[almacen] = resultado_costo
            
            lista_precio.clear() #limpiamos cada array para el proximo almacen
            lista_costo.clear()
            lista_unidades.clear()
        

    else:
        return HttpResponse("<h2> NO SE PUDO GUARDAR EL ALMACÉN</h2>")

    return render(request, 'home.html', {'username':username,
                                             'almacenes':almacenes,
                                             'd':d,
                                             'precio':precio,
                                             'costo':costo,
                                             'unidades':unidades,}) #mandamos todo lo necesario al template
    