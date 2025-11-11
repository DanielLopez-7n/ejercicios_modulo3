"""
Pruebas unitarias para el Ejercicio 4: Validador de Datos Genérico.
"""

from ejercicio_4 import (
    aplicar_validador,
    es_email_valido,
    es_mayor_a_10,
)


def test_es_email_valido_correctos() -> None:
    """Prueba correos válidos."""
    emails = ["ana@mail.com", "pepe@hotmail.es", "test@gmail.co"]
    for correo in emails:
        assert es_email_valido(correo) is True


def test_es_email_valido_incorrectos() -> None:
    """Prueba correos inválidos."""
    emails = ["pepe@", "carla", "juanmail.com", "correo@sinpunto"]
    for correo in emails:
        assert es_email_valido(correo) is False


def test_es_mayor_a_10_correctos() -> None:
    """Verifica que los números mayores a 10 sean válidos."""
    numeros = [11, 20, 100]
    for n in numeros:
        assert es_mayor_a_10(n) is True


def test_es_mayor_a_10_incorrectos() -> None:
    """Verifica que los números menores o iguales a 10 sean inválidos."""
    numeros = [10, 5, 0, -3]
    for n in numeros:
        assert es_mayor_a_10(n) is False


def test_aplicar_validador_con_emails() -> None:
    """Comprueba que aplicar_validador funcione con validador de emails."""
    datos = ["ana@mail.com", "pepe@", "carla@gmail.com", "juanmail.com"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["ana@mail.com", "carla@gmail.com"]


def test_aplicar_validador_con_numeros() -> None:
    """Comprueba que aplicar_validador funcione con validador de números."""
    datos = [3, 15, 8, 22, 10]
    resultado = aplicar_validador(datos, es_mayor_a_10)
    assert resultado == [15, 22]
