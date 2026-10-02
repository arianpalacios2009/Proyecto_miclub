from pathlib import Path
from datetime import date
from base_de_datos.base_de_datoss import conectar,crear_tablas,guardar_socio
from modelo.socio import Socio

RUTA=Path(__file__).parent/"club.db"

conexion=conectar(str(RUTA))
crear_tablas(conexion)

alberto=Socio("alberto gonzales",35,"dni","408200341","Argentina",date(2026,4,5),"activo","socio","alberto","1234")
guardar_socio(conexion,alberto)
print("socio guardado")

