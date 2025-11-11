import pytest
from ejercicio_15 import (
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
)


@pytest.fixture
def biblioteca_mock():
    return [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {
            "libro_id": "002",
            "titulo": "Don Quijote de la Mancha",
            "prestado_a": "Carlos",
        },
    ]


def test_prestar_libro(biblioteca_mock):
    assert prestar_libro(biblioteca_mock, "001", "Ana")
    assert biblioteca_mock[0]["prestado_a"] == "Ana"


def test_prestar_libro_ya_prestado(biblioteca_mock):
    assert not prestar_libro(biblioteca_mock, "002", "Pedro")


def test_devolver_libro(biblioteca_mock):
    assert devolver_libro(biblioteca_mock, "002")
    assert biblioteca_mock[1]["prestado_a"] is None


def test_devolver_libro_no_prestado(biblioteca_mock):
    assert not devolver_libro(biblioteca_mock, "001")


def test_buscar_libro(biblioteca_mock):
    resultados = buscar_libro(biblioteca_mock, "Soledad")
    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Cien Años de Soledad"


def test_ver_libros_prestados(biblioteca_mock):
    prestados = ver_libros_prestados(biblioteca_mock)
    assert len(prestados) == 1
    assert prestados[0]["titulo"] == "Don Quijote de la Mancha"
