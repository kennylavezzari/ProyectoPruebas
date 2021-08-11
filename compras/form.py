
from django import forms
from compras.models import Producto, Cliente, Factura, Detalle_factura


class ClienteForm(forms.ModelForm):
    class Meta:
          model = Cliente
          fields = '_all_'


class ProductoForm(forms.ModelForm):
    class Meta:
          model = Producto
          fields = '_all_'