import pytest

from ejercicio_1 import calcular_imc, interpretar_imc


def test_calcular_imc():
    # Casos de prueba con datos conocidos
    assert calcular_imc(70, 1.75) == pytest.approx(22.857142857142858, rel=1e-9)
    assert calcular_imc(50, 1.60) == pytest.approx(19.53125, rel=1e-9)
    assert calcular_imc(100, 1.80) == pytest.approx(30.864197530864197, rel=1e-9)


def test_interpreter_imc():
    # Casos de prueba para diferentes valores de IMC
    assert interpretar_imc(16.0) == "Bajo peso"  # IMC bajo
    assert interpretar_imc(22.0) == "Normal"  # IMC normal
    assert interpretar_imc(27.0) == "Sobrepeso"  # IMC sobrepeso
    assert interpretar_imc(35.0) == "Obesidad"  # IMC obesidad
