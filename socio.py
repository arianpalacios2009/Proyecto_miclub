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
    def __init__(self, fechas_inscripcion, estado, usuario, contrasena):
        self.lista_clubes = []       # lista de clubes a los que está asociado el socio
        self.lista_cuota = []        # lista de cuotas del socio (se completará al crear la clase Cuota)

        self.fecha_inscripcion = fechas_inscripcion   # fecha en que se inscribió (DD/MM/AAAA)
        self.estado = estado                           # activo, suspendido o inactivo

        # atributos privados: solo accesibles con getters/setters
        self.__usuario = usuario
        self.__contrasena = contrasena

    # ---------- GETTERS ----------
    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena

    # ---------- SETTERS ----------
    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    # ---------- 7) CAMBIAR ESTADO A SUSPENDIDO ----------
    def cambiar_estado(self):
#verificar que recorra la lista para ver si el tipo de estado 

        self.estado = "suspendido"     # pasa el estado del socio a "suspendido"
        print("el estado esta suspendido")

    # ---------- 4) REGISTRAR PAGO DE CUOTA (pendiente de terminar) ----------
    def registrar_pago_de_cuota(self):
#verificar que recorra la lista para ver si el tipo de estado 

        self.estado = "pendiente"
        print("el pago esta pendiente")


    # ---------- 6) CANTIDAD DE CUOTAS PENDIENTES ----------
    def cantidad_cuotas(self):
        cantidad = 0                                # contador, arranca en 0
        for cuota in self.lista_cuota:               # recorremos todas las cuotas
            if cuota.estado == "pendiente":            # si esa cuota está pendiente
                cantidad += 1                            # sumamos 1 al contador
        print(f"El socio tiene {cantidad} cuota(s) pendiente(s).")
        return cantidad


    # ---------- 9) ACTUALIZAR CONTRASEÑA ----------
    def actualizar_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        print("Contraseña actualizada.")

    # ---------- 10) VERIFICAR CREDENCIALES DE ACCESO ----------
    def verificar_acceso(self, usuario_ingresado, contrasena_ingresada):
        # "and" exige que las DOS condiciones sean verdaderas para dar acceso
        if usuario_ingresado == self.__usuario and contrasena_ingresada == self.__contrasena:
            print("Acceso concedido. Bienvenido/a.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False   # también corregido: ahora queda adentro del "else"


asociarte = Socio("10/6/2026", "activo", "pepito123", "12345678")
asociarte.registrar_pago_de_cuota()
asociarte.cambiar_estado()