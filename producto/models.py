from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    
    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
   
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = "Colores"   


class Medida(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

    def __str__(self):
       return self.nombre 


class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    categ_padre = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = "Categorías"    


class Producto(models.Model):
    nombre = models.CharField("Nombre" , max_length=50)
    precio = models.DecimalField("Precio", max_digits=9, decimal_places=2)
    estado = models.CharField("Estado", max_length=1)
    slug = AutoSlugField(populate_from='nombre', unique_with=['nombre'], always_update=True)
    precio_oferta = models.DecimalField("Precio oferta", max_digits=9, decimal_places=2, null=True, blank=True)
    porcentaje_oferta = models.DecimalField("Porcentaje descuento", max_digits=9, decimal_places=2, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    marca_codigo = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    def __str__(self):
       return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"

class Presentacion(models.Model):
    stock = models.DecimalField("Stock Actual", max_digits=9, decimal_places=2)
    precio = models.DecimalField("Precio", max_digits=9, decimal_places=2, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
       return self.producto.nombre + '' + self.medida.nombre + '' + self.colore.nombre

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = "Presentaciones"   

class Imagen(models.Model):
    nombre = models.ImageField("Nombre", upload_to="productos")
    order = models.SmallIntegerField("Orden")
    Producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)

    def __str__(self):
       return self.nombre 

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = "Imagenes"