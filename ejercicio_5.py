"""
Ejercicio 5: Calculadora de Impuestos con Scope Global.

Define una tasa global TASA_IVA y funciones para calcular IVA y actualizar la tasa.
Incluye validaciones básicas para evitar usos incorrectos.
"""

from __future__ import annotations

# Tasa global de IVA (por defecto 19%)
TASA_IVA: float = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el IVA para un precio base usando la variable global TASA_IVA.

    Args:
        precio_base (float): Precio sin impuestos. Debe ser >= 0.

    Returns:
        float: Valor del IVA correspondiente al precio_base.

    Raises:
        ValueError: Si precio_base es negativo.
    """
    if precio_base < 0:
        raise ValueError("precio_base no puede ser negativo.")
    # Usamos la tasa global en tiempo de ejecución
    return round(precio_base * TASA_IVA, 10)


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza la variable global TASA_IVA.

    Args:
        nueva_tasa (float): Nueva tasa expresada como decimal (por ejemplo, 0.19).

    Raises:
        ValueError: Si nueva_tasa no está en el rango [0, 1].
    """
    global TASA_IVA
    if not (0 <= nueva_tasa <= 1):
        raise ValueError("nueva_tasa debe estar entre 0 y 1 (inclusive).")
    TASA_IVA = float(nueva_tasa)


def main() -> None:
    """
    Demostración que muestra cómo cambia el cálculo del IVA antes y después
    de actualizar la tasa global.
    """
    precios = [100.0, 49.99, 0.0]
    print("TASA_IVA inicial:", TASA_IVA)
    for p in precios:
        print(f"Precio: {p} -> IVA: {calcular_iva(p)}")

    print("\nActualizando tasa a 0.10 (10%)...\n")
    actualizar_tasa_iva(0.10)
    print("TASA_IVA actual:", TASA_IVA)
    for p in precios:
        print(f"Precio: {p} -> IVA: {calcular_iva(p)}")


if __name__ == "__main__":
    main()
