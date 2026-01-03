from django.urls import path
from tienda.views import *

urlpatterns = [
    path("home",home,name="home"),
    path("productos", departamentoProductos,name="productos"),
   
]