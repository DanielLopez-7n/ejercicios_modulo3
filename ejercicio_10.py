"""
Ejercicio 10: Explorador de Estructuras de Datos Recursivo.

Este módulo implementa una función recursiva que recorre estructuras de datos
anidadas (listas, tuplas, diccionarios, etc.) e imprime los valores no iterables
junto con su nivel de profundidad.

Conceptos aplicados:
- Recursividad
- isinstance()
- Type Hinting (Any)
"""

from typing import Any


def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente estructuras anidadas e imprime cada valor no iterable
    junto a su profundidad en la estructura.

    Args:
        elemento (Any): Estructura de datos a explorar (lista, diccionario, etc.).
        profundidad (int): Nivel actual de profundidad (por defecto es 1).

    Returns:
        None
    """
    # Caso base: si el elemento no es iterable (str, int, float, bool, None)
    if isinstance(elemento, (int, float, str, bool)) or elemento is None:
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
        return

    # Si es un diccionario, recorrer claves y valores
    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)

    # Si es una lista o tupla, recorrer cada elemento
    elif isinstance(elemento, (list, tuple, set)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)

    # Si es cualquier otro tipo (como un objeto desconocido)
    else:
        print(f"Valor desconocido: {elemento}, Profundidad: {profundidad}")


def main() -> None:
    """
    Función principal que demuestra el funcionamiento del explorador recursivo.
    """
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]

    print("Explorando estructura:")
    explorar_estructura(estructura)


if __name__ == "__main__":
    main()
