
import tkinter as tk
from tkinter import messagebox

from servicios.servicio_autenticacion import autenticar

azul = "#022364"
amarillo = "#F7A600"
blanco = "#FFFFFFFF"
texto = "#000000"



class VentanaLogin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Boca Juniors - Inicio de sesión")
        self.geometry("800x550")
        self.configure(bg="#022364")

        # Encabezado
        encabezado = tk.Frame(self, bg=azul, height=90)
        encabezado.pack(fill="x")

        tk.Label(
        encabezado,
        text="BOCA JUNIORS",
        font=("Arial", 24, "bold"),
        bg=azul,
        fg=amarillo
    ).pack(pady=25)
