from django.shortcuts import render,redirect
from .models import DepartamentoProductos
from .models import DepartamentoClientes
from .models import DepartamentoVentas
from .forms import DepartamentoProductosForm 
from .forms import DepartamentoClientesForm
from .forms import DepartamentoVentasForm



def home(request):
    return render(request, "tienda/index.html")


def departamentoProductos(request):
    departamentos_query = DepartamentoProductos.objects.all() #list(queryset[Depto...])
    
    contexto = {
        'departamentos': departamentos_query
    }
    
    return render(request, 'tienda/producto.html', contexto)

    # function para clientes

def departamentoClientes(request):
    Clientes_query = DepartamentoClientes.objects.all() # list(queryset[dpta...])

    context={
        'Clientes': Clientes_query
    }
    return render(request,'tienda/cliente.html', context)


# function la venta 

def departamentoVentas(request):
    ventas_query= DepartamentoVentas.objects.all() # list(queryset[dept...])

    conta={

        'Ventas': ventas_query
    }
    return render(request,'venta.html',conta)

    #1 vamos a crear el formulario

def crear_producto(request):
    if request.method == 'POST':
        form = DepartamentoProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = DepartamentoProductosForm()

    return render(request, 'crearProducto.html', {'form': form})

    #2 vamos a crear un formulario de cliente

def crear_cliente(request):
    if request.method == 'POST':
        form = DepartamentoClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente")
    else:
        form = DepartamentoClientesForm()

    return render(request, 'crearcliente.html', {'form': form})

#crear una nueva venta

def crear_venta(request):
    if request.method == 'POST':
        form = DepartamentoVentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("venta")
    else:
        form = DepartamentoVentasForm()

    return render(request, 'crearventa.html', {'form': form})
