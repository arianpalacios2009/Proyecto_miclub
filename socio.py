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

#Permitir que un socio pueda asociarse a uno o más clubes.
    def asociar_club(self, club):
        if club not in self.lista_clubes:
            self.lista_clubes.append(club)
            print(f"El socio se asoció al club {club.nombre}.")
        else:
            print("El socio ya está asociado a ese club.")      

#Permitir que un socio deje de pertenecer a un club determinado.
    def desasociar_club(self, club):
        if club in self.lista_clubes:
            self.lista_clubes.remove(club)
            print(f"El socio se desasoció del club {club.nombre}.")
        else:
            print("El socio no está asociado a ese club.")

#Informar si el socio posee deudas o cuotas sin abonar.
    def informar_socio(self):
        for cuota in self.lista_cuota:
            if not cuota.pagada:
                print("El socio posee cuotas sin abonar.")
            return True
    
        print("El socio no posee deudas.")
        return False
    

#Mostrar la cantidad de cuotas pendientes de pago.
    def cantidad_cuotas(self):
        cantidad = 0
        for cuota in self.lista_cuota:
            if cuota.estado == "pendiente":
                cantidad += 1
    
        print(f"El socio tiene {cantidad} cuota(s) pendiente(s).")
        return cantidad

#Reactivar un socio suspendido para que pueda volver a utilizar los servicios del club.
    def reactivar_socio_suspendido(self):
        if self.estado == "suspendido":
            self.estado = "activado"
            print("El socio fue reactivado y su estado ahora es activo.")
        else:
            print("El socio no está suspendido, no es necesario reactivarlo.")

#Permitir la actualización de la contraseña de acceso al sistema.
    def actualizar_contrasena(self,nueva_contrasena):
        self.__contrasena = nueva_contrasena
    print("contrasena actualizada")

#Verificar los datos de acceso ingresados por el socio al momento de iniciar sesión.
    def verificar_acceso(self, usuario_ingresado, contrasena_ingresada):
        if usuario_ingresado == self.__usuario and contrasena_ingresada == self.__contrasena:
            print("Acceso concedido. Bienvenido/a.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
        return False

asociarte=Socio("10/6/2026","activo","pepito123","12345678")
asociarte.registrar_pago_de_cuota()
asociarte.cambiar_estado()