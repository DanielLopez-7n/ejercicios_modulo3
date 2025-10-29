"""
Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions.

Este módulo procesa un texto para extraer palabras con más de 5 letras
en mayúsculas, y luego genera un diccionario con la longitud de cada palabra.

Conceptos aplicados:
- List Comprehensions
- Dictionary Comprehensions
- Métodos de string (split, upper)
"""

from typing import List, Dict


def palabras_mayores_a_5(texto: str) -> List[str]:
    """
    Devuelve una lista de palabras del texto que tengan más de 5 letras, en mayúsculas.

    Args:
        texto (str): Texto de entrada.

    Returns:
        List[str]: Lista de palabras con más de 5 letras, convertidas a mayúsculas.
    """
    return [palabra.upper() for palabra in texto.split() if len(palabra) > 5]


def longitud_palabras(palabras: List[str]) -> Dict[str, int]:
    """
    Devuelve un diccionario con la longitud de cada palabra de la lista dada.

    Args:
        palabras (List[str]): Lista de palabras.

    Returns:
        Dict[str, int]: Diccionario donde la clave es la palabra y el valor su longitud.
    """
    return {palabra: len(palabra) for palabra in palabras}


def main() -> None:
    """
    Función principal que demuestra el uso de las funciones del ejercicio.
    """
    texto = (
        "La programación funcional favorece la inmutabilidad y el uso de expresiones "
        "como map, filter y comprehensions."
    )

    print("Texto original:")
    print(texto)

    palabras_filtradas = palabras_mayores_a_5(texto)
    print("\nPalabras con más de 5 letras (mayúsculas):")
    print(palabras_filtradas)

    longitudes = longitud_palabras(palabras_filtradas)
    print("\n📏 Longitud de cada palabra:")
    for palabra, longitud in longitudes.items():
        print(f"{palabra}: {longitud}")


if __name__ == "__main__":
    main()
