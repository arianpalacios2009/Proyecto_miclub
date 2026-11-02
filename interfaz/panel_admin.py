import tkinter as tk
from tkinter import ttk

class PanelAdmin(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Administrador")
        self.geometry("400x300")
        self.socio = socio
        
        administrador=ttk.Label(self, text=f"Administrador: {socio.nombre_completo}")
        administrador.pack(pady=20)
        panel_gestion=ttk.Label(self, text="Panel de gestión de socios")
        panel_gestion.pack()
        boton_cerrar=ttk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack(pady=20)
