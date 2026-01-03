from django.contrib import admin
from tienda.models import *

#admin.site.register(DepartamentoProductos)

@admin.register(DepartamentoProductos)
class DepartamentoProductosAdmin(admin.ModelAdmin):
    # columnas visibles en la lista modelo
    list_display = ("id_producto","nbre_producto","precio_producto","sku_producto")
    # columnas con enlaces clickeables para entra en el detalle
    list_display_links=("nbre_producto",)
    #campos por los que se pueden buscar
    search_fields=("nbre_producto",)
    # filtros laterales
    list_filter=("sku_producto",)
    # orden por defecto
    ordering=("id_producto","nbre_producto")
    # campos de solo lectura 
    readonly_fields=("nbre_producto",)

    #admin de la seccion de venta
    admin.site.register(DepartamentoVentas)

    # admin de la seccion de cliente
    admin.site.register(DepartamentoClientes)


