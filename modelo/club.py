
from datetime import date


class Club:

    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion

        # atributos privados
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion

    # getters
    def get_presidente(self):
        return self.__presidente

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    # setters
    def set_presidente(self, presidente):
        self.__presidente = presidente

    def set_fecha_fundacion(self, fecha):
        self.__fecha_fundacion = fecha

    # Mostrar información
    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre}"
            f"Descripción: {self.descripcion}"
            f"Ubicación: {self.ubicacion}"
            f"Presidente: {self.get_presidente()}"
            f"Fecha de fundación: {self.get_fecha_fundacion()}"
            f"Antigüedad: {self.antiguedad()} años"
        )

    # Calcular la antigüedad del club
    def antiguedad(self):
        hoy = date.today()
        años = hoy.year - self.__fecha_fundacion.year

        if (hoy.month, hoy.day) < (self.__fecha_fundacion.month, self.__fecha_fundacion.day):
            años -= 1

        return años

    # Mostrar año de antigüedad
    def mostrar_anio_antiguedad(self):
        return (
            f"El club {self.nombre} tiene {self.antiguedad()} años de antigüedad "
            f"(fundado el {self.__fecha_fundacion.strftime('%d/%m/%Y')})."
        )

    # Determinar si el club es histórico
    def determinar_club(self):
        if self.antiguedad() >= 50:
            return "Es una institución histórica."
        else:
            return "No es una institución histórica."

    # Permitir modificar el presidente del club
    def cambiar_presidente(self, nuevo_presidente):
        anterior = self.__presidente
        self.__presidente = nuevo_presidente
        return (
            f"Cambio de autoridades: {anterior} no es mas presidente, "
            f"el nuevo presidente de ahora en adelante es {nuevo_presidente}"
        )