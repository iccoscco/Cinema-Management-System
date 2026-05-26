from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text='Duración en minutos (60-300)')
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    anio = models.PositiveIntegerField()
    destacada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.duracion is not None and (self.duracion < 60 or self.duracion > 300):
            raise ValidationError({'duracion': 'La duración debe estar entre 60 y 300 minutos.'})

    @property
    def rating_promedio(self):
        ratings = self.comentarios.exclude(rating=None)
        if not ratings.exists():
            return None
        return round(ratings.aggregate(avg=models.Avg('rating'))['avg'], 1)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-creada']


class Comentario(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField(max_length=500)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.rating is not None and (self.rating < 1 or self.rating > 5):
            raise ValidationError({'rating': 'El rating debe estar entre 1 y 5.'})
        if self.texto and (len(self.texto.strip()) < 1 or len(self.texto.strip()) > 500):
            raise ValidationError({'texto': 'El comentario debe tener entre 1 y 500 caracteres.'})

    def __str__(self):
        return f"{self.usuario.username} → {self.pelicula.titulo}"
