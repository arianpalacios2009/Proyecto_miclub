from base_de_datos.base_de_datoss import conectar,buscar_socio_por_usuario
from pathlib import Path

ruta_BD=Path(__file__).parent.parent/"club.db"

def autenticar(usuario,contrasena):
    conexion=conectar(ruta_BD)
    socio= buscar_socio_por_usuario(conexion,usuario)
    conexion.close()

    #si el socio no existe,retorne a vacio
    if socio is None:
        return None
    
    if socio.get_contrasena() == contrasena:
        return socio
    
    return None
