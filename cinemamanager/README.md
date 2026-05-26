# CinemaManager 🎬

Sistema de gestión de cine desarrollado con **Django + Python**.  
Proyecto para la actividad académica **"Guerra de Testers"**.

---

## Instalación rápida

```bash
# 1. Instalar dependencias
pip install django pillow pytest pytest-django

# 2. Aplicar migraciones
python manage.py migrate

# 3. Cargar datos de ejemplo
python populate_db.py

# 4. Ejecutar servidor
python manage.py runserver
```

Abrir http://127.0.0.1:8000

---

## Cuentas de prueba

| Usuario    | Contraseña   | Rol          |
|------------|--------------|--------------|
| `admin`    | `admin1234`  | Administrador |
| `cliente1` | `cliente123` | Cliente      |

---

## Ejecutar pruebas (PE y AVL)

```bash
python -m pytest tests/test_validators.py -v
```

---

## Restricciones del sistema

| Campo              | Restricción       |
|--------------------|-------------------|
| Edad               | 13 ≤ edad ≤ 100   |
| Contraseña         | mínimo 8 chars    |
| Duración película  | 60 ≤ min ≤ 300    |
| Rating             | 1 ≤ rating ≤ 5    |
| Entradas por compra| 1 ≤ cant ≤ 10     |
| Comentario         | 1 ≤ chars ≤ 500   |

---

## Estructura del proyecto

```
cinemamanager/
├── cinemamanager/       # Configuración Django
├── usuarios/            # App: registro, login, perfil
├── peliculas/           # App: catálogo, detalle, comentarios
├── entradas/            # App: compra de entradas, funciones
├── templates/           # Plantillas HTML
├── static/css/          # Estilos (morado neón + blanco)
├── validators.py        # Validadores centrales del sistema
├── tests/
│   └── test_validators.py   # 100 pruebas PE + AVL
├── populate_db.py       # Script para cargar datos de prueba
└── manage.py
```
