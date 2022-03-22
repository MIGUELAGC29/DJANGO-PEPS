from django.urls import path
from App.views import *


urlpatterns = [
    path('home/', HolaMundo, name = "Home"),
    
]
