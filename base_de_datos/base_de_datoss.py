
import sqlite3
from datetime import date
from modelo.cuota import Cuota
from modelo.socio import Socio
from modelo.actividad import Actividad


def conectar(ruta):
    """Abre una conexión con la base de datos."""
    conexion = sqlite3.connect(ruta)
    return conexion


def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo TEXT NOT NULL,
            edad INTEGER,
            tipo_identificacion TEXT,
            identificacion TEXT,
            nacionalidad TEXT,
            fecha_inscripcion TEXT,
            estado TEXT DEFAULT 'Activo',
            rol TEXT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id_cuota INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id INTEGER NOT NULL,
            estado TEXT DEFAULT 'pendiente',
            fecha_de_vencimiento TEXT,
            periodo TEXT,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades (
            id_actividad INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dia TEXT,
            horario TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes (
            id_club INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            ubicacion TEXT,
            presidente TEXT,
            fecha_fundacion TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socio_actividad (
            socio_id INTEGER NOT NULL,
            actividad_id INTEGER NOT NULL,
            PRIMARY KEY (socio_id, actividad_id),
            FOREIGN KEY (socio_id) REFERENCES socios(id),
            FOREIGN KEY (actividad_id) REFERENCES actividades(id_actividad)
        )
    """)

    conexion.commit()


def guardar_socio(conexion, socio):
    """Guarda un socio en la tabla socios."""
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO socios (
            nombre_completo, edad, tipo_identificacion,
            identificacion, nacionalidad, fecha_inscripcion,
            estado, rol, usuario, contrasena
        )
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
        socio.get_contrasena()
    ))

    conexion.commit()


def buscar_socio_por_usuario(conexion, usuario):
    """Busca un socio y devuelve un objeto Socio o None."""
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT nombre_completo, edad, tipo_identificacion,
               identificacion, nacionalidad, fecha_inscripcion,
               estado, rol, usuario, contrasena
        FROM socios
        WHERE usuario = ?
    """, (usuario,))

    fila = cursor.fetchone()

    if fila is None:
        return None

    (
        nombre_completo, edad, tipo_identificacion,
        identificacion, nacionalidad, fecha_inscripcion,
        estado, rol, usuario_encontrado, contrasena
    ) = fila

    return Socio(
        nombre_completo,
        edad,
        tipo_identificacion,
        identificacion,
        nacionalidad,
        date.fromisoformat(fecha_inscripcion),
        estado,
        rol,
        usuario_encontrado,
        contrasena
    )


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
        INSERT INTO cuotas (
            socio_id, estado, fecha_de_vencimiento, periodo
        )
        VALUES (?, ?, ?, ?)
    """, (
        socio_id,
        cuota.get_estado(),
        cuota.fecha_de_vencimiento.isoformat(),
        cuota.periodo
    ))

    conexion.commit()


def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve las cuotas de un socio."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return []

    socio_id = fila[0]

    cursor.execute("""
        SELECT periodo, estado, fecha_de_vencimiento
        FROM cuotas
        WHERE socio_id = ?
    """, (socio_id,))

    cuotas = []

    for periodo, estado, fecha_vencimiento in cursor.fetchall():
        cuota = Cuota(
            estado,
            date.fromisoformat(fecha_vencimiento),
            periodo
        )
        cuotas.append(cuota)

    return cuotas


def guardar_club(conexion, club):
    """Guarda el club si todavía no existe."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id_club FROM clubes WHERE nombre = ?",
        (club.nombre,)
    )
    fila = cursor.fetchone()

    if fila is not None:
        return fila[0]

    cursor.execute("""
        INSERT INTO clubes (
            nombre, descripcion, ubicacion, presidente, fecha_fundacion
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        club.nombre,
        club.descripcion,
        club.ubicacion,
        club.get_presidente(),
        club.get_fecha_fundacion()
    ))

    conexion.commit()


def obtener_club(conexion):
    """Devuelve un objeto Club o None si no hay club."""
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion
        FROM clubes
        LIMIT 1
    """)

    fila = cursor.fetchone()

    if fila is None:
        return None

    nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila

    from modelo.club import Club

    return Club(
        nombre,
        descripcion,
        ubicacion,
        presidente,
        date.fromisoformat(fecha_fundacion)
    )


def guardar_actividad(conexion, actividad):
    """Guarda una actividad si todavía no existe."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id_actividad FROM actividades WHERE nombre = ?",
        (actividad.nombre,)
    )
    fila = cursor.fetchone()

    if fila is not None:
        return fila[0]

    cursor.execute("""
        INSERT INTO actividades (nombre, dia, horario)
        VALUES (?, ?, ?)
    """, (
        actividad.nombre,
        actividad.dia,
        actividad.horario
    ))

    conexion.commit()


def anotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Anota al socio en una actividad."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return "El socio no existe."

    socio_id = fila[0]

    cursor.execute(
        "SELECT id_actividad FROM actividades WHERE nombre = ?",
        (nombre_actividad,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return f"La actividad {nombre_actividad} no existe."

    actividad_id = fila[0]

    cursor.execute("""
        INSERT OR IGNORE INTO socio_actividad (socio_id, actividad_id)
        VALUES (?, ?)
    """, (socio_id, actividad_id))

    conexion.commit()

    return f"Te anotaste en {nombre_actividad}."


def desanotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Desanota al socio de una actividad."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return "El socio no existe."

    socio_id = fila[0]

    cursor.execute(
        "SELECT id_actividad FROM actividades WHERE nombre = ?",
        (nombre_actividad,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return f"La actividad {nombre_actividad} no existe."

    actividad_id = fila[0]

    cursor.execute("""
        DELETE FROM socio_actividad
        WHERE socio_id = ? AND actividad_id = ?
    """, (socio_id, actividad_id))

    conexion.commit()

    return f"Te desanotaste de {nombre_actividad}."


def listar_actividades_de_socio(conexion, usuario):
    """Devuelve objetos Actividad de un socio."""
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return []

    socio_id = fila[0]

    cursor.execute("""
        SELECT actividades.nombre, actividades.dia, actividades.horario
        FROM actividades
        JOIN socio_actividad
        ON actividades.id_actividad = socio_actividad.actividad_id
        WHERE socio_actividad.socio_id = ?
    """, (socio_id,))

    actividades = []

    for nombre, dia, horario in cursor.fetchall():
        actividades.append(Actividad(nombre, dia, horario))

    return actividades
