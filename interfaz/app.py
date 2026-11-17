
import tkinter as tk
from tkinter import ttk

from interfaz.login import PantallaLogin
from interfaz.panel_admin import PanelAdmin
from interfaz.panel_socio import PanelSocio
from interfaz.tema import (
    ETIQUETA,
    FONDO,
    FUENTE,
    FUENTE_GRANDE,
    FUENTE_MENU,
    FUENTE_NEGRITA,
    FUENTE_SUBTITULO,
    FUENTE_TABLA,
    LEMA_CLUB,
    NOMBRE_CLUB,
    PANEL,
    PRIMARIO,
    PRIMARIO_HOVER,
    RUTA_LOGO,
    SUBTITULO,
    TEXTO,
    TEXTO_CLARO,
)


class ClubApp(tk.Tk):
    """Ventana única que arma el encabezado, el menú y las pantallas."""

    def __init__(self):
        super().__init__()
        self.socio_actual = None
        self.panel = None

        self.title(f"{NOMBRE_CLUB} | Sistema del club")
        self.geometry("950x650")
        self.minsize(850, 550)
        self.configure(bg=FONDO)

        self._estilizar_tablas()
        self._crear_encabezado()
        self._crear_cuerpo()
        self.mostrar_bienvenida()

        self.protocol("WM_DELETE_WINDOW", self.salir)

    def _estilizar_tablas(self):
        estilo = ttk.Style(self)
        estilo.configure(
            "Club.Treeview",
            background=PANEL,
            fieldbackground=PANEL,
            foreground=TEXTO,
            rowheight=28,
            font=FUENTE_TABLA
        )
        estilo.configure(
            "Club.Treeview.Heading",
            background=PRIMARIO,
            foreground=TEXTO_CLARO,
            font=FUENTE_NEGRITA,
            relief="flat"
        )
        estilo.map(
            "Club.Treeview",
            background=[("selected", PRIMARIO_HOVER)],
            foreground=[("selected", TEXTO_CLARO)]
        )

    def _crear_encabezado(self):
        encabezado = tk.Frame(self, bg=PRIMARIO, height=85)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        self._logo = None
        self._logo_encabezado = None
        self._logo_bienvenida = None

        if RUTA_LOGO.exists():
            self._logo = tk.PhotoImage(file=str(RUTA_LOGO))

            ancho = self._logo.width()
            alto = self._logo.height()
            lado_mayor = max(ancho, alto)

            factor_encabezado = max(1, (lado_mayor + 59) // 60)
            factor_bienvenida = max(1, (lado_mayor + 249) // 250)

            self._logo_encabezado = self._logo.subsample(
                factor_encabezado,
                factor_encabezado
            )

            self._logo_bienvenida = self._logo.subsample(
                factor_bienvenida,
                factor_bienvenida
            )

            tk.Label(
                encabezado,
                image=self._logo_encabezado,
                bg=PRIMARIO
            ).pack(side="left", padx=25, pady=10)

        else:
            tk.Label(
                encabezado,
                text=NOMBRE_CLUB,
                font=FUENTE_SUBTITULO,
                bg=PRIMARIO,
                fg=TEXTO_CLARO
            ).pack(side="left", padx=25, pady=15)

        tk.Label(
            encabezado,
            text=LEMA_CLUB,
            font=FUENTE_NEGRITA,
            bg=PRIMARIO,
            fg=TEXTO_CLARO
        ).pack(side="right", padx=25)

    def _crear_cuerpo(self):
        principal = tk.Frame(self, bg=FONDO)
        principal.pack(fill="both", expand=True)

        self.menu = tk.Frame(principal, bg=PANEL, width=210)
        self.menu.pack_propagate(False)

        self.contenido = tk.Frame(principal, bg=PANEL)

    def limpiar_contenido(self):
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    def ocultar_menu(self):
        self.menu.pack_forget()
        self.contenido.pack_forget()
        self.contenido.pack(fill="both", expand=True)

    def mostrar_menu(self, panel):
        for elemento in self.menu.winfo_children():
            elemento.destroy()

        tk.Label(
            self.menu,
            text="MENÚ PRINCIPAL",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=PRIMARIO
        ).pack(pady=(25, 15))

        for texto, comando in panel.botones_menu():
            self.crear_boton_menu(texto, comando)

        self.contenido.pack_forget()
        self.menu.pack(side="left", fill="y")
        self.contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=12,
            pady=12
        )

    def crear_boton_menu(self, texto, comando):
        tk.Button(
            self.menu,
            text=texto,
            command=comando,
            font=FUENTE_MENU,
            bg=PANEL,
            fg=TEXTO,
            activebackground=PRIMARIO,
            activeforeground=TEXTO_CLARO,
            relief="flat",
            anchor="w",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(fill="x", padx=8, pady=3)

    def crear_boton(self, padre, texto, comando, ancho=25, borde=False):
        return tk.Button(
            padre,
            text=texto,
            command=comando,
            bg=PRIMARIO,
            fg=TEXTO_CLARO,
            font=FUENTE_NEGRITA,
            width=ancho,
            relief="solid" if borde else "flat",
            bd=1 if borde else 0,
            cursor="hand2"
        )

    def mostrar_bienvenida(self):
        self.limpiar_contenido()
        self.ocultar_menu()

        fila_titulo = tk.Frame(self.contenido, bg=PANEL)
        fila_titulo.pack(pady=(65, 10))

        if self._logo_bienvenida is not None:
            tk.Label(
                fila_titulo,
                image=self._logo_bienvenida,
                bg=PANEL
            ).pack(side="left", padx=10)

        tk.Label(
            fila_titulo,
            text=NOMBRE_CLUB,
            font=FUENTE_GRANDE,
            bg=PANEL,
            fg=PRIMARIO
        ).pack(side="left", padx=10)

        tk.Label(
            self.contenido,
            text=f"CLUB {NOMBRE_CLUB}",
            font=FUENTE_SUBTITULO,
            bg=PANEL,
            fg=TEXTO
        ).pack(pady=5)

        tk.Label(
            self.contenido,
            text=SUBTITULO,
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO
        ).pack(pady=5)

        tk.Label(
            self.contenido,
            text=ETIQUETA,
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO
        ).pack(pady=10)

        self.crear_boton(
            self.contenido,
            "INICIAR SESIÓN",
            self.mostrar_login,
            ancho=25
        ).pack(pady=(30, 10))

        boton_salir = self.crear_boton(
            self.contenido,
            "SALIR",
            self.salir,
            ancho=25,
            borde=True
        )
        boton_salir.config(bg=PANEL, fg=PRIMARIO)
        boton_salir.pack(pady=5)

    def mostrar_login(self):
        self.limpiar_contenido()
        self.ocultar_menu()
        PantallaLogin(self.contenido, self)

    def iniciar_sesion(self, socio):
        self.limpiar_contenido()
        self.socio_actual = socio

        if socio.es_admin():
            self.panel = PanelAdmin(self, socio)
        else:
            self.panel = PanelSocio(self, socio)

        self.mostrar_menu(self.panel)
        self.panel.mostrar_inicio()

    def cerrar_sesion(self):
        self.socio_actual = None
        self.panel = None
        self.mostrar_bienvenida()

    def salir(self):
        self.destroy()
