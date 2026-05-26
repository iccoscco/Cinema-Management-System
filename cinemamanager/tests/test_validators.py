"""
tests/test_validators.py — CinemaManager
=========================================
Pruebas Black Box: Partición de Equivalencia (PE) y Análisis de Valores Límite (AVL)
para todos los validadores del sistema.
"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validators import (
    validar_edad, validar_password, validar_duracion,
    validar_rating, validar_cantidad_entradas, validar_comentario,
    validar_fecha_funcion,
    validar_anio_pelicula,
)

# =========================================
#  EDAD  (13 <= edad <= 100)

class TestEdadPE:
    @pytest.mark.parametrize("edad", [13, 20, 50, 100])
    def test_clase_valida(self, edad):
        assert validar_edad(edad) == "Edad válida"

    @pytest.mark.parametrize("edad", [-1, 0, 12])
    def test_clase_invalida_baja(self, edad):
        with pytest.raises(ValueError):
            validar_edad(edad)

    @pytest.mark.parametrize("edad", [101, 150, 999])
    def test_clase_invalida_alta(self, edad):
        with pytest.raises(ValueError):
            validar_edad(edad)

    @pytest.mark.parametrize("edad", ["veinte", 20.5, None])
    def test_tipo_incorrecto(self, edad):
        with pytest.raises(TypeError):
            validar_edad(edad)


class TestEdadAVL:
    @pytest.mark.parametrize("edad, esperado", [
        (13,  "Edad válida"),
        (14,  "Edad válida"),
        (99,  "Edad válida"),
        (100, "Edad válida"),
    ])
    def test_limites_validos(self, edad, esperado):
        assert validar_edad(edad) == esperado

    @pytest.mark.parametrize("edad", [12, 101])
    def test_limites_invalidos(self, edad):
        with pytest.raises(ValueError):
            validar_edad(edad)


# =========================================
#  PASSWORD  (len >= 8)

class TestPasswordPE:
    @pytest.mark.parametrize("password", ["abcd1234", "password!", "superclave99"])
    def test_clase_valida(self, password):
        assert validar_password(password) == "Contraseña válida"

    @pytest.mark.parametrize("password", ["", "abc", "1234567"])
    def test_clase_invalida_corta(self, password):
        with pytest.raises(ValueError):
            validar_password(password)

    @pytest.mark.parametrize("password", [12345678, None, ["abc"]])
    def test_tipo_incorrecto(self, password):
        with pytest.raises(TypeError):
            validar_password(password)


class TestPasswordAVL:
    def test_siete_chars_falla(self):
        with pytest.raises(ValueError):
            validar_password("abcd123")

    def test_ocho_chars_exacto(self):
        assert validar_password("abcd1234") == "Contraseña válida"

    def test_nueve_chars_pasa(self):
        assert validar_password("abcd12345") == "Contraseña válida"


# =========================================
#  DURACIÓN  (60 <= minutos <= 300)

class TestDuracionPE:
    @pytest.mark.parametrize("minutos", [60, 90, 120, 300])
    def test_clase_valida(self, minutos):
        assert validar_duracion(minutos) == "Duración válida"

    @pytest.mark.parametrize("minutos", [0, 30, 59])
    def test_clase_invalida_baja(self, minutos):
        with pytest.raises(ValueError):
            validar_duracion(minutos)

    @pytest.mark.parametrize("minutos", [301, 400, 999])
    def test_clase_invalida_alta(self, minutos):
        with pytest.raises(ValueError):
            validar_duracion(minutos)

    @pytest.mark.parametrize("minutos", ["noventa", 90.5, None])
    def test_tipo_incorrecto(self, minutos):
        with pytest.raises(TypeError):
            validar_duracion(minutos)


class TestDuracionAVL:
    @pytest.mark.parametrize("minutos, esperado", [
        (60,  "Duración válida"),
        (61,  "Duración válida"),
        (299, "Duración válida"),
        (300, "Duración válida"),
    ])
    def test_limites_validos(self, minutos, esperado):
        assert validar_duracion(minutos) == esperado

    @pytest.mark.parametrize("minutos", [59, 301])
    def test_limites_invalidos(self, minutos):
        with pytest.raises(ValueError):
            validar_duracion(minutos)


# =========================================
#  RATING  (1 <= rating <= 5)

class TestRatingPE:
    @pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
    def test_clase_valida(self, rating):
        assert validar_rating(rating) == "Rating válido"

    @pytest.mark.parametrize("rating", [-1, 0])
    def test_clase_invalida_baja(self, rating):
        with pytest.raises(ValueError):
            validar_rating(rating)

    @pytest.mark.parametrize("rating", [6, 10, 100])
    def test_clase_invalida_alta(self, rating):
        with pytest.raises(ValueError):
            validar_rating(rating)

    @pytest.mark.parametrize("rating", ["cinco", 3.5, None])
    def test_tipo_incorrecto(self, rating):
        with pytest.raises(TypeError):
            validar_rating(rating)


class TestRatingAVL:
    @pytest.mark.parametrize("rating, esperado", [
        (1, "Rating válido"),
        (2, "Rating válido"),
        (4, "Rating válido"),
        (5, "Rating válido"),
    ])
    def test_limites_validos(self, rating, esperado):
        assert validar_rating(rating) == esperado

    @pytest.mark.parametrize("rating", [0, 6])
    def test_limites_invalidos(self, rating):
        with pytest.raises(ValueError):
            validar_rating(rating)


# =========================================
#  ENTRADAS  (1 <= cantidad <= 10)

class TestEntradasPE:
    @pytest.mark.parametrize("cantidad", [1, 5, 10])
    def test_clase_valida(self, cantidad):
        assert validar_cantidad_entradas(cantidad) == "Cantidad válida"

    @pytest.mark.parametrize("cantidad", [-1, 0])
    def test_clase_invalida_baja(self, cantidad):
        with pytest.raises(ValueError):
            validar_cantidad_entradas(cantidad)

    @pytest.mark.parametrize("cantidad", [11, 50, 999])
    def test_clase_invalida_alta(self, cantidad):
        with pytest.raises(ValueError):
            validar_cantidad_entradas(cantidad)

    @pytest.mark.parametrize("cantidad", ["cinco", 5.5, None])
    def test_tipo_incorrecto(self, cantidad):
        with pytest.raises(TypeError):
            validar_cantidad_entradas(cantidad)


class TestEntradasAVL:
    @pytest.mark.parametrize("cantidad, esperado", [
        (1,  "Cantidad válida"),
        (2,  "Cantidad válida"),
        (9,  "Cantidad válida"),
        (10, "Cantidad válida"),
    ])
    def test_limites_validos(self, cantidad, esperado):
        assert validar_cantidad_entradas(cantidad) == esperado

    @pytest.mark.parametrize("cantidad", [0, 11])
    def test_limites_invalidos(self, cantidad):
        with pytest.raises(ValueError):
            validar_cantidad_entradas(cantidad)


# =========================================
#  COMENTARIO  (1 <= len <= 500)

class TestComentarioPE:
    @pytest.mark.parametrize("texto", ["Buena película", "Excelente, muy recomendada!"])
    def test_clase_valida(self, texto):
        assert validar_comentario(texto) == "Comentario válido"

    @pytest.mark.parametrize("texto", ["", "   "])
    def test_clase_invalida_vacia(self, texto):
        with pytest.raises(ValueError):
            validar_comentario(texto)

    def test_clase_invalida_muy_largo(self):
        with pytest.raises(ValueError):
            validar_comentario("x" * 501)

    @pytest.mark.parametrize("texto", [123, None, ["comentario"]])
    def test_tipo_incorrecto(self, texto):
        with pytest.raises(TypeError):
            validar_comentario(texto)


class TestComentarioAVL:
    @pytest.mark.parametrize("texto, esperado", [
        ("x",       "Comentario válido"),
        ("xx",      "Comentario válido"),
        ("x" * 499, "Comentario válido"),
        ("x" * 500, "Comentario válido"),
    ])
    def test_limites_validos(self, texto, esperado):
        assert validar_comentario(texto) == esperado

    @pytest.mark.parametrize("texto", ["", "x" * 501])
    def test_limites_invalidos(self, texto):
        with pytest.raises(ValueError):
            validar_comentario(texto)


# =========================================
#  FECHA FUNCIÓN  (fecha > ahora exacto)

from datetime import datetime as _dt, timedelta as _td


class TestFechaFuncionPE:
    """Partición de Equivalencia para fecha/hora de función."""

    @pytest.mark.parametrize("delta", [
        _td(hours=1), _td(days=1), _td(days=30), _td(days=365)
    ])
    def test_clase_valida_futura(self, delta):
        """CE1 — Clase válida: fecha futura al momento actual."""
        fecha = _dt.now() + delta
        assert validar_fecha_funcion(fecha) == "Fecha válida"

    @pytest.mark.parametrize("delta", [
        _td(days=-1), _td(days=-30), _td(days=-365)
    ])
    def test_clase_invalida_pasada(self, delta):
        """CE2 — Clase inválida: fecha pasada → lanza ValueError."""
        fecha = _dt.now() + delta
        with pytest.raises(ValueError):
            validar_fecha_funcion(fecha)

    @pytest.mark.parametrize("fecha", ["2027-01-01", 20270101, None])
    def test_tipo_incorrecto(self, fecha):
        """CE3 — Tipo incorrecto → lanza TypeError."""
        with pytest.raises(TypeError):
            validar_fecha_funcion(fecha)


class TestFechaFuncionAVL:
    """Análisis de Valores Límite para fecha de función."""

    def test_un_segundo_futuro(self):
        """Frontera mínima práctica: 1 segundo en el futuro → válido."""
        assert validar_fecha_funcion(_dt.now() + _td(seconds=2)) == "Fecha válida"

    def test_un_dia_futuro(self):
        """1 día en el futuro → válido."""
        assert validar_fecha_funcion(_dt.now() + _td(days=1)) == "Fecha válida"

    def test_un_segundo_pasado(self):
        """1 segundo en el pasado → inválido."""
        with pytest.raises(ValueError):
            validar_fecha_funcion(_dt.now() - _td(seconds=1))

    def test_un_dia_pasado(self):
        """1 día en el pasado → inválido."""
        with pytest.raises(ValueError):
            validar_fecha_funcion(_dt.now() - _td(days=1))


# =========================================
#  AÑO PELÍCULA  (anio <= año actual)

_ANIO_ACTUAL = _dt.now().year


class TestAnioPeliculaPE:
    """Partición de Equivalencia para año de estreno de película."""

    @pytest.mark.parametrize("anio", [_ANIO_ACTUAL, _ANIO_ACTUAL - 1, 2000, 1950])
    def test_clase_valida(self, anio):
        """CE1 — Clase válida: anio <= año actual."""
        assert validar_anio_pelicula(anio) == "Año de película válido"

    @pytest.mark.parametrize("anio", [_ANIO_ACTUAL + 1, _ANIO_ACTUAL + 5, 2099])
    def test_clase_invalida_futuro(self, anio):
        """CE2 — Clase inválida: año futuro → lanza ValueError."""
        with pytest.raises(ValueError):
            validar_anio_pelicula(anio)

    @pytest.mark.parametrize("anio", ["2024", 2024.0, None])
    def test_tipo_incorrecto(self, anio):
        """CE3 — Tipo incorrecto → lanza TypeError."""
        with pytest.raises(TypeError):
            validar_anio_pelicula(anio)


class TestAnioPeliculaAVL:
    """Análisis de Valores Límite para año de película (frontera = año actual)."""

    def test_anio_actual_exacto(self):
        """Frontera superior exacta → válido."""
        assert validar_anio_pelicula(_ANIO_ACTUAL) == "Año de película válido"

    def test_anio_anterior(self):
        """Frontera - 1 → válido."""
        assert validar_anio_pelicula(_ANIO_ACTUAL - 1) == "Año de película válido"

    def test_anio_siguiente(self):
        """Frontera + 1 (futuro) → inválido."""
        with pytest.raises(ValueError):
            validar_anio_pelicula(_ANIO_ACTUAL + 1)

    def test_anio_muy_futuro(self):
        """Año muy en el futuro → inválido."""
        with pytest.raises(ValueError):
            validar_anio_pelicula(2099)
