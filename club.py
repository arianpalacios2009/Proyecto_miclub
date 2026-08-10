
#a) Crear el archivo club.py con la clase Club:
#Atributos:

#● nombre
#● descripcion
#● ubicacion
#● __presidente
#● __fecha_fundacion

#Métodos:

#● mostrar_info()
#● getters y setters

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
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Ubicación:", self.ubicacion)
        print("Presidente:", self.get_presidente())
        print("Fecha de fundación:", self.get_fecha_fundacion())
        print("Antigüedad:", self.antiguedad(), "años")

    # Calcular la antigüedad del club
    def antiguedad(self):
        hoy = date.today()
 
        años = hoy.year - self.__fecha_fundacion.year
 
    # Ajuste: si todavía no llegó el mes/día del aniversario este año, resto 1
        if (hoy.month, hoy.day) < (self.__fecha_fundacion.month, self.__fecha_fundacion.day):
            años -= 1
 
        return años
 
    # Mostrar año de antigüedad (método solicitado)
    def mostrar_anio_antiguedad(self):
        #Muestra por pantalla la antigüedad del club calculando los años,transcurridos desde su fecha de fundación hasta la fecha actual.
        print(f"El club {self.nombre} tiene {self.antiguedad()} años de antigüedad "
              f"(fundado el {self.__fecha_fundacion.strftime('%d/%m/%Y')}).")
 
    # Determinar si el club es histórico
    def determinar_club(self):

        if self.antiguedad() >= 50:
            print("Es una institución histórica.")
        else:
            print("No es una institución histórica.")


    #Permitir modificar el presidente del club cuando se produzca un cambio de autoridades.
    def cambiar_presidente(self,nuevo_presidente):
        anterior=self.__presidente
        self.__presidente= nuevo_presidente
        print(f"Cambio de autoridades: {anterior} no es mas presidente,el nuevo presidente de ahora en adelante es {nuevo_presidente}")

club1 = Club("Boca Juniors","Xeneize","Ciudad Autónoma de Buenos Aires","Juan Román Riquelme",date(1905, 4, 3))

club1.mostrar_info()
club1.determinar_club()
club1.cambiar_presidente("marcelo delgado")