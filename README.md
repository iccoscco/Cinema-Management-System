# 🎬 CinemaManager

Sistema de gestión de cine desarrollado con **Python + Django** para la actividad académica **Guerra de Testers**.

---

## Integrantes

- Ccoscco Alvis, Italo Frankdux
- Del Castillo Montoya, Christopher Brad
- García Valdivia, Ronald Pablo
- Ordóñez Ccoriccaza, Juan Carlos


---

## Descripción

CinemaManager es una aplicación web que permite gestionar un cine completo: catálogo de películas, compra de entradas, comentarios con calificaciones y administración de funciones.

**Roles del sistema:**

| Rol | Permisos |
|-----|----------|
| Cliente | Ver catálogo, buscar películas, comprar entradas, comentar, guardar favoritos |
| Administrador | Agregar/editar/eliminar películas, crear funciones, gestionar asientos |

---

## Instalación y ejecución

### 1. Instalar dependencias
```bash
pip install django pillow pytest pytest-django
```

### 2. Aplicar migraciones
```bash
python manage.py migrate
```

### 3. Cargar datos de ejemplo
```bash
python populate_db.py
```

### 4. Iniciar el servidor
```bash
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000**

---

## Cuentas de prueba

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `admin` | `admin1234` | Administrador |
| `cliente1` | `cliente123` | Cliente |

Panel de administración: http://127.0.0.1:8000/admin/

---

## Ejecutar pruebas (PE y AVL)

```bash
python -m pytest tests/test_validators.py -v
```

> 128 pruebas automatizadas — todas en verde ✅

---

## Estructura del proyecto

```
cinemamanager/
├── manage.py
├── validators.py               ← Validadores centrales del sistema
├── populate_db.py              ← Carga datos de ejemplo
├── descargar_posters.py        ← Descarga imágenes de películas (TMDB)
├── conftest.py
├── pytest.ini
│
├── cinemamanager/              ← Configuración Django
│   ├── settings.py
│   └── urls.py
│
├── usuarios/                   ← Registro, login, perfil
├── peliculas/                  ← Catálogo, detalle, comentarios
├── entradas/                   ← Compra de entradas, funciones
│
├── templates/                  ← HTML
│   ├── base.html
│   ├── peliculas/
│   ├── usuarios/
│   └── entradas/
│
├── static/css/
│   └── style.css               ← Diseño morado neón
│
└── tests/
    └── test_validators.py      ← 128 pruebas PE + AVL
```

---

## Validaciones del sistema

| Campo | Restricción |
|-------|-------------|
| Edad | 13 ≤ edad ≤ 100 |
| Contraseña | Mínimo 8 caracteres |
| Cantidad de entradas | 1 ≤ entradas ≤ 10 |
| Rating | 1 ≤ rating ≤ 5 |
| Duración película | 60 ≤ minutos ≤ 300 |
| Año de estreno | año ≤ año actual (≤ 2026) |
| Comentario | 1 ≤ caracteres ≤ 500 |
| Fecha de función | fecha > momento actual |

---

## Tecnologías

- **Python 3.10+**
- **Django**
- **SQLite**
- **pytest + pytest-django**
- **HTML + CSS** (sin frameworks externos)

---

## Pruebas — Resumen PE y AVL

### Partición de Equivalencia (PE)
Cada campo tiene 4 clases: válida, inválida baja, inválida alta, tipo incorrecto.

### Análisis de Valores Límite (AVL)
Se prueba frontera exacta, frontera−1 y frontera+1 para cada límite.

| Campo | Límite inferior | Límite superior |
|-------|----------------|----------------|
| Edad | 13 ✓ / 12 ✗ | 100 ✓ / 101 ✗ |
| Contraseña | 8 chars ✓ / 7 ✗ | — |
| Entradas | 1 ✓ / 0 ✗ | 10 ✓ / 11 ✗ |
| Rating | 1 ✓ / 0 ✗ | 5 ✓ / 6 ✗ |
| Duración | 60 ✓ / 59 ✗ | 300 ✓ / 301 ✗ |
| Año película | — | 2026 ✓ / 2027 ✗ |
| Comentario | 1 char ✓ / 0 ✗ | 500 ✓ / 501 ✗ |
| Fecha función | ahora+1seg ✓ / ahora−1seg ✗ | — |
