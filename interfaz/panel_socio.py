
import tkinter as tk
from tkinter import ttk
from modelo.socio import Socio

class PanelSocio(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Socio")
        self.geometry("400x300")
        self.socio = socio
        
        bienvenida= ttk.Label(self, text=f"Bienvenido/a: {socio.nombre_completo}")
        bienvenida.pack(pady=20)
        usuario=ttk.Label(self, text=f"Usuario: {socio.get_usuario()}")
        usuario.pack()
        estado=ttk.Label(self, text=f"Estado: {socio.estado}")
        estado.pack()
        rol=ttk.Label(self, text=f"Rol: {socio.rol}")
        rol.pack(pady=10)
        boton_cerrar=ttk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack(pady=20)
