import csv
import pytest
from ejercicio_12 import analizar_csv


@pytest.fixture
def archivo_csv_temp(tmp_path):
    """Crea un archivo CSV temporal con datos de prueba."""
    ruta = tmp_path / "estudiantes.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre", "edad", "calificacion"])
        escritor.writerow(["Ana", 20, 4.5])
        escritor.writerow(["Juan", 21, 3.8])
        escritor.writerow(["Maria", 19, 4.0])
    return ruta


def test_analizar_csv_funciona_correctamente(archivo_csv_temp):
    resultado = analizar_csv(archivo_csv_temp, "calificacion")
    assert pytest.approx(resultado["promedio"], 0.1) == 4.1
    assert resultado["max"] == 4.5
    assert resultado["min"] == 3.8


def test_analizar_csv_con_columna_inexistente(archivo_csv_temp):
    with pytest.raises(ValueError):
        analizar_csv(archivo_csv_temp, "nota_final")


def test_analizar_csv_con_datos_no_numericos(tmp_path):
    ruta = tmp_path / "datos_invalidos.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre", "edad"])
        escritor.writerow(["Ana", "abc"])
        escritor.writerow(["Luis", ""])
    with pytest.raises(ValueError):
        analizar_csv(ruta, "edad")


def test_analizar_csv_archivo_vacio(tmp_path):
    ruta = tmp_path / "vacio.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        f.write("nombre,edad,calificacion\n")
    with pytest.raises(ValueError):
        analizar_csv(ruta, "calificacion")
