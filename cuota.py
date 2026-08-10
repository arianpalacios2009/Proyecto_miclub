#f) Crear el archivo cuota.py con la clase Cuota:
#Atributos:

#● __estado (pagada, pendiente, vencida)
#● fecha_de_vencimiento
#● periodo (mes/año)

#Métodos:

#● getters y setters
from datetime import date



class Cuota:
    def __init__(self,estado,fecha_de_vencimiento,periodo):
        self.__estado=estado
        self.fecha_de_vencimiento=fecha_de_vencimiento
        self.periodo=periodo
        
    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado):
        self.__estado=estado
    
    def mostrar(self):
        print("estado: ",self.__estado)
        print("fecha de nacimiento: ",self.fecha_de_vencimiento)
        print("periodo: ",self.periodo)
        
    #Registrar una cuota como pagada.
    def pagar_cuota(self):
        self.__estado="pagada"
        print("la cuota esta pagada")
    #Determinar si una cuota se encuentra vencida comparando la fecha de vencimiento con la fecha actual.

    def determinar(self):
        hoy = date.today()
        if self.__estado != "pagada" and hoy > self.fecha_de_vencimiento:
            self.__estado = "vencida"
            return True
        return False

#Actualizar automáticamente el estado de la cuota cuando corresponda.
    def actualizar_estado(self):
         self.determinar()
    
    
#Informar cuántos días faltan para el vencimiento de una cuota.
    def informar_dias_faltantes(self):
        hoy = date.today()
        diferencia = self.fecha_de_vencimiento - hoy
        dias = diferencia.days

        if self.__estado == "pagada":
            print("La cuota ya está pagada.")
        elif dias > 0:
            print(f"Faltan {dias} días para el vencimiento.")
        elif dias == 0:
            print("La cuota vence hoy.")
        else:
            print(f"La cuota está vencida hace {abs(dias)} días.") 
    
#Informar cuántos días faltan para el vencimiento de una cuota.
    def informar_dias_faltantes(self):
        hoy = date.today()
        diferencia = self.fecha_de_vencimiento - hoy
        dias = diferencia.days
 
        if self.__estado == "pagada":
            print("La cuota ya está pagada.")
        elif dias > 0:
            print(f"Faltan {dias} días para el vencimiento.")
        elif dias == 0:
            print("La cuota vence hoy.")
        else:
            print(f"La cuota está vencida hace {abs(dias)} días.")

#Permitir la renovación de una cuota para un nuevo período.
    def renovar_cuota(self):
        mes, anio = map(int, self.periodo.split("/"))

        if mes == 12:
            nuevo_mes = 1
            nuevo_anio = anio + 1
        else:
            nuevo_mes = mes + 1
            nuevo_anio = anio

            dia = self.fecha_de_vencimiento.day
            nueva_fecha = date(nuevo_anio, nuevo_mes, dia)

        self.fecha_de_vencimiento = nueva_fecha
        self.periodo = f"{nuevo_mes:02d}/{nuevo_anio}"
        self.__estado = "pendiente"

        print(f"Cuota renovada. Nuevo período: {self.periodo}, "
            f"vence el {nueva_fecha.strftime('%d/%m/%Y')}")          
 
pagar=Cuota("pendiente", date(2026,8,1), "08/2026")
pagar.mostrar()
pagar.set_estado("pagada")
pagar.mostrar()
pagar.pagar_cuota()
pagar.determinar()
pagar.actualizar_estado()
pagar.informar_dias_faltantes()
pagar.renovar_cuota()