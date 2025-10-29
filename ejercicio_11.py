from typing import List
from rich.console import Console
from rich.table import Table
import os

ARCHIVO_TAREAS = "tareas.txt"


def agregar_tarea(tarea: str) -> None:
    """Agrega una tarea al archivo de texto."""
    if not tarea.strip():
        raise ValueError("La tarea no puede estar vacía.")
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea.strip() + "\n")


def ver_tareas() -> List[str]:
    """Lee todas las tareas del archivo y las devuelve como lista."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]


def mostrar_tareas_en_tabla(tareas: List[str]) -> None:
    """Muestra las tareas en una tabla usando rich."""
    console = Console()
    if not tareas:
        console.print("[yellow]No hay tareas registradas.[/yellow]")
        return

    tabla = Table(title="Lista de Tareas", show_header=True, header_style="bold green")
    tabla.add_column("N°", justify="center")
    tabla.add_column("Tarea", justify="left")

    for i, tarea in enumerate(tareas, start=1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)


def main():
    """Menú principal de la aplicación."""
    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tareas = ver_tareas()
            mostrar_tareas_en_tabla(tareas)

        elif opcion == "2":
            tarea = input("Ingrese la nueva tarea: ")
            try:
                agregar_tarea(tarea)
                print("Tarea agregada con éxito.")
            except ValueError as e:
                print(f"{e}")

        elif opcion == "3":
            print("Saliendo del gestor de tareas...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
