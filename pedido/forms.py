from django import forms
from pedido.models import Cliente
from django.core.exceptions import ValidationError


# Toda validacioón se hace en formularios
# modificando nuestro formularios
class ClienteForm(forms.ModelForm):
    

    # metodo para realoizar validaciones
    def clean(self):
        super().clean()
        print(self.cleaned_data)
        dni = self.cleaned_data.get('dni')
        if dni is not None and len(dni) < 8:
            raise ValidationError("DNI no es correcto")
        print(dni)

    class Meta:
        model = Cliente
        fields = '__all__' # Atributo __all__ se utuliza para mostras todas las columnas del modelo


