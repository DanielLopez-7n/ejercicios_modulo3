def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con información personal, hobbies y redes sociales.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista variable de hobbies o intereses.
        **redes_sociales (str): Pares clave-valor donde la clave es el nombre de la red
            (por ejemplo, 'twitter', 'instagram') y el valor es el nombre de usuario
            o enlace del perfil.

    Returns:
        str: Un texto formateado con toda la información del usuario.
    """
    perfil = f"Perfil de Usuario\nNombre: {nombre}\nEdad: {edad}\n"

    if hobbies:
        hobbies_texto = ", ".join(hobbies)
        perfil += f"Hobbies: {hobbies_texto}\n"
    else:
        perfil += "Hobbies: (sin registrar)\n"

    if redes_sociales:
        perfil += "Redes Sociales:\n"
        for red, usuario in redes_sociales.items():
            perfil += f"  • {red.capitalize()}: {usuario}\n"
    else:
        perfil += "Redes Sociales: (sin registrar)\n"

    return perfil.strip()


def main() -> None:
    """
    Función principal que ejecuta un ejemplo de uso del generador de perfiles.
    """
    perfil = crear_perfil(
        "Daniel",
        19,
        "programar",
        "música",
        "fútbol",
        twitter="@daniel_dev",
        github="dani-github",
    )
    print(perfil)


if __name__ == "__main__":
    main()
