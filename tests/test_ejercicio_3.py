"""Pruebas unitarias para el ejercicio 3 (Contador con Closure)."""

from ejercicio_3 import crear_contador


def test_contador_incrementa_correctamente():
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3


def test_contadores_independientes():
    contador1 = crear_contador()
    contador2 = crear_contador()

    assert contador1() == 1
    assert contador1() == 2
    assert contador2() == 1  # Debe empezar desde cero, independiente
    assert contador1() == 3
    assert contador2() == 2
