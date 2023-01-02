from django import forms
from producto.models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        models = Producto
        fields = ['nombre', 'marca_codigo', 'nombre', 'precio', 'precio_oferta', 'porcentaje_oferta']
        