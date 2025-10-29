"""
Pruebas unitarias para Ejercicio 5: Calculadora de Impuestos con Scope Global.
Cubrimos casos normales y casos borde / errores esperados.
"""

import math
import importlib
import pytest

import ejercicio_5 as ejercicio_5


def setup_function() -> None:
    """
    Antes de cada test nos aseguramos de recargar el módulo para restablecer
    la TASA_IVA global a su valor por defecto (esto evita efectos colaterales
    entre tests que modifican la variable global).
    """
    importlib.reload(ejercicio_5)


def test_calcular_iva_valor_basico() -> None:
    """Calcula IVA con la tasa por defecto (0.19)."""
    precio = 100.0
    esperado = round(precio * 0.19, 10)
    assert math.isclose(ejercicio_5.calcular_iva(precio), esperado, rel_tol=1e-9)


def test_calcular_iva_cero() -> None:
    """Precio 0 debe devolver IVA 0."""
    assert ejercicio_5.calcular_iva(0.0) == 0.0


def test_calcular_iva_precision() -> None:
    """Verifica precisión y redondeo consistente para valores con decimales."""
    precio = 49.99
    esperado = round(precio * 0.19, 10)
    assert ejercicio_5.calcular_iva(precio) == esperado


def test_calcular_iva_precio_negativo_raise() -> None:
    """Precio negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        ejercicio_5.calcular_iva(-1.0)


def test_actualizar_tasa_valida_y_efecto_global() -> None:
    """Actualizar la tasa debe afectar cálculos posteriores."""
    # Tasa por defecto
    importlib.reload(ejercicio_5)
    assert math.isclose(ejercicio_5.TASA_IVA, 0.19, rel_tol=1e-9)

    ejercicio_5.actualizar_tasa_iva(0.10)
    assert math.isclose(ejercicio_5.TASA_IVA, 0.10, rel_tol=1e-9)

    # Después de actualizar, el cálculo debe usar la nueva tasa
    assert ejercicio_5.calcular_iva(100.0) == round(100.0 * 0.10, 10)


def test_actualizar_tasa_valores_borde() -> None:
    """Probar tasas en los límites 0 y 1 (válidas según la función)."""
    importlib.reload(ejercicio_5)
    ejercicio_5.actualizar_tasa_iva(0.0)
    assert ejercicio_5.TASA_IVA == 0.0
    assert ejercicio_5.calcular_iva(50.0) == 0.0

    ejercicio_5.actualizar_tasa_iva(1.0)
    assert ejercicio_5.TASA_IVA == 1.0
    assert ejercicio_5.calcular_iva(10.0) == 10.0


def test_actualizar_tasa_invalida_raise() -> None:
    """Tasas fuera de rango deben lanzar ValueError."""
    importlib.reload(ejercicio_5)
    with pytest.raises(ValueError):
        ejercicio_5.actualizar_tasa_iva(-0.1)

    with pytest.raises(ValueError):
        ejercicio_5.actualizar_tasa_iva(1.5)
