from django.contrib import admin
from tienda.models import *

admin.site.register(DepartamentoProductos)


    #admin de la seccion de venta
admin.site.register(DepartamentoVentas)

    # admin de la seccion de cliente
admin.site.register(DepartamentoClientes)


