from django.contrib import admin
from producto.models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'categoria__nombre', 'marca_codigo__nombre' ]

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    # list_display modificas la columna de la tabla de listado de producto  
    list_display = ( 'nombre', 'categoria', 'estado','marca_codigo' ,'precio_oferta', 'porcentaje_oferta','precio')

    # list_filter agrega filtros a la busqeuda
    list_filter = ['categoria', 'marca_codigo']


admin.site.register(Producto, ProductoAdmin)



admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Medida)
admin.site.register(Imagen)
admin.site.register(Presentacion)