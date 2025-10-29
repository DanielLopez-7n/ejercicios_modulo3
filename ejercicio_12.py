import csv
from typing import Dict
from rich.console import Console
from rich.table import Table


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Lee un archivo CSV con datos de estudiantes y analiza una columna numérica.
    Retorna un diccionario con el promedio, el máximo y el mínimo de esa columna.

    Args:
        nombre_archivo (str): Ruta del archivo CSV.
        columna (str): Nombre de la columna numérica a analizar.

    Returns:
        dict: {'promedio': float, 'max': float, 'min': float}
    """
    valores = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        if columna not in lector.fieldnames:
            raise ValueError(f"La columna '{columna}' no existe en el archivo.")

        for fila in lector:
            valor = fila.get(columna)
            try:
                valores.append(float(valor))
            except (TypeError, ValueError):
                # Ignorar celdas vacías o con datos no numéricos
                continue

    if not valores:
        raise ValueError(f"No se encontraron valores numéricos válidos en la columna '{columna}'.")

    resultado = {
        "promedio": sum(valores) / len(valores),
        "max": max(valores),
        "min": min(valores)
    }

    return resultado


def mostrar_resultados_tabla(resultado: Dict[str, float], columna: str) -> None:
    """
    Muestra los resultados del análisis en una tabla con Rich.
    """
    console = Console()
    tabla = Table(title=f"Análisis de la columna '{columna}'", show_header=True, header_style="bold cyan")

    tabla.add_column("Métrica", justify="left")
    tabla.add_column("Valor", justify="right")

    for clave, valor in resultado.items():
        tabla.add_row(clave.capitalize(), f"{valor:.2f}")

    console.print(tabla)


def main():
    print("=== Analizador de Datos CSV ===")
    nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
    columna = input("Ingrese el nombre de la columna a analizar: ")

    try:
        resultado = analizar_csv(nombre_archivo, columna)
        mostrar_resultados_tabla(resultado, columna)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except ValueError as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()
