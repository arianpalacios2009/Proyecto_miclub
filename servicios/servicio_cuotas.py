
from pathlib import Path

from base_de_datos.base_de_datoss import (
    conectar,
    listar_cuotas_de_socio,
    pagar_cuota as pagar_cuota_en_bd,
)


RUTA_DB = Path(__file__).parent.parent / "club.db"


def listar_cuotas(usuario):
    """Devuelve las cuotas de un socio."""

    conexion = conectar(str(RUTA_DB))

    try:
        return listar_cuotas_de_socio(conexion, usuario)

    finally:
        conexion.close()


def pagar_cuota(usuario, periodo):
    """Registra el pago de una cuota."""

    conexion = conectar(str(RUTA_DB))

    try:
        return pagar_cuota_en_bd(conexion, usuario, periodo)

    finally:
        conexion.close()

