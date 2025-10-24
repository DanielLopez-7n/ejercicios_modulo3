import sys


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC) basado en el peso y la
    altura proporcionados.
    """
    return peso / (altura**2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC y devuelve una categoría.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def pedir_float(prompt: str, positivo: bool = True) -> float:
    """
    Lee y valida un float desde input. Reintenta ante entradas inválidas.
    Captura KeyboardInterrupt/EOFError para salir sin traceback.
    """
    while True:
        try:
            texto = input(prompt)
            valor = float(texto)
            if positivo and valor <= 0:
                print("El valor debe ser mayor que cero. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Introduce un número válido (p.ej. 70.5).")
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)


def main() -> None:
    """
    Orquesta el programa: pide los datos al usuario, calcula el IMC y
    muestra la interpretación.
    """
    try:
        peso = pedir_float("Introduce tu peso en kilogramos: ")
        altura = pedir_float("Introduce tu altura en metros: ")
        imc = calcular_imc(peso, altura)
        resultado = interpretar_imc(imc)
        print(f"Tu IMC es {imc:.2f}, lo cual indica: {resultado}")
    except Exception as e:
        # Mensaje corto para errores inesperados (sin traceback)
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
