"""
Pruebas unitarias para el Ejercicio 9: Sumatoria con reduce.
"""

from ejercicio_9 import sumar_lista, concatenar_textos


def test_sumar_lista_basico() -> None:
    """Debe calcular correctamente la suma de una lista de enteros."""
    assert sumar_lista([1, 2, 3, 4, 5]) == 15


def test_sumar_lista_vacia() -> None:
    """Si la lista está vacía, debe devolver 0."""
    assert sumar_lista([]) == 0


def test_sumar_lista_negativos_y_positivos() -> None:
    """Debe manejar correctamente números negativos y positivos."""
    assert sumar_lista([-2, 5, -3, 10]) == 10


def test_concatenar_textos_basico() -> None:
    """Debe concatenar correctamente los textos de la lista."""
    assert concatenar_textos(["Hola", " ", "SENA", "!"]) == "Hola SENA!"


def test_concatenar_textos_vacio() -> None:
    """Si la lista está vacía, debe devolver una cadena vacía."""
    assert concatenar_textos([]) == ""


def test_concatenar_textos_con_espacios() -> None:
    """Verifica que respete los espacios en la concatenación."""
    assert concatenar_textos(["Hola", " ", "Mundo"]) == "Hola Mundo"
