from django.db import models
from producto.models import Presentacion
# Create your models here.

# Creando modelos en la app pedido
# Modelo Cleinte
class Cliente(models.Model):
    nombres = models.CharField("Nombres", max_length=50)
    apellidos = models.CharField("Apellidos", max_length=70)
    email =models.EmailField("Email")
    dni = models.CharField("DNI", max_length=8, null=True, blank=True)
    direccion = models.CharField("Direccion", max_length=50, null=True, blank=True)
    celular = models.CharField("Celular", max_length=20, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


    # Modelo de pedido
class Pedido(models.Model):
    fecha =  models.DateTimeField("Fecha")
    total  = models.DecimalField("Total", max_digits=9, decimal_places=2)
    numero = models.CharField("Número", max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)

    def __str__(self):
        return self.numero + " " + self.cliente.nombres + " " + self.cliente.apellidos
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural ="Pedidos"    

    # Modelo detalle pedido
class DetallePedido(models.Model):
    cantidad = models.DecimalField("Cantidades", max_digits=9, decimal_places=2)
    precio_unitario = models.DecimalField("Precio unitario" , max_digits=9, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.RESTRICT)

    def __str__(self):
        return self.pedido.numero + " " + self.presentacion.producto.nombre

    class Meta:
        verbose_name = "Detalle Pedido"
        verbose_name_plural = "Detalle del Pedido"