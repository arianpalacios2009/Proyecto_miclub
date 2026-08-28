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
        self.estado = "suspendido"     # pasa el estado del socio a "suspendido"
        print("el estado esta suspendido")

    # ---------- 4) REGISTRAR PAGO DE CUOTA (pendiente de terminar) ----------
    # NOTA: esto todavía no cumple bien la consigna. Está usando self.estado
    # (que es el estado del SOCIO: activo/suspendido/inactivo) para guardar
    # algo que en realidad pertenece a una CUOTA. Falta la clase Cuota para
    # poder resolverlo correctamente (buscar la cuota en self.lista_cuota
    # y marcarla como pagada, en vez de tocar self.estado).
    def registrar_pago_de_cuota(self):
        self.estado = "pendiente"
        print("el pago esta pendiente")

    # ---------- 1) ASOCIARSE A UNO O MÁS CLUBES ----------
    def asociar_club(self, club):
        if club not in self.lista_clubes:        # evita agregar el mismo club dos veces
            self.lista_clubes.append(club)
            print(f"El socio se asoció al club {club.nombre}.")
        else:
            print("El socio ya está asociado a ese club.")

    # ---------- 2) DEJAR DE PERTENECER A UN CLUB ----------
    def dejar_club(self, club):
        if club in self.lista_clubes:             # solo saca el club si realmente está en la lista
            self.lista_clubes.remove(club)
            print(f"El socio se desasoció del club {club.nombre}.")
        else:
            print("El socio no está asociado a ese club.")

    # ---------- 5) INFORMAR SI TIENE DEUDAS ----------
    def informar_socio(self):
        for cuota in self.lista_cuota:            # recorremos todas las cuotas del socio
            if not cuota.pagada:                   # si encontramos UNA que no está pagada...
                print("El socio posee cuotas sin abonar.")
                # CORREGIDO: antes el "return True" estaba afuera del "if",
                # entonces cortaba en la primera vuelta del for sin importar
                # si esa cuota estaba pagada o no. Ahora sí queda adentro del "if",
                # así solo corta cuando realmente encontró una deuda.
                return True
        print("El socio no posee deudas.")
        return False   # si el for termina sin encontrar ninguna deuda, no debe nada

    # ---------- 6) CANTIDAD DE CUOTAS PENDIENTES ----------
    def cantidad_cuotas(self):
        cantidad = 0                                # contador, arranca en 0
        for cuota in self.lista_cuota:               # recorremos todas las cuotas
            if cuota.estado == "pendiente":            # si esa cuota está pendiente
                cantidad += 1                            # sumamos 1 al contador
        print(f"El socio tiene {cantidad} cuota(s) pendiente(s).")
        return cantidad

    # ---------- 8) REACTIVAR SOCIO SUSPENDIDO ----------
    def reactivar_socio_suspendido(self):
        if self.estado == "suspendido":            # solo reactiva si realmente estaba suspendido
            # CORREGIDO: antes decía "activado", que no coincide con el resto
            # del código (cambiar_estado usa "suspendido", y en otros lados
            # se compara contra "activo"). Ahora queda consistente.
            self.estado = "activo"
            print("El socio fue reactivado y su estado ahora es activo.")
        else:
            print("El socio no está suspendido, no es necesario reactivarlo.")

    # ---------- 9) ACTUALIZAR CONTRASEÑA ----------
    def actualizar_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        # CORREGIDO: antes este print() estaba escrito con 0 espacios de
        # indentación, entonces quedaba AFUERA del método por completo.
        # Eso hacía que se ejecutara una sola vez, al definirse la clase,
        # en vez de ejecutarse cada vez que se llama al método.
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