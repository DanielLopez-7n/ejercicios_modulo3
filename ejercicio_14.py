import csv
import json
from rich.console import Console
from rich.table import Table

console = Console()


def leer_csv(ruta_csv):
    """Lee los datos de estudiantes desde un archivo CSV."""
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return [fila for fila in lector]
    except FileNotFoundError:
        console.print(f"[red]Error:[/] No se encontró el archivo {ruta_csv}")
        return []


def leer_json(ruta_json):
    """Lee los datos de cursos desde un archivo JSON."""
    try:
        with open(ruta_json, mode="r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        console.print(f"[red]Error:[/] No se encontró el archivo {ruta_json}")
        return {}


def generar_reporte(estudiantes, cursos, ruta_salida):
    """
    Genera un reporte que combina los datos de estudiantes y cursos,
    y lo guarda en un archivo de texto.
    """
    if not estudiantes or not cursos:
        console.print("[yellow]No hay datos suficientes para generar el reporte.[/]")
        return

    # Crear estructura del reporte
    reporte_lineas = []
    tabla = Table(title="Reporte de Cursos por Estudiante", show_lines=True)
    tabla.add_column("ID Estudiante", style="cyan", justify="center")
    tabla.add_column("Nombre", style="green")
    tabla.add_column("Cursos Inscritos", style="magenta")

    for estudiante in estudiantes:
        id_est = estudiante.get("id")
        nombre = estudiante.get("nombre")
        cursos_tomados = cursos.get(id_est, [])

        cursos_str = ", ".join(cursos_tomados) if cursos_tomados else "Ninguno"
        reporte_lineas.append(f"{id_est} - {nombre}: {cursos_str}")
        tabla.add_row(id_est, nombre, cursos_str)

    # Mostrar reporte en consola
    console.print(tabla)

    # Guardar en archivo de texto
    with open(ruta_salida, mode="w", encoding="utf-8") as archivo:
        archivo.write("Reporte de Cursos por Estudiante\n")
        archivo.write("=" * 40 + "\n")
        archivo.write("\n".join(reporte_lineas))

    console.print(f"[green]Reporte generado exitosamente en {ruta_salida}[/]")


if __name__ == "__main__":
    estudiantes = leer_csv("estudiantes_ej14.csv")  # ✅ nuevo nombre
    cursos = leer_json("cursos.json")
    generar_reporte(estudiantes, cursos, "reporte.txt")
