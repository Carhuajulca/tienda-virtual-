from django import forms
from .models import Cliente, Pedido, DetallePedido

# modificando nuestro formularios
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        # Atributo __all__ se utuliza para mostras todas las columnas del modelo
        fields = '__all__' 