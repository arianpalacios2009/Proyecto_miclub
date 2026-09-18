#d) Crear el archivo socio.py con la clase Socio:
#Atributos:

#● clubes (lista)
#● cuotas (lista)
#● fecha_inscripcion (DD/MM/AAAA)
#● estado (activo, suspendido, inactivo)
#● __usuario
#● __contraseña

#Métodos:

#● getters y setters
# socio.py
from modelo.persona import Persona


class Socio(Persona):
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion,
                 nacionalidad, fecha_inscripcion, estado, usuario, contrasena, rol="socio"):

        # inicializa lo que viene de Persona
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)

        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado

        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__rol = rol   # "socio" o "admin"

    # ---------- GETTERS ----------
    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena

    def get_rol(self):
        return self.__rol

    # ---------- SETTERS ----------
    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def set_rol(self, rol):
        self.__rol = rol

    # ---------- ROL: reemplaza a la clase Administrador ----------
    def es_admin(self):
        return self.__rol == "admin"

    # ---------- CAMBIAR ESTADO ----------
    def cambiar_estado(self):
        self.estado = "suspendido"
        return "el estado esta suspendido"

    # ---------- REGISTRAR PAGO ----------
    def registrar_pago_de_cuota(self):
        self.estado = "pendiente"
        return "el pago esta pendiente"

    # ---------- CANTIDAD DE CUOTAS PENDIENTES ----------
    def cantidad_cuotas(self):
        cantidad = 0
        for cuota in self.cuotas:
            if cuota.get_estado() == "pendiente":
                cantidad += 1
        return cantidad

    # ---------- ACTUALIZAR CONTRASEÑA ----------
    def actualizar_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        return "Contraseña actualizada."

    # ---------- VERIFICAR ACCESO ----------
    def verificar_acceso(self, usuario_ingresado, contrasena_ingresada):
        if usuario_ingresado == self.__usuario and contrasena_ingresada == self.__contrasena:
            return True
        return False