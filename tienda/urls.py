from django.urls import path
from .views import *

urlpatterns = [
    path("home",home,name="home"),
    path("productos", departamentoProductos,name="productos"),
    path("cliente",departamentoClientes,name="cliente"),
    path("venta",departamentoVentas,name="venta"),
    path("crear_product" , crear_producto , name="crear_product"),
    path("crear_cliento", crear_cliente , name="crear_cliento"),
    path("ver_venta", crear_venta , name="ver_venta"),
]