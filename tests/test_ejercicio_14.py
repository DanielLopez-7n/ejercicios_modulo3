import json
import csv
import pytest
from ejercicio_14 import leer_csv, leer_json, generar_reporte


@pytest.fixture
def archivos_temporales(tmp_path):
    # Crear archivos temporales CSV y JSON
    archivo_csv = tmp_path / "estudiantes.csv"
    archivo_json = tmp_path / "cursos.json"
    archivo_reporte = tmp_path / "reporte.txt"

    # CSV de estudiantes
    with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["id", "nombre", "edad"])
        escritor.writerow(["1", "Ana Pérez", "20"])
        escritor.writerow(["2", "Carlos Gómez", "22"])

    # JSON de cursos
    cursos = {"1": ["Matemáticas", "Historia"], "2": ["Física"]}
    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(cursos, f)

    return archivo_csv, archivo_json, archivo_reporte


def test_leer_csv(archivos_temporales):
    archivo_csv, _, _ = archivos_temporales
    estudiantes = leer_csv(archivo_csv)
    assert len(estudiantes) == 2
    assert estudiantes[0]["nombre"] == "Ana Pérez"


def test_leer_json(archivos_temporales):
    _, archivo_json, _ = archivos_temporales
    cursos = leer_json(archivo_json)
    assert "1" in cursos
    assert cursos["1"] == ["Matemáticas", "Historia"]


def test_generar_reporte(archivos_temporales):
    archivo_csv, archivo_json, archivo_reporte = archivos_temporales

    estudiantes = leer_csv(archivo_csv)
    cursos = leer_json(archivo_json)

    generar_reporte(estudiantes, cursos, archivo_reporte)

    contenido = archivo_reporte.read_text(encoding="utf-8")
    assert "Ana Pérez" in contenido
    assert "Matemáticas" in contenido
    assert "Reporte de Cursos por Estudiante" in contenido


def test_reporte_sin_datos(tmp_path):
    archivo_reporte = tmp_path / "reporte.txt"
    generar_reporte([], {}, archivo_reporte)
    assert not archivo_reporte.exists()  # No debe crear archivo si no hay datos
