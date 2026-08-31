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

class Persona():
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre = nombre_completo   
        self.edad = edad

        # atributos privados (doble guión bajo): solo se acceden con getters/setters
        self.__tipo_identificacion = tipo_identificacion   # ej: "DNI", "Pasaporte"
        self.__identificacion = identificacion             # el número/código en sí
        self.__nacionalidad = nacionalidad

    # ---------- GETTERS ----------
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion   # devuelve el tipo (DNI, Pasaporte, etc.)

    def get_identificacion(self):
        return self.__identificacion        # devuelve el número de identificación

    def get_nacionalidad(self):
        return self.__nacionalidad          # devuelve la nacionalidad

    # ---------- SETTERS ----------
    def set_tipo_identificacion(self, tipo_identificacion):
        
        self.__tipo_identificacion = tipo_identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion   # reemplaza el número de identificación

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad        # reemplaza la nacionalidad

    # ---------- 1) DETERMINAR MAYOR/MENOR DE EDAD ----------
    def es_mayor_edad(self):
        if self.edad >= 18:              # si tiene 18 años o más
            print("es mayor de edad")
        else:                             # si tiene menos de 18
            print("es menor de edad")

    # ---------- MOSTRAR TODOS LOS DATOS ----------
    def mostrar_datos(self):
        print("nombre_completo: ", self.nombre)
        print("edad: ", self.edad)
        print("tipo_identificacion: ", self.get_tipo_identificacion())
        print("identificacion: ", self.get_identificacion())
        print("nacionalidad: ", self.get_nacionalidad())

    # ---------- 2) VERIFICAR IDENTIFICACIÓN VÁLIDA ----------
    def verificar_identificacion(self):
       
        if self.__identificacion is None or str(self.__identificacion).strip() == "":
            print("La identificación no es válida (está vacía).")
            return False

        print("La identificación es válida.")
        return True


persona = Persona("arian", 16, "Dni ", "32400127", "Argentina")
persona.verificar_identificacion()
persona.mostrar_datos()
persona.es_mayor_edad()