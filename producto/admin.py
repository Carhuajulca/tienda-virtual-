from django.contrib import admin
from producto.models import *

# Register your models here.
admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Medida)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Presentacion)
admin.site.register(Imagen)