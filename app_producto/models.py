from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    id_ingrediente = models.IntegerField()

    def __str__(self):
        return f'Producto: {self.nombre_producto}'