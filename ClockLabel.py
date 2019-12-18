from tkinter import Label
from time import strftime
import locale

class Clock(Label):
    def __init__(self, parent, bg):
        locale.setlocale(locale.LC_ALL, 'es-ES')
        self.bg = bg
        self.parent = parent
        super().__init__(parent, font=("", "20"), padx=10, bg=self.bg, fg="white")
        self.pack(side='left')

        self.mostrar_hora()

    def mostrar_hora(self):
        self['text'] = strftime('%H:%M:%S | %a, %d de %B')
        self.actualizar_reloj()

    def actualizar_reloj(self):
        self.after(1000, self.mostrar_hora)
