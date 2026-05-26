from django.db import models
from datetime import datetime
from django.conf import settings
from django.core.exceptions import ValidationError


class Funcion(models.Model):
    pelicula = models.ForeignKey('peliculas.Pelicula', on_delete=models.CASCADE, related_name='funciones')
    fecha_hora = models.DateTimeField()
    sala = models.CharField(max_length=50)
    asientos_totales = models.PositiveIntegerField(default=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.fecha_hora and self.fecha_hora <= datetime.now():
            raise ValidationError({'fecha_hora': f"La fecha de la función debe ser futura al momento actual."})

    @property
    def asientos_disponibles(self):
        vendidas = self.compras.aggregate(total=models.Sum('cantidad'))['total'] or 0
        return self.asientos_totales - vendidas

    def __str__(self):
        return f"{self.pelicula.titulo} — {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} | Sala {self.sala}"

    class Meta:
        ordering = ['fecha_hora']


class Compra(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='compras')
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.cantidad is not None and (self.cantidad < 1 or self.cantidad > 10):
            raise ValidationError({'cantidad': 'Puedes comprar entre 1 y 10 entradas por compra.'})

    def __str__(self):
        return f"Compra #{self.pk} — {self.usuario.username}"

    class Meta:
        ordering = ['-fecha_compra']
