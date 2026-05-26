"""
populate_db.py — CinemaManager
Carga datos de ejemplo para demostración.
Uso: python manage.py shell < populate_db.py
  o: python populate_db.py (desde el directorio del proyecto)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemamanager.settings')
django.setup()

from django.contrib.auth import get_user_model
from peliculas.models import Genero, Pelicula
from entradas.models import Funcion
from django.utils import timezone
from datetime import timedelta

Usuario = get_user_model()

# Géneros
generos_data = ['Acción', 'Drama', 'Comedia', 'Terror', 'Ciencia Ficción', 'Animación']
generos = {}
for nombre in generos_data:
    g, _ = Genero.objects.get_or_create(nombre=nombre)
    generos[nombre] = g

# Películas de ejemplo
TMDB_BASE = 'https://image.tmdb.org/t/p/w500'
peliculas_data = [
    {'titulo': 'Dune: Parte Dos', 'poster_url': TMDB_BASE+'/cdqLnri3NEGcmfnqwk2TSIYtddg.jpg', 'descripcion': 'Paul Atreides se une a los Fremen y comienza un viaje espiritual para convertirse en Muad\'Dib.', 'duracion': 166, 'genero': 'Ciencia Ficción', 'anio': 2024, 'destacada': True},
    {'titulo': 'Oppenheimer', 'poster_url': TMDB_BASE+'/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg', 'descripcion': 'La historia del físico J. Robert Oppenheimer y su papel en el desarrollo de la bomba atómica.', 'duracion': 180, 'genero': 'Drama', 'anio': 2023, 'destacada': True},
    {'titulo': 'Pobres Criaturas', 'poster_url': TMDB_BASE+'/kCGlIMHnOm8JPXNbpUntpiadaAN.jpg', 'descripcion': 'La increíble evolución de Bella Baxter, una joven devuelta a la vida por el excéntrico científico Dr. Godwin Baxter.', 'duracion': 141, 'genero': 'Drama', 'anio': 2023, 'destacada': True},
    {'titulo': 'Godzilla x Kong', 'poster_url': TMDB_BASE+'/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg', 'descripcion': 'Los titanes se enfrentan a una amenaza colosal escondida dentro de nuestro mundo.', 'duracion': 115, 'genero': 'Acción', 'anio': 2024, 'destacada': False},
    {'titulo': 'Inside Out 2', 'poster_url': TMDB_BASE+'/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg', 'descripcion': 'Riley entra a la adolescencia y nuevas emociones llegan a su mente.', 'duracion': 100, 'genero': 'Animación', 'anio': 2024, 'destacada': False},
    {'titulo': 'Alien: Romulus', 'poster_url': TMDB_BASE+'/b33nnKl1GSFbao4l3fZDDqsMx0F.jpg', 'descripcion': 'Jóvenes colonizadores del espacio se enfrentan a la forma de vida más aterradora del universo.', 'duracion': 119, 'genero': 'Terror', 'anio': 2024, 'destacada': False},
    {'titulo': 'Un Mundo Imaginario', 'poster_url': TMDB_BASE+'/zOpe0eHsq0A2NvNyBbtT6sj53qV.jpg', 'descripcion': 'Una niña descubre un mundo mágico lleno de amigos imaginarios que nadie más puede ver.', 'duracion': 100, 'genero': 'Comedia', 'anio': 2024, 'destacada': False},
    {'titulo': 'Deadpool & Wolverine', 'poster_url': TMDB_BASE+'/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg', 'descripcion': 'Wade Wilson recluta a Wolverine para una misión que cambiará la historia del MCU.', 'duracion': 127, 'genero': 'Acción', 'anio': 2024, 'destacada': False},
]

peliculas_creadas = []
for data in peliculas_data:
    genero = generos.get(data.pop('genero'))
    p, created = Pelicula.objects.get_or_create(titulo=data['titulo'], defaults={**data, 'genero': genero})
    peliculas_creadas.append(p)
    if created:
        print(f"  ✓ Película: {p.titulo}")

# Funciones
now = timezone.now()
for i, p in enumerate(peliculas_creadas[:4]):
    for j in range(2):
        Funcion.objects.get_or_create(
            pelicula=p,
            fecha_hora=now + timedelta(days=j+1, hours=i*2+14),
            defaults={'sala': f'Sala {j+1}', 'asientos_totales': 80, 'precio': 18.00 + i}
        )

# Usuarios de prueba
if not Usuario.objects.filter(username='admin').exists():
    admin = Usuario.objects.create_superuser('admin', 'admin@cinema.com', 'admin1234')
    admin.rol = 'admin'
    admin.edad = 30
    admin.save()
    print("  ✓ Admin creado: admin / admin1234")

if not Usuario.objects.filter(username='cliente1').exists():
    cliente = Usuario.objects.create_user('cliente1', 'cliente@cinema.com', 'cliente123')
    cliente.edad = 25
    cliente.save()
    print("  ✓ Cliente creado: cliente1 / cliente123")

print("\n✅ Base de datos poblada correctamente.")
print("   Admin:   admin / admin1234")
print("   Cliente: cliente1 / cliente123")
