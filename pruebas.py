from modelo.club import Club
from datetime import date

club1 = Club("Boca Juniors", "Xeneize", "Ciudad Autónoma de Buenos Aires", "Juan Román Riquelme", date(1905, 4, 3))
print(club1.mostrar_info())
print(club1.determinar_club())
print(club1.cambiar_presidente("marcelo delgado"))



from modelo.cuota import Cuota
from datetime import date

cuota1 = Cuota("pendiente", date(2026, 8, 1), "08/2026")
print(cuota1.mostrar())
cuota1.set_estado("pagada")
print(cuota1.mostrar())
print(cuota1.pagar_cuota())
print(cuota1.determinar())
print(cuota1.actualizar_estado())
print(cuota1.informar_dias_faltantes())
print(cuota1.renovar_cuota())


from modelo.persona import Persona

persona1 = Persona("Arian ", 16 , " DNI ", " 32400127 ", " Argentina ")
print(persona1.verificar_identificacion())
print(persona1.mostrar_datos())
print(persona1.es_mayor_edad())


from modelo.socio import Socio

socio1 = Socio(" Pepito ", 30 , " DNI ", " 40111222 ", " Argentina "," 10/06/2026 ", " activo ", " pepito123 ", " 12345678 ", rol="socio" )

print(socio1.mostrar_datos())      
print(socio1.registrar_pago_de_cuota())
print(socio1.cambiar_estado())
print("¿Es admin?:", socio1.es_admin())
print(socio1.verificar_acceso("pepito123", "12345678"))
