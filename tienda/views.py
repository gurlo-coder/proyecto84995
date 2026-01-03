from django.shortcuts import render
from tienda.models import DepartamentoProductos


def home(request):
    return render(request, "tienda/index.html")


def departamentoProductos(request):
    departamentos_query = DepartamentoProductos.objects.all() #list(queryset[Depto...])
    
    contexto = {
        'departamentos': departamentos_query
    }
    
    return render(request, 'tienda/producto.html', contexto)



