from pathlib import Path

NOMBRE_CLUB = "BOCA JUNIORS"
LEMA_CLUB = "CLUB ATLÉTICO BOCA JUNIORS"
SUBTITULO = "Sistema de gestión del club"
ETIQUETA = "Socios | Cuotas | Clubes"

# Paleta inspirada en Boca Juniors
PRIMARIO = "#002364"           # Azul Boca oficial (Pantone 287 C): encabezado y botones
PRIMARIO_HOVER = "#103F79"     # Azul más claro para el efecto hover
SECUNDARIO = "#F7A600"         # Oro Boca oficial (Pantone 7409 C): detalles o bordes destacados

PANEL = "#F4F6FA"              # Blanco azulado muy suave para el menú lateral y contenido
FONDO = "#E6ECF5"              # Gris azulado claro detrás de todo
TEXTO = "#081226"              # Azul casi negro para textos sobre fondos claros (mejor armonía que el negro puro)
TEXTO_CLARO = "#F7A600"        # Dorado Boca para el texto sobre el azul principal (o "#FFFFFF" si prefieres blanco puro)
FILA_PAR = "#EBF0F7"           # Rayado azul muy tenue para las filas pares de las tablas

# Colores de estado 
ESTADO_ACTIVO = "#1E7A1E"      # Verde para socios/cuotas activas
ESTADO_SUSPENDIDO = "#B00020"  # Rojo para socios suspendidos
ESTADO_VENCIDO = "#B00020"     # Rojo para cuotas vencidas
ESTADO_PENDIENTE = "#D98A00"   # Dorado oscuro/ámbar para cuotas pendientes

FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_GRANDE = ("Arial", 30, "bold")
FUENTE_SUBTITULO = ("Arial", 16, "bold")
FUENTE = ("Arial", 11)
FUENTE_NEGRITA = ("Arial", 11, "bold")
FUENTE_CHICA = ("Arial", 10)
FUENTE_MENU = ("Arial", 11)
FUENTE_TABLA = ("Arial", 10)

RUTA_LOGO = Path(__file__).parent.parent / "logo.png"
