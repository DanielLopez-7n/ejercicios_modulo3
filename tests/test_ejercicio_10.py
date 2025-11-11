"""
Pruebas unitarias para el Ejercicio 10: Explorador de Estructuras de Datos Recursivo.
"""

from io import StringIO
from contextlib import redirect_stdout
from ejercicio_10 import explorar_estructura


def capturar_salida(func, *args, **kwargs) -> str:
    """Captura la salida impresa de una función."""
    buffer = StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue().strip()


def test_explorar_lista_simple() -> None:
    """Verifica que explore correctamente una lista simple."""
    salida = capturar_salida(explorar_estructura, [1, 2, 3])
    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 3, Profundidad: 2" in salida


def test_explorar_diccionario_anidado() -> None:
    """Verifica que explore correctamente un diccionario anidado."""
    datos = {"a": 1, "b": {"c": 2, "d": 3}}
    salida = capturar_salida(explorar_estructura, datos)
    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 2, Profundidad: 3" in salida
    assert "Valor: 3, Profundidad: 3" in salida


def test_explorar_estructura_mixta() -> None:
    """Verifica que maneje listas y diccionarios anidados simultáneamente."""
    estructura = [1, {"x": [2, {"y": 3}]}]
    salida = capturar_salida(explorar_estructura, estructura)
    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 2, Profundidad: 4" in salida
    assert "Valor: 3, Profundidad: 5" in salida


def test_explorar_elemento_primitivo() -> None:
    """Verifica que funcione correctamente con valores primitivos."""
    salida = capturar_salida(explorar_estructura, 42)
    assert salida == "Valor: 42, Profundidad: 1"


def test_explorar_elemento_none() -> None:
    """Verifica que funcione con None."""
    salida = capturar_salida(explorar_estructura, None)
    assert salida == "Valor: None, Profundidad: 1"
