
from datetime import date


class Cuota:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    # GETTER
    def get_estado(self):
        return self.__estado

    # SETTER
    def set_estado(self, estado):
        self.__estado = estado

    # Mostrar los datos de la cuota
    def mostrar(self):
        return (
            f"Estado: {self.__estado} | "
            f"Fecha de vencimiento: "
            f"{self.fecha_de_vencimiento.strftime('%d/%m/%Y')} | "
            f"Periodo: {self.periodo}"
        )

    # Permite mostrar la cuota directamente con print()
    def __str__(self):
        return self.mostrar()

    # Registrar una cuota como pagada
    def pagar_cuota(self):
        self.__estado = "pagada"
        return "La cuota está pagada."

    # Determinar si la cuota está vencida
    def determinar(self):
        hoy = date.today()

        if self.__estado != "pagada" and hoy > self.fecha_de_vencimiento:
            self.__estado = "vencida"
            return True

        return False

    # Actualizar automáticamente el estado
    def actualizar_estado(self):
        self.determinar()

    # Informar los días que faltan para el vencimiento
    def informar_dias_faltantes(self):
        hoy = date.today()
        diferencia = self.fecha_de_vencimiento - hoy
        dias = diferencia.days

        if self.__estado == "pagada":
            return "La cuota ya está pagada."
        elif dias > 0:
            return f"Faltan {dias} días para el vencimiento."
        elif dias == 0:
            return "La cuota vence hoy."
        else:
            self.__estado = "vencida"
            return f"La cuota está vencida hace {abs(dias)} días."

    # Renovar la cuota para un nuevo período
    def renovar_cuota(self):
        mes, anio = map(int, self.periodo.split("/"))

        if mes == 12:
            nuevo_mes = 1
            nuevo_anio = anio + 1
        else:
            nuevo_mes = mes + 1
            nuevo_anio = anio

        dia = self.fecha_de_vencimiento.day

        # Evitar errores con días que no existen en el nuevo mes
        import calendar
        ultimo_dia = calendar.monthrange(nuevo_anio, nuevo_mes)[1]
        dia = min(dia, ultimo_dia)

        nueva_fecha = date(nuevo_anio, nuevo_mes, dia)

        self.fecha_de_vencimiento = nueva_fecha
        self.periodo = f"{nuevo_mes:02d}/{nuevo_anio}"
        self.__estado = "pendiente"

        return (
            f"Cuota renovada. Nuevo período: {self.periodo}, "
            f"vence el {nueva_fecha.strftime('%d/%m/%Y')}"
        )
