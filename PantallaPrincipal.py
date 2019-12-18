from tkinter import Tk, PhotoImage, Frame, Label
from ClockToolbar import ClockToolbar as Toolbar
from R import *

class PantallaInicio(Tk):
    def __init__(self, main):
        super().__init__()
        self.config(cursor='', bg=BG)
        #Para pantalla completa
        #self.attributes('-fullscreen', True)
        #Para eliminar el marco de la ventana
        #self.overrideredirect(True)

        self.IMG_BUTTON_ON = PhotoImage(file='images/boton_on.png')
        self.IMG_BUTTON_OFF = PhotoImage(file='images/boton_off.png')
        self.IMG_BUTTON_DISABLED = PhotoImage(file='images/boton_disabled.png')

        self.toolbar = Toolbar(self, BG)

        self.marco = Frame(self, bg=BG, pady=50)
        self.marco.pack(fill='both', expand=1)

        self.lblBoton = Label(self.marco, image=self.IMG_BUTTON_ON, bg=BG)
        self.lblBoton.bind('<Button-1>', self.onOffButtonClic)
        self.lblBoton.pack(anchor='center')

        self.lblEspacio = Label(self.marco, bg=BG)
        self.lblEspacio.pack()

        self.lblMensaje = Label(self.marco, font=("", "22"), bg=BG, fg="white")
        self.lblMensaje.config(width="50")
        self.lblMensaje.pack(anchor='center')