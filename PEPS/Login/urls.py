from django.urls import path
from Login.views import *
from App.views import *

#from CRUD.APP.views import *

urlpatterns = [
    path('login/', InicioSesion.as_view(), name = "Login"),
    path('logout/', LogoutView.as_view(next_page = 'Login'), name = "Logout"),
    path('crearuser/', CrearUser.as_view(), name = "Crear"),
]