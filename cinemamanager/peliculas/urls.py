from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<int:pk>/', views.detalle, name='detalle'),
    path('<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
]
