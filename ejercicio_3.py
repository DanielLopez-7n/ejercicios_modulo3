"""Ejercicio 3: Contador de Llamadas con Closure.

Este módulo implementa una función que genera contadores independientes
utilizando funciones anidadas (closures) y la palabra clave `nonlocal`.
"""

from typing import Callable

from rich.console import Console
from rich.table import Table


def crear_contador() -> Callable[[], int]:
    """Crea un contador independiente que recuerda su valor entre llamadas.

    Returns:
        Callable[[], int]: Una función que, al ser llamada, incrementa y devuelve
        el conteo actual.
    """
    conteo = 0

    def incrementar() -> int:
        """Incrementa el conteo interno y lo devuelve."""
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def mostrar_contadores(resultados: list[tuple[str, int]]) -> None:
    """Muestra los resultados de los contadores en una tabla usando Rich.

    Args:
        resultados (list[tuple[str, int]]): Lista de tuplas con el nombre del contador
        y su valor.
    """
    console = Console()
    table = Table(title="Resultados de los Contadores", style="cyan")
    table.add_column("Contador", style="bold magenta")
    table.add_column("Valor", justify="center")

    for nombre, valor in resultados:
        table.add_row(nombre, str(valor))

    console.print(table)


def main() -> None:
    """Ejecuta una demostración del funcionamiento de los contadores."""
    contador_a = crear_contador()
    contador_b = crear_contador()

    resultados = [
        ("Contador A - Llamada 1", contador_a()),
        ("Contador A - Llamada 2", contador_a()),
        ("Contador B - Llamada 1", contador_b()),
        ("Contador A - Llamada 3", contador_a()),
        ("Contador B - Llamada 2", contador_b()),
    ]

    mostrar_contadores(resultados)


if __name__ == "__main__":
    main()
