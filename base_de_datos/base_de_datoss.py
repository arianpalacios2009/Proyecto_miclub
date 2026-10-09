import sqlite3
#from modelo.socio import Socio

def conectar(ruta):
    conexion=sqlite3.connect(ruta)
    return conexion

def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            edad                INTEGER,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            rol                 TEXT,
            usuario             TEXT UNIQUE NOT NULL,
            contrasena         TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id_cuota            INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id INTEGER NOT NULL`
            estado              TEXT DEFAULT 'pediente'              
            fecha_de_vencimiento    TEXT,
            periodo                 TEXT,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
    """)
    conexion.commit()    



def guardar_socio(conexion, socio):
    """Recibe un objeto Socio y lo guarda en la tabla socios."""
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,
                            identificacion, nacionalidad, fecha_inscripcion,
                            estado, rol, usuario, contrasena)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat(),
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasena(),
    ))
    conexion.commit()



def guardar_cuota(conexion, usuario, cuota):
    """Guarda una cuota asociada a un socio."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )

    fila = cursor.fetchone()

    if fila is None:
        raise ValueError("El socio no existe")

    socio_id = fila[0]

    cursor.execute("""
        INSERT INTO cuotas (socio_id, periodo, fecha_vencimiento, estado)
        VALUES (?, ?, ?, ?)
    """, (
        socio_id,
        cuota.periodo,
        cuota.fecha_vencimiento.isoformat(),
        cuota.estado
    ))

    conexion.commit()


def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Cuota para el socio con ese usuario."""
    cursor = conexion.cursor()

    # Buscar el id del socio
    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )

    fila = cursor.fetchone()

    if fila is None:
        return []

    socio_id = fila[0]

    # Traer las cuotas de ese socio
    cursor.execute(
        "SELECT periodo, estado, fecha_vencimiento FROM cuotas WHERE socio_id = ?",
        (socio_id,)
    )



    from datetime import date
    from modelo.cuota import Cuota

    cuotas = []

    for periodo, estado, fecha_vencimiento in cursor.fetchall():
        cuota = Cuota(
            estado,
            date.fromisoformat(fecha_vencimiento),
            periodo
        )
        cuotas.append(cuota)

    return cuotas
