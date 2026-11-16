from pathlib import Path

from base_de_datos.base_de_datoss import conectar, crear_tablas
from interfaz.app import ClubApp
from servicios.servicios_socios import asegurar_admin

RUTA_BASE = Path(__file__).parent / "club.db"


def main():
    conexion = conectar(str(RUTA_BASE))
    crear_tablas(conexion)
    conexion.close()

    admin = asegurar_admin()
    if admin is not None:
        print("Admin creado: usuario 'admin' / contraseña 'admin123'")

    ClubApp().mainloop()


if __name__ == "__main__":
    main()
