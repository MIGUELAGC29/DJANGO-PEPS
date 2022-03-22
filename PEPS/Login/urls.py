from django.urls import path
from Login.views import *
from App.views import *

#from CRUD.APP.views import *

urlpatterns = [
    path('login/', InicioSesion.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = "logout"),
    path('listado/', ListarUser, name = "listado_1"),
    path('crearuser/', CrearUser.as_view(), name = "crear"),
    path('deleteuser/<int:pk>/', EliminarUser.as_view(), name = "eliminar"),
    path('edituser/<int:pk>/', EditarUser.as_view(), name = "editar"),

]