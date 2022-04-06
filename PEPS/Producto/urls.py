from django.urls import path
from Producto.views import *


urlpatterns = [
    path('crearproducto/<int:id>', Crear_Producto, name = "Crear_Producto"),
    path('guardarproducto/<int:id>', Guardar_Producto, name = "Guardar_Producto" ),
    path('agregarunidades/<int:id>', Agregar_Unidades, name = "Agregar_Unidades"),
    path('quitarunidades/<int:id>', Quitar_Unidades, name = "Quitar_Unidades"),
    path('guardarproducto2/<int:id>', Guardar_Producto2, name = "Guardar_Producto2" ),
    path('guardarproducto3/<int:id>', Guardar_Producto3, name = "Guardar_Producto3" ),
]