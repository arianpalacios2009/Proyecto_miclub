#c) Crear el archivo persona.py con la clase Persona:
#Atributos:

#● nombre_completo
#● edad
#● __tipo_identificacion (DNI, Pasaporte, Cédula de identidad)
#● __identificacion
#● __nacionalidad

#Métodos:

#● mostrar_datos()
#● getters y setters
#c) Crear el archivo persona.py con la clase Persona:
#Atributos:

#● nombre_completo
#● edad
#● __tipo_identificacion (DNI, Pasaporte, Cédula de identidad)
#● __identificacion
#● __nacionalidad

#Métodos:

#● mostrar_datos()
#● getters y setters
# persona.py

class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre = nombre_completo
        self.edad = edad

        # atributos privados
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    # ---------- GETTERS ----------
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion

    def get_identificacion(self):
        return self.__identificacion

    def get_nacionalidad(self):
        return self.__nacionalidad

    # ---------- SETTERS ----------
    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # ---------- MAYOR/MENOR DE EDAD ----------
    def es_mayor_edad(self):
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "es menor de edad"

    # ---------- MOSTRAR DATOS ----------
    def mostrar_datos(self):
        return (
            f"nombre_completo: {self.nombre}"
            f"edad: {self.edad}"
            f"tipo_identificacion: {self.get_tipo_identificacion()}"
            f"identificacion: {self.get_identificacion()}"
            f"nacionalidad: {self.get_nacionalidad()}"
        )

    # ---------- VERIFICAR IDENTIFICACIÓN VÁLIDA ----------
    def verificar_identificacion(self):
        if self.__identificacion is None or str(self.__identificacion).strip() == "":
            return False
        return True