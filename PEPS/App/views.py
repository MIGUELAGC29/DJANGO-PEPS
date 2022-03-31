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
        username = request.user.username #se obtiene el username del usuario que entro en sesión
        ide = request.user.id #se obtiene el id del ususario
        almacenes = Almacen.objects.filter(usuario_id = ide) #obtenemos que almacenes tiene cada usuario 
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
            
        return render(request, 'home.html', {'username':username,
                                             'almacenes':almacenes,
                                             'd':d,
                                             'precio':precio,
                                             'costo':costo,
                                             'unidades':unidades,}) #mandamos todo lo necesario al template
        