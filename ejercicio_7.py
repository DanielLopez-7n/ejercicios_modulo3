"""
Ejercicio 7: Filtrado de Estudiantes con filter y lambda.

Este módulo utiliza la función `filter()` junto con una expresión lambda
para obtener los estudiantes que aprobaron según su nota.

Conceptos aplicados:
- filter()
- lambda
- Trabajo con tuplas
"""

from typing import List, Tuple


def filtrar_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra los estudiantes que aprobaron (nota >= 3.0) usando filter() y lambda.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas con (nombre, nota).

    Returns:
        List[Tuple[str, float]]: Lista de estudiantes aprobados.
    """
    return list(filter(lambda e: e[1] >= 3.0, estudiantes))


def main() -> None:
    """
    Función principal que demuestra el uso de `filtrar_aprobados`.
    """
    estudiantes = [
        ("Ana", 4.5),
        ("Juan", 2.8),
        ("María", 3.9),
        ("Carlos", 1.5),
        ("Lucía", 3.0),
    ]

    print("🎓 Lista original de estudiantes:")
    for nombre, nota in estudiantes:
        print(f"- {nombre}: {nota}")

    aprobados = filtrar_aprobados(estudiantes)

    print("\nEstudiantes aprobados:")
    for nombre, nota in aprobados:
        print(f"- {nombre}: {nota}")


if __name__ == "__main__":
    main()
