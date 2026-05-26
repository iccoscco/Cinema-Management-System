from django.urls import path
from . import views

urlpatterns = [
    path('comprar/<int:pelicula_pk>/', views.comprar, name='comprar'),
    path('historial/', views.historial, name='historial'),
    path('funciones/', views.gestionar_funciones, name='gestionar_funciones'),
    path('funciones/crear/', views.crear_funcion, name='crear_funcion'),
    path('funciones/<int:pk>/eliminar/', views.eliminar_funcion, name='eliminar_funcion'),
]
