import os
import pytest
from ejercicio_11 import agregar_tarea, ver_tareas, ARCHIVO_TAREAS


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Se ejecuta antes de cada test para iniciar con un archivo limpio."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    yield
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)


def test_agregar_y_ver_tareas():
    agregar_tarea("Aprender Python")
    agregar_tarea("Estudiar para el examen")
    tareas = ver_tareas()
    assert len(tareas) == 2
    assert "Aprender Python" in tareas
    assert "Estudiar para el examen" in tareas


def test_agregar_tarea_vacia_lanza_error():
    with pytest.raises(ValueError):
        agregar_tarea("   ")


def test_ver_tareas_con_archivo_vacio():
    tareas = ver_tareas()
    assert tareas == []


def test_archivo_se_crea_correctamente():
    agregar_tarea("Hacer ejercicio")
    assert os.path.exists(ARCHIVO_TAREAS)


def test_lectura_no_incluye_lineas_vacias():
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        archivo.write("Tarea 1\n\nTarea 2\n")
    tareas = ver_tareas()
    assert tareas == ["Tarea 1", "Tarea 2"]
