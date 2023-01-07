from django import forms
from producto.models import Producto

# Classe que se importara en admin.py
class ProductoForm(forms.ModelForm):
    
    class Meta:
        models = Producto
        fields = ['nombre', 'marca_codigo', 'nombre', 'precio', 'precio_oferta', 'porcentaje_oferta']
        