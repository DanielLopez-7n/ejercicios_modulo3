import os
import json
import pytest
from ejercicio_13 import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
)

# ---------- CONFIGURACIÓN ----------
ARCHIVO_PRUEBA = "inventario_test.json"


@pytest.fixture(autouse=True)
def preparar_archivo():
    """Crea un archivo JSON temporal antes de cada prueba y lo elimina al final."""
    inventario_inicial = [
        {"nombre": "Teclado", "cantidad": 10, "precio": 50000},
        {"nombre": "Mouse", "cantidad": 5, "precio": 30000},
    ]
    with open(ARCHIVO_PRUEBA, "w", encoding="utf-8") as f:
        json.dump(inventario_inicial, f, indent=4)

    yield  # Aquí se ejecutan las pruebas

    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)


# ---------- PRUEBAS ----------


def test_cargar_inventario():
    inventario = cargar_inventario(ARCHIVO_PRUEBA)
    assert isinstance(inventario, list)
    assert len(inventario) == 2
    assert inventario[0]["nombre"] == "Teclado"


def test_guardar_inventario():
    inventario = [{"nombre": "Monitor", "cantidad": 3, "precio": 250000}]
    guardar_inventario(inventario, ARCHIVO_PRUEBA)

    with open(ARCHIVO_PRUEBA, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data[0]["nombre"] == "Monitor"
    assert data[0]["cantidad"] == 3


def test_agregar_producto():
    inventario = cargar_inventario(ARCHIVO_PRUEBA)
    inventario = agregar_producto(inventario, "Audífonos", 8, 45000)

    assert any(p["nombre"] == "Audífonos" for p in inventario)

    # Se guarda y se verifica persistencia
    guardar_inventario(inventario, ARCHIVO_PRUEBA)
    with open(ARCHIVO_PRUEBA, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert any(p["nombre"] == "Audífonos" for p in data)


def test_vender_producto():
    inventario = cargar_inventario(ARCHIVO_PRUEBA)
    inventario = vender_producto(inventario, "Mouse", 2)

    producto = next((p for p in inventario if p["nombre"] == "Mouse"), None)
    assert producto is not None
    assert producto["cantidad"] == 3  # 5 - 2 = 3

    # Caso venta mayor que stock
    inventario = vender_producto(inventario, "Mouse", 10)
    producto = next((p for p in inventario if p["nombre"] == "Mouse"), None)
    assert producto["cantidad"] == 3  # No debe cambiar si no hay suficiente stock


def test_vender_producto_inexistente():
    inventario = cargar_inventario(ARCHIVO_PRUEBA)
    inventario_modificado = vender_producto(inventario, "Impresora", 1)
    assert inventario_modificado == inventario  # No debe alterar si no existe


def test_archivo_inexistente():
    if os.path.exists("no_existe.json"):
        os.remove("no_existe.json")

    inventario = cargar_inventario("no_existe.json")
    assert inventario == []  # Debe retornar lista vacía si no existe
