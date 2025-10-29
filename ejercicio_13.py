import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

console = Console()

ARCHIVO_INVENTARIO = "inventario.json"


def cargar_inventario(nombre_archivo: str = ARCHIVO_INVENTARIO) -> List[Dict]:
    """Carga el inventario desde un archivo JSON. Retorna lista vacía si no existe."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_inventario(inventario: List[Dict], nombre_archivo: str = ARCHIVO_INVENTARIO) -> None:
    """Guarda el inventario actual en el archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)


def agregar_producto(inventario: List[Dict], nombre: str, cantidad: int, precio: float) -> List[Dict]:
    """Agrega un nuevo producto al inventario."""
    nuevo = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(nuevo)
    return inventario


def vender_producto(inventario: List[Dict], nombre: str, cantidad_vendida: int) -> List[Dict]:
    """Disminuye la cantidad del producto indicado si hay stock suficiente."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
            else:
                console.print(f"[red]Stock insuficiente para {nombre}[/red]")
            return inventario

    console.print(f"[yellow]Producto '{nombre}' no encontrado[/yellow]")
    return inventario


def mostrar_inventario(inventario: List[Dict]) -> None:
    """Muestra el inventario en formato tabla con Rich."""
    if not inventario:
        console.print("[red]Inventario vacío[/red]")
        return

    tabla = Table(title="Inventario Actual")
    tabla.add_column("Nombre", justify="left", style="cyan")
    tabla.add_column("Cantidad", justify="center", style="green")
    tabla.add_column("Precio", justify="right", style="yellow")

    for producto in inventario:
        tabla.add_row(
            producto["nombre"],
            str(producto["cantidad"]),
            f"${producto['precio']:,}"
        )

    console.print(tabla)


def main() -> None:
    inventario = cargar_inventario()
    while True:
        console.print("\n[bold blue]Gestor de Inventario[/bold blue]")
        console.print("1. Ver inventario\n2. Agregar producto\n3. Vender producto\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario = agregar_producto(inventario, nombre, cantidad, precio)
            guardar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            inventario = vender_producto(inventario, nombre, cantidad)
            guardar_inventario(inventario)
        elif opcion == "4":
            break
        else:
            console.print("[red]Opción inválida[/red]")


if __name__ == "__main__":
    main()
