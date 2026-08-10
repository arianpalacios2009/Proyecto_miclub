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

class Socio:
    def __init__(self,fechas_inscripcion,estado,usuario,contrasena):
        self.lista_clubes=[]
        self.lista_cuota = []
    
        self.fecha_inscripcion=fechas_inscripcion
        self.estado=estado
        
        
        #atributos privados
        self.__usuario=usuario
        self.__contrasena=contrasena
    
    def get_usuario(self):
        return self.__usuario
    def get_contrasena(self):
        return self.__contrasena
    
    def set_usuario(self,usuario):
        self.__usuario=usuario
        
    def set_contrasena(self,contrasena):
        self.__contrasena=contrasena
        
        
#Cambiar el estado de un socio activo a suspendido cuando corresponda.

    def cambiar_estado(self):
        self.estado="suspendido"
        print("el estado esta suspendido")

    #Registrar el pago de una cuota pendiente.
    def registrar_pago_de_cuota(self):
        self.estado="pendiente"
        print("el pago esta pendiente")
    
asociarte=Socio("10/6/2026","activo","pepito123","12345678")
asociarte.registrar_pago_de_cuota()
asociarte.cambiar_estado()