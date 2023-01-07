from django.contrib import admin
# Importanto los modelos
from .models import Cliente, Pedido, DetallePedido
# importando ClienteForm
from .forms import ClienteForm

# Register your models here.
# Segunda froma de registrar modelos con decarodadores
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Forma de busqueda por campos
    search_fields = ['nombres', 'apellidos', 'dni']
    # Campos que se muestren en el panel de control 
    list_display = ['dni', 'apellidos', 'nombres', 'email', 'direccion', 'celular' ]
    # Ordar por:
    ordering = ['apellidos', 'nombres']
    # llamando la clas ClienteForm
    forms = ClienteForm
    # Ordenadno campos de nuestro formulario en el panel de control 
    fieldsets = (
        ('Datos del cliente', {
            'fields': (
                'apellidos',
                'nombres',
                'dni'
            )
        }),
        ('Datos Secunadrios', {
            'fields': (('email', 'direccion'), 'celular')
        })
    )

# admin.site.register(Cliente, ClienteAdmin)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Cliente)
# admin.site.register(Pedido)
# admin.site.register(DetallePedido)