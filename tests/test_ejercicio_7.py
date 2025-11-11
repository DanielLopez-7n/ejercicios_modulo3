"""
Pruebas unitarias para el Ejercicio 7: Filtrado de Estudiantes con filter y lambda.
"""

from ejercicio_7 import filtrar_aprobados


def test_filtrar_aprobados_basico() -> None:
    """Verifica que solo se incluyan los estudiantes con nota >= 3.0."""
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("María", 3.9)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == [("Ana", 4.5), ("María", 3.9)]


def test_filtrar_aprobados_limite() -> None:
    """Verifica que los estudiantes con nota exactamente 3.0 también sean aprobados."""
    estudiantes = [("Lucía", 3.0), ("Pedro", 2.9)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == [("Lucía", 3.0)]


def test_filtrar_aprobados_todos_reprobados() -> None:
    """Si todos los estudiantes tienen nota menor a 3.0, debe devolver una lista vacía."""
    estudiantes = [("Carlos", 2.0), ("Juan", 1.8)]
    assert filtrar_aprobados(estudiantes) == []


def test_filtrar_aprobados_lista_vacia() -> None:
    """Si la lista está vacía, debe devolver una lista vacía."""
    assert filtrar_aprobados([]) == []
