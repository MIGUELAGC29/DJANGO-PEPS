from django.contrib import admin
from Login.models import Usuario
from App.models import Almacen, Producto, Proveedor

admin.site.register(Usuario)
admin.site.register(Almacen)
admin.site.register(Proveedor)
admin.site.register(Producto)

