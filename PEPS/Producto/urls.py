from django.urls import path
from Producto.views import *


urlpatterns = [
    path('crearproducto/<int:id>', Crear_Producto, name = "Crear_Producto"),
    path('guardarproducto/<int:id>', Guardar_Producto, name = "Guardar_Producto" )
]