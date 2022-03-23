from django.urls import path
from Login.views import *
from App.views import *

#from CRUD.APP.views import *

urlpatterns = [
    path('login/', InicioSesion.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = "logout"),
    path('crearuser/', CrearUser.as_view(), name = "crear"),
]