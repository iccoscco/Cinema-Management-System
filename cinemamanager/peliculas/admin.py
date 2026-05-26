from django.contrib import admin
from .models import Pelicula, Genero, Comentario

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'genero', 'anio', 'duracion', 'destacada']
    list_filter = ['genero', 'destacada']
    search_fields = ['titulo']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pelicula', 'rating', 'fecha']
