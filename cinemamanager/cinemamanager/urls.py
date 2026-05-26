from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from peliculas import views as pelicula_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pelicula_views.catalogo, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('peliculas/', include('peliculas.urls')),
    path('entradas/', include('entradas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
