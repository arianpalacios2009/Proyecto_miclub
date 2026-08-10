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
    def __init__(self,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad):
        self.nombre=nombre_completo
        self.edad=edad
        
        #atributos privado
        self.__tipo_identificacion=tipo_identificacion
        self.__identificacion=identificacion
        self.__nacionalidad=nacionalidad
        
        

    #getters    
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion
    
    def get_identificacion(self):
        return self.__identificacion
    
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    #setters
    
    def set_tipo_identificacion(self,tipo_identificacion):
        self._tipo_identificacion=tipo_identificacion
        
    def set_identificacion(self,identificacion):
        self.__identificacion=identificacion
        
    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad=nacionalidad
        
    #Determinar automáticamente si una persona es mayor o menor de edad.
    def es_mayor_edad(self):
        if  self.edad >= 18:
            print("es mayor de edad")
        else:
            print("es menor de edad")
    
    def verificar_identificacion(self):
        if len(self.__identificacion) == 8:
            print("La identificacion es valida")
        else:
            print("No es valida")


    def mostrar_datos(self):
        print("nombre_completo: ",self.nombre)
        print("edad: ",self.edad)
        print("tipo_identificacion: ",self.get_identificacion())
        print("identificacion: ",self.get_identificacion())
        print("nacionalidad: ",self.get_nacionalidad())
        
    


persona=Persona("juan",20,"Dni ","32400127","Argentina")
persona.verificar_identificacion()
persona.mostrar_datos()
persona.es_mayor_edad()