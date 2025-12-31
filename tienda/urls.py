from django.urls import path
from tienda.views import *

urlpatterns = [
    path("home",home,name="home"),
    path("producto", DepartamentosProductos,name="producto"),
]