from datetime import date 
from pathlib import Path
from base_de_datos.base_de_datoss import(conectar,crear_tablas,guardar_socio,guardar_cuota,listar_cuotas_de_socio)

from modelo.socio import Socio
from modelo.cuota import Cuota

RUTA = Path(__file__).parent / "club.db"

if RUTA.exists():
    RUTA.unlink() #borra la tabla anterior(si es que estaba creada) y ejecuta una nueva

conexion=conectar(str(RUTA))
crear_tablas(conexion)

socio1=Socio("Brenda",26,"DNI","30900777","Argentina",date(2026,10,16),"activo","socio","brenda123","racing123")
socio2=Socio("Juan",20,"DNI","29201234","Argentina",date(2026,9,10),"activo","socio","juan321","54321")
socio3=Socio("Pepe",30,"DNI","19202300","Argentina",date(2026,7,4),"activo","admin","pepe30","pepe1234")

guardar_socio(conexion,socio1)
guardar_socio(conexion,socio2)
guardar_socio(conexion,socio3)
print("se guardaron socios")


guardar_cuota(conexion, "brenda123", Cuota("pendiente", date(2026, 10, 16), "Octubre 2026"))
guardar_cuota(conexion, "juan321", Cuota("pendiente", date(2026, 9, 10), "Septiembre 2026"))
guardar_cuota(conexion, "pepe30", Cuota("pendiente", date(2026, 7, 4), "Julio 2026"))
print("se guardaron las cuotas")

for usuario in ("Brenda123","Juan321","Pepe30"):
    print(f"cuotas de {usuario}:")
    for cuotas in listar_cuotas_de_socio(conexion,usuario):
        print (cuotas)

conexion.close()