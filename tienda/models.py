from django.db import models

# Modelo Productos
class DepartamentoProductos(models.Model):
    id_producto = models.CharField(max_length=50, unique=True)
    nbre_producto = models.CharField(max_length=100)
    precio_producto = models.IntegerField(null=True)
    sku_producto = models.IntegerField(null=True)

    def __str__(self):
        return f"id_producto:{self.id_producto} nbre_producto:{self.nbre_producto}"


# Modelo Clientes
class DepartamentoClientes(models.Model):
    id_cliente = models.CharField(max_length=50, unique=True)
    nbre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    id_producto = models.IntegerField(null=True)
    email_cliente = models.EmailField()
    tel_cliente = models.IntegerField(null=True)

    def __str__(self):
        return f"nbre_cliente:{self.nbre_cliente} apellido_cliente:{self.apellido_cliente}"


# Modelo Ventas
class DepartamentoVentas(models.Model):
    id_venta = models.IntegerField(unique=True)
    nbre_producto = models.CharField(max_length=100)
    nbre_cliente = models.CharField(max_length=100)
    id_producto = models.IntegerField(null=True)
    fecha_de_venta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"id_venta:{self.id_venta} nbre_producto:{self.nbre_producto}"
