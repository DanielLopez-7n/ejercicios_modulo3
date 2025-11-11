"""
Pruebas unitarias para el Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions.
"""

from ejercicio_8 import palabras_mayores_a_5, longitud_palabras


def test_palabras_mayores_a_5_basico() -> None:
    """Debe devolver solo las palabras con más de 5 letras en mayúsculas."""
    texto = "Hola mundo programación funcional increíble"
    resultado = palabras_mayores_a_5(texto)
    assert resultado == ["PROGRAMACIÓN", "FUNCIONAL", "INCREÍBLE"]


def test_palabras_mayores_a_5_vacio() -> None:
    """Si el texto no contiene palabras mayores a 5 letras, devuelve una lista vacía."""
    texto = "sol mar pez ave"
    resultado = palabras_mayores_a_5(texto)
    assert resultado == []


def test_longitud_palabras_correcto() -> None:
    """Verifica que el diccionario asigne correctamente las longitudes."""
    palabras = ["PROGRAMACIÓN", "FUNCIONAL"]
    resultado = longitud_palabras(palabras)
    assert resultado == {"PROGRAMACIÓN": 12, "FUNCIONAL": 9}


def test_longitud_palabras_vacia() -> None:
    """Debe devolver un diccionario vacío si la lista está vacía."""
    assert longitud_palabras([]) == {}


def test_integracion_lista_y_diccionario() -> None:
    """Verifica que ambas funciones trabajen correctamente en conjunto."""
    texto = "El aprendizaje constante mejora la habilidad"
    palabras = palabras_mayores_a_5(texto)
    diccionario = longitud_palabras(palabras)
    assert diccionario == {
        "APRENDIZAJE": 11,
        "CONSTANTE": 9,
        "MEJORA": 6,
        "HABILIDAD": 9,
    }
