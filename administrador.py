#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters

from club_categoria import ClubDeportivo

class Administrador(ClubDeportivo):
    def __init__(self,nombre,usuario,contrasena):
        self.nombre=nombre
        
        self.listado_socios=[]
        
        
        #atributos privados
        self.__usuario=usuario
        self.__contrasena=contrasena
        
    def get__usuario(self):
        return self.__usuario
    
    def get__contrasena(self):
        return self.__contrasena
    
    def set_usuario(self,usuario):
        self.__usuario=usuario
        
    def set_contrasena(self,contrasena):
        self.__contrasena=contrasena
        
    #Obtener un listado completo de los socios pertenecientes a un club
    # .Registrar nuevos socios en un club.    
    def agregar_lista(self,socio):
        super().__socios.append(socio)
        
    def listado_completo(self):
        for i in super().__socios:
            print("nombre completo: ",i)
        


admin=Administrador("tiziano","tizi123","87654321")
admin.agregar_lista("arian")
admin.agregar_lista("juan")
admin.agregar_lista("pepe")
admin.listado_completo()