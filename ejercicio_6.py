"""
Ejercicio 6: Procesamiento de Datos con map y lambda.

Este módulo aplica programación funcional para procesar una lista de productos,
utilizando `map()` y `lambda` para generar una nueva lista con los precios que
incluyen un descuento del 10%.

Conceptos aplicados:
- Programación funcional
- map()
- lambda
- Trabajo con diccionarios
"""

from typing import List, Dict


def aplicar_descuento(productos: List[Dict[str, float]]) -> List[float]:
    """
    Aplica un descuento del 10% a los precios de una lista de productos usando map() y lambda.

    Args:
        productos (List[Dict[str, float]]): Lista de diccionarios con las claves "nombre" y "precio".

    Returns:
        List[float]: Lista de precios con el 10% de descuento aplicado.
    """
    return list(map(lambda p: round(p["precio"] * 0.9, 2), productos))


def main() -> None:
    """
    Función principal que demuestra el uso de `aplicar_descuento`.
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
    ]

    print("Productos originales:")
    for p in productos:
        print(f"- {p['nombre']}: ${p['precio']:,}")

    precios_descuento = aplicar_descuento(productos)

    print("\nPrecios con 10% de descuento:")
    for precio in precios_descuento:
        print(f"- ${precio:,.2f}")


if __name__ == "__main__":
    main()
