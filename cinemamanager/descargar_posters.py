"""
descargar_posters.py
Descarga los posters de TMDB y los guarda localmente en media/peliculas/
Uso: python descargar_posters.py
"""
import os, sys, django, urllib.request, ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemamanager.settings')
django.setup()

from peliculas.models import Pelicula
from django.conf import settings

MEDIA_DIR = os.path.join(settings.BASE_DIR, 'media', 'peliculas')
os.makedirs(MEDIA_DIR, exist_ok=True)

# Posters reales de TMDB
POSTERS = {
    'Dune: Parte Dos':       'https://image.tmdb.org/t/p/w500/cdqLnri3NEGcmfnqwk2TSIYtddg.jpg',
    'Oppenheimer':           'https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg',
    'Pobres Criaturas':      'https://image.tmdb.org/t/p/w500/kCGlIMHnOm8JPXNbpUntpiadaAN.jpg',
    'Godzilla x Kong':       'https://image.tmdb.org/t/p/w500/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg',
    'Inside Out 2':          'https://image.tmdb.org/t/p/w500/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg',
    'Alien: Romulus':        'https://image.tmdb.org/t/p/w500/b33nnKl1GSFbao4l3fZDDqsMx0F.jpg',
    'Un Mundo Imaginario':   'https://image.tmdb.org/t/p/w500/zOpe0eHsq0A2NvNyBbtT6sj53qV.jpg',
    'Deadpool & Wolverine':  'https://image.tmdb.org/t/p/w500/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg',
}

# SSL sin verificar (para evitar errores de certificado en Windows)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for titulo, url in POSTERS.items():
    try:
        p = Pelicula.objects.get(titulo=titulo)
        filename = f"{titulo.lower().replace(' ', '_').replace(':', '').replace('&', 'y')}.jpg"
        filepath = os.path.join(MEDIA_DIR, filename)

        if not os.path.exists(filepath):
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx) as r, open(filepath, 'wb') as f:
                f.write(r.read())
            print(f"  ✓ Descargado: {filename}")
        else:
            print(f"  ○ Ya existe:  {filename}")

        # Guardar ruta relativa en el campo imagen
        p.imagen = f"peliculas/{filename}"
        p.save()
        print(f"    → Guardado en DB: {p.titulo}")

    except Pelicula.DoesNotExist:
        print(f"  ✗ No encontrada en DB: {titulo}")
    except Exception as e:
        print(f"  ✗ Error en {titulo}: {e}")

print("\n✅ Listo. Reinicia el servidor y recarga la página.")
