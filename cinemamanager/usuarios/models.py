from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class Usuario(AbstractUser):
    ROLES = [('cliente', 'Cliente'), ('admin', 'Administrador')]
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')
    edad = models.PositiveIntegerField(null=True, blank=True)
    favoritos = models.ManyToManyField('peliculas.Pelicula', blank=True, related_name='fans')

    def clean(self):
        super().clean()
        if self.edad is not None:
            if self.edad < 13 or self.edad > 100:
                raise ValidationError({'edad': 'La edad debe estar entre 13 y 100 años.'})

    def __str__(self):
        return f"{self.username} ({self.rol})"
