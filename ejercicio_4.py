"""
Ejercicio 4: Validador de Datos Genérico

Este módulo demuestra el uso de funciones de orden superior en Python.
Permite aplicar diferentes funciones de validación a una lista de datos.
"""

from typing import Callable, List


def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica una función de validación a cada elemento de la lista y
    devuelve una nueva lista con los elementos que pasan la validación.

    Args:
        datos (List): Lista de elementos a validar.
        validador (Callable): Función que recibe un elemento y devuelve un bool.

    Returns:
        List: Lista de elementos que pasaron la validación.
    """
    return [d for d in datos if validador(d)]


def es_email_valido(email: str) -> bool:
    """
    Valida si un email tiene el formato correcto.
    (Contiene '@' y un punto '.' después).

    Args:
        email (str): Email a validar.

    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return "@" in email and "." in email.split("@")[-1]


def es_mayor_a_10(numero: int) -> bool:
    """
    Verifica si un número es mayor que 10.

    Args:
        numero (int): Número a validar.

    Returns:
        bool: True si es mayor a 10, False en caso contrario.
    """
    return numero > 10


def main():
    """Ejecuta ejemplos de validación."""
    correos = ["ana@mail.com", "pepe@", "carla@gmail.com", "juanmail.com"]
    numeros = [3, 15, 8, 22, 10]

    correos_validos = aplicar_validador(correos, es_email_valido)
    numeros_validos = aplicar_validador(numeros, es_mayor_a_10)

    print("Correos válidos:", correos_validos)
    print("Números mayores a 10:", numeros_validos)


if __name__ == "__main__":
    main()
