import json
from typing import Any
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel


# === Configuración Rich personalizada ===
custom_theme = Theme(
    {
        "info": "bold cyan",
        "warning": "bold yellow",
        "error": "bold red",
        "success": "bold green",
        "title": "bold magenta underline",
        "book": "bright_blue",
    }
)
console = Console(theme=custom_theme)


# === Funciones auxiliares de presentación ===
def print_panel(text: str, title: str = "", border_style: str = "bright_blue") -> None:
    """Imprime texto dentro de un panel bonito."""
    console.print(Panel.fit(text, title=title, border_style=border_style))


def print_table(
    headers: list[str], rows: list[list[str]], title: str = "Tabla"
) -> None:
    """Imprime una tabla con estilo."""
    table = Table(title=title, style="bold cyan", border_style="bright_magenta")
    for h in headers:
        table.add_column(h, style="bold yellow")
    for row in rows:
        table.add_row(*row)
    console.print(table)


# === Funciones de manejo de biblioteca ===
def cargar_biblioteca(nombre_archivo: str) -> list[dict[str, Any]]:
    """Carga los datos de la biblioteca desde un archivo JSON."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[warning]Archivo no encontrado, creando nuevo...[/warning]")
        return []
    except json.JSONDecodeError:
        console.print("[error]Error al leer el archivo JSON.[/error]")
        return []


def guardar_biblioteca(nombre_archivo: str, biblioteca: list[dict[str, Any]]) -> None:
    """Guarda el estado actual de la biblioteca en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, indent=4, ensure_ascii=False)


def prestar_libro(
    biblioteca: list[dict[str, Any]], libro_id: str, nombre_aprendiz: str
) -> bool:
    """Marca un libro como prestado si está disponible."""
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                libro["prestado_a"] = nombre_aprendiz
                console.print(f"Libro prestado a [success]{nombre_aprendiz}[/success]")
                return True
            else:
                console.print("[error]El libro ya está prestado.[/error]")
                return False
    console.print("[error]Libro no encontrado.[/error]")
    return False


def devolver_libro(biblioteca: list[dict[str, Any]], libro_id: str) -> bool:
    """Marca un libro como devuelto."""
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is not None:
                libro["prestado_a"] = None
                console.print("[success]Libro devuelto correctamente.[/success]")
                return True
            else:
                console.print("[warning]El libro no estaba prestado.[/warning]")
                return False
    console.print("[error]Libro no encontrado.[/error]")
    return False


def buscar_libro(biblioteca: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Busca libros cuyo título contenga la palabra indicada (no sensible a mayúsculas)."""
    resultados = [libro for libro in biblioteca if query.lower() in libro["titulo"].lower()]
    if resultados:
        rows = [
            [libro["libro_id"], libro["titulo"], libro["prestado_a"] or "Disponible"]
            for libro in resultados
        ]
        print_table(["ID", "Título", "Estado"], rows, title="Resultados de Búsqueda")
    else:
        console.print("[warning]No se encontraron libros con ese título.[/warning]")
    return resultados



def ver_libros_prestados(biblioteca: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Muestra todos los libros que están actualmente prestados."""
    prestados = [libro for libro in biblioteca if libro["prestado_a"] is not None]
    if prestados:
        rows = [
            [libro["libro_id"], libro["titulo"], libro["prestado_a"]]
            for libro in prestados
        ]
        print_table(["ID", "Título", "Prestado a"], rows, title="Libros Prestados")
    else:
        console.print("[info]No hay libros prestados actualmente.[/info]")
    return prestados



# === Función principal con menú ===
def main() -> None:
    """Función principal con menú interactivo."""
    archivo = "biblioteca.json"
    biblioteca = cargar_biblioteca(archivo)

    while True:
        print_panel(
            "1 Prestar libro\n2 Devolver libro\n3 Buscar libro\n4 Ver libros prestados\n5 Salir",
            title="Menú Biblioteca",
        )

        opcion = console.input("[bold cyan]Selecciona una opción: [/bold cyan] ")

        if opcion == "1":
            libro_id = console.input("ID del libro: ")
            nombre = console.input("Nombre del aprendiz: ")
            if prestar_libro(biblioteca, libro_id, nombre):
                guardar_biblioteca(archivo, biblioteca)

        elif opcion == "2":
            libro_id = console.input("ID del libro a devolver: ")
            if devolver_libro(biblioteca, libro_id):
                guardar_biblioteca(archivo, biblioteca)

        elif opcion == "3":
            query = console.input("Buscar por título: ")
            buscar_libro(biblioteca, query)

        elif opcion == "4":
            ver_libros_prestados(biblioteca)

        elif opcion == "5":
            console.print("[success]Saliendo del sistema... ¡Hasta pronto![/success]")
            break

        else:
            console.print("[error]Opción inválida. Intenta de nuevo.[/error]")


if __name__ == "__main__":
    main()
