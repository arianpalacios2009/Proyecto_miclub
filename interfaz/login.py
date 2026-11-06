
import tkinter as tk
from tkinter import messagebox



from servicios.servicio_autenticacion import autenticar

azul = "#022364"
amarillo = "#F7A600"
blanco = "#FFFFFF"
texto = "#000000"



class VentanaLogin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Boca Juniors - Inicio de sesión")
        self.geometry("800x550")
        self.configure(bg="#022364")

        def inicio_como_socio():

        # Encabezado
            encabezado = tk.Frame(self, bg=azul, height=90)
            encabezado.pack(fill="x")

            tk.Label(encabezado,text="BOCA JUNIORS",font=("Arial", 24, "bold"),bg=azul,fg=amarillo).pack(pady=25)

        #formulario
        tk.Label(self,text="INICIAR SESIÓN",font=("Arial", 20, "bold"),bg=azul,fg=blanco).pack(pady=30)


        #usuario
        tk.Label(self,text="Usuario:", font=("Arial", 12), bg=azul, fg=blanco).pack(pady=5)
        self.entrada_usuario = tk.Entry(self, font=("Arial", 12))
        self.entrada_usuario.pack(pady=5)

        boton_inicio_sesion=tk.Button(self,text="iniciar sesion ",bg=blanco, command=inicio_como_socio)
        boton_inicio_sesion.pack(pady=10)

   


    
#faltaria que cuando hago click en iniciar sesion ,si es un socio deberia redirigir al panel de socio y si es admin redirigir al panel admin

    
