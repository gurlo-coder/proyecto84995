from django.shortcuts import render
from tienda.models import DepartamentoProductos

def home(request):
    return render(request, "tienda/index.html")


def DepartamentosProductos(request):
    departamentos_query = DepartamentoProductos.objects.all()
    
    contexto = {
        'departamentos': departamentos_query
    }
    
    return render(
        request,
        'tienda/producto.html',
        contexto
    )
