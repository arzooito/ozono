from tkinter import Tk, PhotoImage, Frame, Label
from view.components.ClockToolbar import ClockToolbar as Toolbar

BG = "slate blue"
IMG_BUTTON_ON_PATH = 'resources/images/boton_on.png'
IMG_BUTTON_OFF_PATH = 'resources/images/boton_off.png'
IMG_BUTTON_DISABLED_PATH = 'resources/images/boton_disabled.png'


class PantallaPrincipal(Tk):
    """Controlador de pantalla principal"""

    def __init__(self):
        super().__init__()
        self.config(cursor='', bg=BG)
        # Para pantalla completa
        # self.attributes('-fullscreen', True)
        # Para eliminar el marco de la ventana
        # self.overrideredirect(True)

        self.IMG_BUTTON_ON = PhotoImage(file=IMG_BUTTON_ON_PATH)
        self.IMG_BUTTON_OFF = PhotoImage(file=IMG_BUTTON_OFF_PATH)
        self.IMG_BUTTON_DISABLED = PhotoImage(file=IMG_BUTTON_DISABLED_PATH)

        self.toolbar = Toolbar(self, BG)

        self.marco = Frame(self, bg=BG, pady=50)
        self.marco.pack(fill='both', expand=1)

        self.lblBoton = Label(self.marco, image=self.IMG_BUTTON_ON, bg=BG)
        self.lblBoton.pack(anchor='center')

        self.lblEspacio = Label(self.marco, bg=BG)
        self.lblEspacio.pack()

        self.lblMensaje = Label(self.marco, font=("", "22"), bg=BG, fg="white")
        self.lblMensaje.config(width="50")
        self.lblMensaje.pack(anchor='center')

