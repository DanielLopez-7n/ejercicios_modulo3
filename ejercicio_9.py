"""
Ejercicio 9: Sumatoria con functools.reduce.

Este módulo utiliza la función `reduce` para:
1. Calcular la suma total de una lista de números.
2. Concatenar una lista de strings en una sola frase.

Conceptos aplicados:
- functools.reduce
- lambda
"""

from functools import reduce
from typing import List


def sumar_lista(numeros: List[int]) -> int:
    """
    Calcula la suma total de una lista de números usando functools.reduce.

    Args:
        numeros (List[int]): Lista de números enteros.

    Returns:
        int: La suma total de todos los números en la lista.
    """
    return reduce(lambda a, b: a + b, numeros, 0)


def concatenar_textos(textos: List[str]) -> str:
    """
    Concatena una lista de strings en una sola frase usando functools.reduce.

    Args:
        textos (List[str]): Lista de cadenas de texto.

    Returns:
        str: Una cadena resultante de concatenar todos los textos.
    """
    return reduce(lambda a, b: a + b, textos, "")


def main() -> None:
    """
    Función principal que demuestra el uso de `reduce` para sumar y concatenar.
    """
    numeros = [1, 2, 3, 4, 5]
    textos = ["Hola", " ", "SENA", "!"]

    suma = sumar_lista(numeros)
    frase = concatenar_textos(textos)

    print("Lista de números:", numeros)
    print(f" Suma total: {suma}")

    print("\nLista de textos:", textos)
    print(f"Frase concatenada: {frase}")


if __name__ == "__main__":
    main()
