#b) Crear el archivo clubCategoria.py con la subclase ClubCategoria (la categoría que ustedes
#quieran, por ejemplo: ClubRecreativo) que hereda de Club:
#Atributos:

#● __socios (lista de socios)
#● actividades (lista de actividades)

#Métodos:

#● getters y setters

from club import Club   # importamos la clase Club, porque ClubDeportivo va a heredar de ella

class ClubDeportivo(Club):   # ClubDeportivo hereda todo lo que ya tiene Club (nombre, presidente, etc.)

    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios, actividades):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []       # lista privada (doble guión bajo): solo se toca desde adentro de la clase
        self.__actividades = []    # lista pública: se puede leer/modificar directamente desde afuera

    # ---------- GETTERS ----------
    def get_socios(self):
        return self.__socios      # devuelve la lista de socios (para poder leerla desde afuera)

    def get_actividades(self):
        return self.__actividades   # devuelve la lista de actividades

    # ---------- SETTERS ----------
    def set_socios(self, socios):
        self.__socios = socios    # reemplaza toda la lista de socios por una nueva

    def set_actividades(self, actividades):
        self.__actividades = actividades   # reemplaza toda la lista de actividades por una nueva

    # ---------- MOSTRAR DATOS DEL CLUB ----------
    def mostrar(self):
        print("Nombre:", self.nombre)                    # atributo heredado de Club (público)
        print("Descripcion:", self.descripcion)           # atributo heredado de Club (público)
        print("Ubicacion:", self.ubicacion)                # atributo heredado de Club (público)
        print("Presidente:", self.get_presidente())        # usamos el getter heredado de Club
        print("Fundacion:", self.get_fecha_fundacion())    # usamos el getter heredado de Club
        print("socios:", self.__socios)                    # lista de socios de ESTA categoría
        print("actividades:", self.actividades)            # lista de actividades de ESTA categoría

    # ---------- 1) REGISTRAR NUEVOS SOCIOS ----------
    def registrar_socios(self, socio, activo=True):
        # guardamos si el socio arranca activo o no, como un atributo dentro del objeto socio

#verificar si el socio esta dentro de la lista con una condicion

        socio.activo = activo
        self.__socios.append(socio)   # agregamos el objeto socio al final de la lista
        print("Se agregó el socio.")

    # ---------- 2) ELIMINAR SOCIOS ----------
    def eliminar_socios(self, socio):
        if socio in self.__socios:              # chequeamos que el socio realmente esté en la lista
            self.__socios.remove(socio)          # si está, lo sacamos
            print(f"Socio '{socio.get_socios()}' eliminado de la categoría {self.nombre}.")
        else:
            print("Ese socio no pertenece a esta categoría.")   # si no estaba, avisamos

    # ---------- 3) LOCALIZAR SOCIO POR IDENTIFICACIÓN ----------
    def localizar_socio_con_identificacion(self, usuario):
        for socio in self.__socios:                     # recorremos cada socio de la lista
            if socio.get_socios() == usuario:            # comparamos su usuario con el buscado
                print(f"Socio encontrado: usuario '{usuario}'.")
                return socio                               # cortamos apenas lo encontramos y lo devolvemos
        print(f"No se encontró ningún socio con usuario '{usuario}'.")
        return None    # si el for termina sin encontrarlo, devolvemos None

    # ---------- 4) CANTIDAD TOTAL DE SOCIOS ----------
    def cantidad_socio(self):
        return len(self.__socios)    # len() cuenta cuántos elementos tiene la lista

    # ---------- 5) AGREGAR NUEVA ACTIVIDAD ----------
    def actividad_nueva(self, actividad):

#consultar primero si existe la actividad 

        self.__actividades.append(actividad)   # agregamos la actividad al final de la lista
        print("Agregando actividad nueva.")

    # ---------- 6) ELIMINAR ACTIVIDAD ----------
    def eliminar_actividad(self, actividad):
        if actividad in self.__actividades:               # chequeamos que exista en la lista
            self.__actividades.remove(actividad)            # si existe, la sacamos
            print(f"Actividad '{actividad}' eliminada de la categoría {self.nombre}.")
        else:
            print(f"La actividad '{actividad}' no existe en esta categoría.")

    # ---------- 7) LISTADO DE ACTIVIDADES ----------
    def mostrar_actividades(self):
        for i in self.__actividades:   # recorremos toda la lista de actividades
            print(i)                  # imprimimos cada una

    # ---------- 8) PORCENTAJE DE SOCIOS ACTIVOS ----------
    def calcular_porcentaje(self):
        if not self.__socios:               # si la lista está vacía, evitamos dividir por cero
            return 0.0

        activos = 0                          # contador, arranca en 0
        for socio in self.__socios:           # recorremos todos los socios
            if socio.activo:                   # si ese socio está marcado como activo
                activos += 1                     # sumamos 1 al contador

        return (activos * 100) / len(self.__socios)   # regla de 3: (activos * 100) / total


club_boca = ClubDeportivo(
    "Boca juniors",                     # nombre
    "Gigante del fútbol mundial, apodado Xeneize. Famoso por su estadio La Bombonera "
    "y su enorme identidad popular.",    # descripcion
    "Barrio de La Boca, Buenos Aires, Argentina",   # ubicacion
    "Juan Román Riquelme",               # presidente
    "3 de abril de 1905",                # fecha_fundacion
    [],                                   # socios (se ignora, siempre arranca vacío)
    []                                    # actividades (se ignora, siempre arranca vacío)
)

club_boca.mostrar()   # imprime todos los datos del club recién creado