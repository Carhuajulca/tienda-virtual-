from django.contrib import admin
from producto.models import *
from producto.forms import ProductoForm

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    list_per_page = 4

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'categoria__nombre', 'marca_codigo__nombre']
    # list_display modificas la columna de la tabla de listado de producto  
    list_display = ( 'nombre', 'categoria', 'estado','marca_codigo' ,'precio_oferta', 'porcentaje_oferta','precio')

    # list_filter agrega filtros a la busqeuda
    list_filter = ['categoria', 'marca_codigo']

    # ordering, ordena por el nombre de la columman que se desea
    ordering = ['nombre']

    # listado de paginas que deseas ver
    list_per_page = 20

    # me abre una nueva ventana y puedo aprovechar todas las configuraciones
    raw_id_fields = ['categoria']

    # Agregando formulario
    form = ProductoForm

 





admin.site.register(Producto, ProductoAdmin)



admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Medida)
admin.site.register(Imagen)
admin.site.register(Presentacion)