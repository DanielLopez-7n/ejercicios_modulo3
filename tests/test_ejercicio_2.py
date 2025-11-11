from ejercicio_2 import crear_perfil


def test_perfil_completo():
    resultado = crear_perfil(
        "Ana", 25, "leer", "viajar", twitter="@anita25", instagram="@ana_ig"
    )
    assert "Ana" in resultado
    assert "leer" in resultado
    assert "twitter" in resultado.lower()
    assert "@anita25" in resultado


def test_perfil_sin_hobbies():
    resultado = crear_perfil("Carlos", 30, twitter="@carlos30")
    assert "Hobbies: (sin registrar)" in resultado


def test_perfil_sin_redes():
    resultado = crear_perfil("Laura", 28, "bailar", "dibujar")
    assert "Redes Sociales: (sin registrar)" in resultado


def test_perfil_vacio():
    # Caso borde: sin hobbies ni redes
    resultado = crear_perfil("Pedro", 40)
    assert "Hobbies: (sin registrar)" in resultado
    assert "Redes Sociales: (sin registrar)" in resultado
