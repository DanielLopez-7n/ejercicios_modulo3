"""
Pruebas unitarias para el Ejercicio 6: Procesamiento de Datos con map y lambda.
"""

from ejercicio_6 import aplicar_descuento


def test_aplicar_descuento_basico() -> None:
    """Verifica que se aplique correctamente el 10% de descuento."""
    productos = [
        {"nombre": "Camisa", "precio": 100.0},
        {"nombre": "Pantalón", "precio": 200.0},
    ]
    resultado = aplicar_descuento(productos)
    assert resultado == [90.0, 180.0]


def test_aplicar_descuento_redondeo() -> None:
    """Verifica que los precios se redondeen correctamente a dos decimales."""
    productos = [{"nombre": "Zapatos", "precio": 99.99}]
    resultado = aplicar_descuento(productos)
    assert resultado == [89.99]


def test_aplicar_descuento_lista_vacia() -> None:
    """Si la lista está vacía, debe devolver una lista vacía."""
    assert aplicar_descuento([]) == []
