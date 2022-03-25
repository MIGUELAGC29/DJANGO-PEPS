from django.db import models
from Login.models import Usuario

class Almacen(models.Model):
    nombre = models.CharField('Nombre', max_length = 100, blank=True, null=True)
    capacidad = models.PositiveIntegerField('Capacidad', default = 1, blank = True )
    fecha_creacion = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    
    
class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length = 100, blank=True, null=True)
    apellido_pat = models.CharField('Apellido Paterno', max_length = 100, blank=True, null=True)
    apellido_mat = models.CharField('Apellido Materno', max_length = 100, blank=True, null=True)
    empresa = models.CharField('Empresa', max_length = 100, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length = 100, blank=True, null=True)
    
    
class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length = 100, blank=True, null=True)
    precio = models.PositiveIntegerField('Precio', default = 1, blank = True )
    costo = models.PositiveIntegerField('Costo', default = 1, blank = True )
    unidades = models.PositiveIntegerField('Unidades', default = 1, blank = True )
    descripcion = models.CharField('Descripcion', max_length = 200, blank=True, null=True)
    Almacen = models.ForeignKey(Almacen, on_delete = models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    