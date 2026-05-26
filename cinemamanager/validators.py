"""
validators.py — CinemaManager
Validaciones centrales del sistema. Diseñadas para PE y AVL.
"""


# ─────────────────────────────────────────────
#  USUARIOS
# ─────────────────────────────────────────────

def validar_edad(edad: int) -> str:
    """
    Valida que la edad esté en el rango permitido [13, 100].

    Restricción: 13 <= edad <= 100

    Raises:
        TypeError: si edad no es un entero.
        ValueError: si edad está fuera del rango permitido.
    """
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 13 or edad > 100:
        raise ValueError(f"Edad fuera de rango permitido (13-100). Recibido: {edad}")
    return "Edad válida"


def validar_password(password: str) -> str:
    """
    Valida que la contraseña tenga al menos 8 caracteres.

    Restricción: len(password) >= 8

    Raises:
        TypeError: si password no es str.
        ValueError: si la contraseña es demasiado corta.
    """
    if not isinstance(password, str):
        raise TypeError("La contraseña debe ser una cadena de texto.")
    if len(password) < 8:
        raise ValueError(
            f"Contraseña muy corta. Mínimo 8 caracteres. Recibido: {len(password)}"
        )
    return "Contraseña válida"


# ─────────────────────────────────────────────
#  PELÍCULAS
# ─────────────────────────────────────────────

def validar_duracion(minutos: int) -> str:
    """
    Valida que la duración de una película esté en [60, 300] minutos.

    Restricción: 60 <= minutos <= 300

    Raises:
        TypeError: si minutos no es entero.
        ValueError: si está fuera del rango.
    """
    if not isinstance(minutos, int):
        raise TypeError("La duración debe ser un número entero de minutos.")
    if minutos < 60 or minutos > 300:
        raise ValueError(
            f"Duración fuera de rango (60-300 min). Recibido: {minutos}"
        )
    return "Duración válida"


def validar_rating(rating: int) -> str:
    """
    Valida que el rating de una película esté en [1, 5].

    Restricción: 1 <= rating <= 5

    Raises:
        TypeError: si rating no es entero.
        ValueError: si está fuera del rango.
    """
    if not isinstance(rating, int):
        raise TypeError("El rating debe ser un número entero.")
    if rating < 1 or rating > 5:
        raise ValueError(
            f"Rating fuera de rango permitido (1-5). Recibido: {rating}"
        )
    return "Rating válido"


# ─────────────────────────────────────────────
#  ENTRADAS
# ─────────────────────────────────────────────

def validar_cantidad_entradas(cantidad: int) -> str:
    """
    Valida que la cantidad de entradas a comprar esté en [1, 10].

    Restricción: 1 <= cantidad <= 10

    Raises:
        TypeError: si cantidad no es entero.
        ValueError: si está fuera del rango.
    """
    if not isinstance(cantidad, int):
        raise TypeError("La cantidad de entradas debe ser un número entero.")
    if cantidad < 1 or cantidad > 10:
        raise ValueError(
            f"Cantidad de entradas fuera de rango (1-10). Recibido: {cantidad}"
        )
    return "Cantidad válida"


# ─────────────────────────────────────────────
#  COMENTARIOS
# ─────────────────────────────────────────────

def validar_comentario(texto: str) -> str:
    """
    Valida que un comentario tenga entre 1 y 500 caracteres.

    Restricción: 1 <= len(texto) <= 500

    Raises:
        TypeError: si texto no es str.
        ValueError: si está fuera del rango.
    """
    if not isinstance(texto, str):
        raise TypeError("El comentario debe ser una cadena de texto.")
    largo = len(texto.strip())
    if largo < 1 or largo > 500:
        raise ValueError(
            f"Comentario fuera de rango (1-500 caracteres). Recibido: {largo}"
        )
    return "Comentario válido"


# ─────────────────────────────────────────────
#  FUNCIONES / HORARIOS
# ─────────────────────────────────────────────

def validar_fecha_funcion(fecha) -> str:
    """
    Valida que la fecha/hora de una función sea estrictamente futura (mayor al momento actual).

    Restricción: fecha > datetime.now()

    Raises:
        TypeError: si fecha no es un objeto datetime.
        ValueError: si la fecha es en el pasado o presente.
    """
    from datetime import datetime
    if not isinstance(fecha, datetime):
        raise TypeError("La fecha debe ser un objeto datetime.")
    if fecha <= datetime.now():
        raise ValueError(
            f"La fecha de la función debe ser futura. Recibido: {fecha.strftime('%d/%m/%Y %H:%M')}"
        )
    return "Fecha válida"


def validar_anio_pelicula(anio: int) -> str:
    """
    Valida que el año de estreno de una película no sea futuro.

    Restricción: anio <= año actual

    Raises:
        TypeError: si anio no es un entero.
        ValueError: si el año es mayor al año actual.
    """
    from datetime import datetime
    if not isinstance(anio, int):
        raise TypeError("El año debe ser un número entero.")
    anio_actual = datetime.now().year
    if anio > anio_actual:
        raise ValueError(
            f"El año de estreno no puede ser futuro (máximo {anio_actual}). Recibido: {anio}"
        )
    return "Año de película válido"
