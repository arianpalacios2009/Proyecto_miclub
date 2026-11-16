from datetime import date
from pathlib import Path

from base_de_datos.base_de_datoss import (
    conectar,
    crear_tablas,
    guardar_socio,
)

from modelo.socio import Socio
from servicios.servicio_autenticacion import autenticar


# Ruta de la base de datos
RUTA = Path(__file__).parent / "club.db"


# Crear una base de datos nueva para las pruebas
if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)


try:
    # Crear un socio de prueba
    brenda = Socio(
        "Brenda",
        26,
        "DNI",
        "30900777",
        "Argentina",
        date(2026, 10, 16),
        "Activo",
        "socio",
        "brenda123",
        "racing123"
    )

    # Guardar el socio
    guardar_socio(conexion, brenda)

    print("Socio guardado correctamente.")

    # Probar la autenticación
    socio = autenticar("brenda123", "racing123")

    if socio is None:
        print("El socio no existe o los datos son incorrectos.")
    else:
        print("El socio existe.")
        print("Nombre completo:", socio.nombre_completo)
        print("Nombre de usuario:", socio.get_usuario())

finally:
    conexion.close()
