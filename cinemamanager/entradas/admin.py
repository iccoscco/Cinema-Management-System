from django.contrib import admin
from .models import Funcion, Compra

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ['pelicula', 'fecha_hora', 'sala', 'precio', 'asientos_disponibles']

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'funcion', 'cantidad', 'total', 'fecha_compra']
