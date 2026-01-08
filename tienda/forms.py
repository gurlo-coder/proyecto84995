from django import forms
from tienda.models import DepartamentoProductos
from tienda.models import DepartamentoClientes
from tienda.models import DepartamentoVentas


class DepartamentoProductosForm(forms.ModelForm):
    class Meta:
        model= DepartamentoProductos
        fields=['id_producto','nbre_producto','precio_producto','sku_producto',]

        widgets={
'id_producto':forms.NumberInput(attrs={'class':'form-control'}),
'nbre_producto':forms.TextInput(attrs={'class':'form-control'}),
'precio_producto':forms.NumberInput(attrs={'class':'form-control'}),
'sku_producto':forms.NumberInput(attrs={'class':'form-control'}),
        }
# vamos a crear el formulario de los clientes
class DepartamentoClientesForm(forms.ModelForm):
    class Meta:
        model=DepartamentoClientes
        fields=[
            'id_cliente',
            'nbre_cliente',
            'apellido_cliente',
            'id_producto',
            'email_cliente',
            'tel_cliente',
        ]
        widgets={
            'id_cliente':forms.NumberInput(attrs={'class':'form-control'}),
            'nbre_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'id_producto':forms.NumberInput(attrs={'class':'form-control'}),
            'email_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'tel_cliente':forms.NumberInput(attrs={'class':'form-control'}),
        }

        # Registro de las ventas 
class DepartamentoVentasForm(forms.ModelForm):
            class Meta:
                model=DepartamentoVentas
                fields=[
                    'id_venta',
                    'nbre_producto',
                    'nbre_cliente',
                    'id_producto',
                    
                ]
                widgets={
                    'id_venta':forms.NumberInput(attrs={'class':'form-control'}),
                    'nbre_producto':forms.TextInput(attrs={'class':'form-control'}),
                    'nbre_cliente':forms.TextInput(attrs={'class':'form-control'}),
                    'id_producto':forms.NumberInput(attrs={'class':'form-control'}),
                    # 'fecha_de_venta':forms.DateInput(attrs={'class':'form-control'}),
                }
