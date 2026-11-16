
from datetime import date
from pathlib import Path

from base_de_datos.base_de_datoss import (
    conectar,
    buscar_socio_por_usuario,
    listar_socios as listar_socios_en_bd,
    listar_clubes_de_socio as listar_clubes_en_bd,
    guardar_socio,
    actualizar_estado_socio,
)

from modelo.socio import Socio


RUTA_DB = Path(__file__).parent.parent / "club.db"


def obtener_socio(usuario):
    """Devuelve el socio o None si no existe."""

    conexion = conectar(str(RUTA_DB))

    try:
        return buscar_socio_por_usuario(conexion, usuario)

    finally:
        conexion.close()


def listar_socios():
    """Devuelve la lista de todos los socios."""

    conexion = conectar(str(RUTA_DB))

    try:
        return listar_socios_en_bd(conexion)

    finally:
        conexion.close()


def listar_clubes_de_socio(usuario):
    """Devuelve los clubes a los que pertenece un socio."""

    conexion = conectar(str(RUTA_DB))

    try:
        return listar_clubes_en_bd(conexion, usuario)

    finally:
        conexion.close()


def registrar_socio(nombre,edad,tipo_identificacion,identificacion,nacionalidad,usuario,contrasenia):
    """Valida y registra un nuevo socio."""

    nombre = (nombre or "").strip()
    usuario = (usuario or "").strip()
    identificacion = (identificacion or "").strip()

    if not nombre or not usuario or not contrasenia or not identificacion:
        raise ValueError("Completá todos los campos obligatorios.")

    try:
        edad = int(edad)

    except (TypeError, ValueError):
        raise ValueError("La edad debe ser un número entero.")

    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    tipo_identificacion = (tipo_identificacion or "").strip() or None
    nacionalidad = (nacionalidad or "").strip() or None

    socio = Socio(
        nombre,
        edad,
        tipo_identificacion,
        identificacion,
        nacionalidad,
        date.today(),
        "Activo",
        "socio",
        usuario,
        contrasenia
    )

    if not socio.verificar_identificacion():
        raise ValueError("La identificación no puede estar vacía.")

    conexion = conectar(str(RUTA_DB))

    try:
        guardar_socio(conexion, socio)

    finally:
        conexion.close()

    return socio


def suspender_socio(usuario):
    """Suspende a un socio activo."""

    conexion = conectar(str(RUTA_DB))

    try:
        socio = buscar_socio_por_usuario(conexion, usuario)

        if socio is None:
            return "El socio no existe."

        if socio.estado == "Suspendido":
            return "El socio ya se encuentra suspendido."

        if socio.estado == "Activo":
            actualizar_estado_socio(
                conexion,
                usuario,
                "Suspendido"
            )

            return f"El socio {usuario} fue suspendido."

    finally:
        conexion.close()


def reactivar_socio(usuario):
    """Reactiva a un socio suspendido."""

    conexion = conectar(str(RUTA_DB))

    try:
        socio = buscar_socio_por_usuario(conexion, usuario)

        if socio is None:
            return "El socio no existe."

        if socio.estado == "Suspendido":
            actualizar_estado_socio(
                conexion,
                usuario,
                "Activo"
            )

            return f"El socio {usuario} fue reactivado."

        return "El socio no necesita reactivación."

    finally:
        conexion.close()


def asegurar_admin():
    """Crea un admin por defecto si la base de datos no tiene ninguno."""

    conexion = conectar(str(RUTA_DB))

    try:
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM socios WHERE rol = 'admin'"
        )
        cantidad = cursor.fetchone()[0]

        if cantidad > 0:
            return None

        admin = Socio(
            "Administrador del club",
            None,
            None,
            None,
            None,
            date.today(),
            "Activo",
            "admin",
            "admin",
            "admin123"
        )

        guardar_socio(conexion, admin)

        return admin

    finally:
        conexion.close()

