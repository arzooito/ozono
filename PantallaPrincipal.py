from tkinter import Tk, PhotoImage, Frame, Label
from ClockToolbar import ClockToolbar as Toolbar
import R

BG = "slate blue"
IMG_BUTTON_ON_PATH = 'images/boton_on.png'
IMG_BUTTON_OFF_PATH = 'images/boton_off.png'
IMG_BUTTON_DISABLED_PATH = 'images/boton_disabled.png'


class PantallaPrincipal(Tk):

    IMG_BUTTON_ON = PhotoImage(file=IMG_BUTTON_ON_PATH)
    IMG_BUTTON_OFF = PhotoImage(file=IMG_BUTTON_OFF_PATH)
    IMG_BUTTON_DISABLED = PhotoImage(file=IMG_BUTTON_DISABLED_PATH)

    def __init__(self, funcion_boton):
        super().__init__()
        self.funcion_boton = funcion_boton
        self.config(cursor='', bg=BG)
        # Para pantalla completa
        # self.attributes('-fullscreen', True)
        # Para eliminar el marco de la ventana
        # self.overrideredirect(True)

        self.toolbar = Toolbar(self, BG)

        self.marco = Frame(self, bg=BG, pady=50)
        self.marco.pack(fill='both', expand=1)

        self.lblBoton = Label(self.marco, image=self.IMG_BUTTON_ON, bg=BG)
        self.lblBoton.bind('<Button-1>', self.button_click)
        self.lblBoton.pack(anchor='center')

        self.lblEspacio = Label(self.marco, bg=BG)
        self.lblEspacio.pack()

        self.lblMensaje = Label(self.marco, font=("", "22"), bg=BG, fg="white")
        self.lblMensaje.config(width="50")
        self.lblMensaje.pack(anchor='center')

    def button_click(self, event):
        estado = self.funcion_boton()
        if R.ARRANCANDO == estado:
            event.widget.config(image=self.IMG_BUTTON_OFF)
        elif R.PARANDO:
            event.widget.config(image=self.IMG_BUTTON_DISABLED)

        iniciarContador()
