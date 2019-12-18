from tkinter import Tk, PhotoImage, Frame, Label
from time import strftime
import locale

IMG_OPTIONS = PhotoImage(file='images/ruleta32.png')

class clock_toolbar(Frame):

    def __init__(self, parent, bg, images):
        locale.setlocale(locale.LC_ALL, 'es-ES')
        super(parent, pady=10, padx=10, bg=bg)
        self.parent = parent
        self.add_components()
        self.actualizarReloj()

    def add_components(self):
        self.clock = Label(self, font=("", "20"), padx=10, bg=self.bg, fg="white")
        self.clock.pack(side='left')

        self.lbl_options = Label(self, image=IMG_OPTIONS, bg=self.bg)
        self.lbl_options.bind('<Button-1>', self.abrirOpciones)
        self.lbl_options.pack(side='right')

    def abrirOpciones(event):
        print('Abriendo opciones')

    def mostrarHora(self):
        self.clock['text'] = strftime('%H:%M:%S ')
        self.actualizarReloj()

    def actualizarReloj(self):
        self.clock.after(1000, self.mostrarHora)