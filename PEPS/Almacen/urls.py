from django.urls import path
from App.views import *
from Almacen.views import *


urlpatterns = [
    path('crear_almacen/', Vista_Formulario_Almacen, name = "Crear_Almacen"),
    path('mostrar/', Guardar_Almacen, name = "Guardar_Almacen" ),
    
]
