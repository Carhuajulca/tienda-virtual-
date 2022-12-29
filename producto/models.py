from django.db import models

# Create your models here.
class Marca(models.Model):
    nobre = models.CharField("Nombre", max_length=50)

class Color(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

class Medida(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    categ_padre = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField("Nombre" , max_length=50)
    precio = models.DecimalField("Precio", max_digits=9, decimal_places=2)
    estado = models.CharField("Estado", max_length=1)
    slug = models.CharField("Slug", max_length=50)
    precio_oferta = models.DecimalField("Precio oferta", max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    marca_codigo = models.ForeignKey(Marca, on_delete=models.RESTRICT)

class PResentacion(models.Model):
    stock = models.DecimalField("Stock Actual", max_digits=9, decimal_places=2)
    precio = models.DecimalField("Precio", max_digits=9, decimal_places=2, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
