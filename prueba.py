from datetime import date
from pathlib import Path
from base_de_datos.base_de_datoss import (
    conectar, crear_tablas, guardar_socio, buscar_socio_por_usuario,
    guardar_cuota, listar_cuotas_de_socio, anotar_socio_actividad,
    desanotar_socio_actividad, listar_actividades_de_socio,
    guardar_actividad, guardar_club, obtener_club
)
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.actividad import Actividad
from modelo.club import Club
from servicios.servicio_autenticacion import autenticar


RUTA = Path(__file__).parent / "club.db"

if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)

brenda=Socio("Brenda",26,"DNI","30900777","Argentina",date(2026,10,16),"activo","socio","brenda123","racing123")
guardar_socio(conexion,brenda)
socio=autenticar("brenda123","racing123")

if socio is None :
    print("El socio no existe")
else:
    print("El socio existe")
    print("nombre completo: ",socio.nombre_completo)
    print("nombre de usuario: ",socio.get_usuario())
    print("su contrasena: ",socio.get_contrasena())
# socio1=Socio("Brenda",26,"DNI","30900777","Argentina",date(2026,10,16),"activo","socio","brenda123","racing123")
# socio2=Socio("Juan",20,"DNI","29201234","Argentina",date(2026,9,10),"activo","socio","juan321","54321")
# socio3=Socio("Pepe",30,"DNI","19202300","Argentina",date(2026,7,4),"activo","admin","pepe30","pepe1234")

# guardar_socio(conexion,socio1)
# guardar_socio(conexion,socio2)
# guardar_socio(conexion,socio3)
# print("se guardaron socios")


# cuota1 = Cuota("pendiente", date(2026, 10, 16), "Octubre 2026")
# cuota2=Cuota("pendiente", date(2026, 9, 10), "Septiembre 2026")
# cuota3=Cuota("pendiente", date(2026, 7, 4), "Julio 2026")


# guardar_cuota(conexion, "brenda123", cuota1)
# guardar_cuota(conexion, "juan321",cuota2 )
# guardar_cuota(conexion, "pepe30", cuota3)
# print("se guardaron las cuotas")


# actividad1 = Actividad("Futbol", "Lunes", "18:00")
# actividad2= Actividad("basquetball", "viernes", "17:00")
# actividad3 = Actividad("voley", "miércoles", "14:00")


# guardar_actividad(conexion, actividad1)
# guardar_actividad(conexion, actividad2)
# guardar_actividad(conexion, actividad3)

# print("se guardó la actividad")

# club1 = Club("Boca juniors","bostero hasta el final","Ciudad Autónoma de Buenos Aires","roman riquelme",date(1905, 4, 3))

# guardar_club(conexion, club1)

# club = obtener_club(conexion)

# if club is not None:
#     print("Nombre:", club.nombre)
#     print("Descripción:", club.descripcion)
#     print("Ubicación:", club.ubicacion)
#     print("Presidente:", club.get_presidente())
#     print("Fecha de fundación:", club.get_fecha_fundacion())
# else:
#     print("No se encontró el club")




# anotar_socio_actividad(conexion,"brenda123","Futbol")
# anotar_socio_actividad(conexion, "juan321", "basquetball")
# anotar_socio_actividad(conexion, "pepe30", "voley")

# desanotar_socio_actividad(conexion,"brenda123","Futbol")
# desanotar_socio_actividad(conexion,"juan321","basquetball")


# print("Actividades de Pepe:")
# for actividad in listar_actividades_de_socio(conexion, "pepe30"):
#     print(actividad.mostrarInfo())



# for usuario in ("brenda123","juan321","pepe30"):
#     print(f"cuotas de {usuario}: ")
#     for cuotas in listar_cuotas_de_socio(conexion,usuario):
#         print(cuotas)

# socio_encontrado = buscar_socio_por_usuario(conexion, "brenda123")

# if socio_encontrado is not None:
#     print("Socio encontrado:", socio_encontrado.nombre_completo)
# else:
#     print("No se encontró el socio")

conexion.close()