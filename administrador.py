#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters
from club_categoria import ClubDeportivo

class Administrador(ClubDeportivo):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios, actividades, usuario, contrasena):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios, actividades)
        self.__usuario = usuario
        self.__contrasena = contrasena

    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def agregar_lista(self, socio):
        self.registrar_socios(socio)

    def listado_completo(self):
        for socio in self.get_socios():
            print("Usuario del socio:", socio.get_usuario())

    def reactivar_socio(self, socio):
        if socio not in self.get_socios():
            print("Ese socio no pertenece a este club.")
            return False
    
        elif socio.estado != "suspendido":
            print("El socio no está suspendido, no corresponde reactivarlo.")
        return False


    def suspender_socio(self, socio):
        if socio not in self.get_socios():
            print("Ese socio no pertenece a este club.")
        return False
    
        if socio.estado == "suspendido":
            print("El socio ya se encuentra suspendido.")
        return False
    
        socio.estado = "suspendido"
        print("El socio fue suspendido por incumplimiento o deudas pendientes.")
        return True
    
            


admin=Administrador("tiziano","tizi123","87654321")
admin.agregar_lista("arian")
admin.agregar_lista("juan")
admin.agregar_lista("pepe")
admin.listado_completo()