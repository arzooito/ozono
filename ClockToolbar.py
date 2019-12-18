from tkinter import PhotoImage, Frame, Label
from ClockLabel import Clock

IMG_OPTIONS_PATH = 'images/ruleta32.png'
IMG_ALARM_PATH = 'images/alarm32.png'


class ClockToolbar(Frame):

    def __init__(self, parent, bg):
        self.visible = True
        self.IMG_OPTIONS = PhotoImage(file=IMG_OPTIONS_PATH)
        self.IMG_ALARM = PhotoImage(file=IMG_ALARM_PATH)
        self.bg = bg
        self.parent = parent

        super().__init__(parent, pady=10, padx=10, bg=bg)
        self.clock = Clock(self, bg)

        self.lbl_options = Label(self, image=self.IMG_OPTIONS, bg=self.bg)
        self.lbl_options.bind('<Button-1>', self.abrir_opciones)
        self.lbl_options.pack(side='right')

        self.lbl_alarm = Label(self, image=self.IMG_ALARM, bg=self.bg)
        self.lbl_alarm.pack()

        self.pack(fill='x')

    def abrir_opciones(self, event):
        if self.visible:
            self.lbl_alarm.pack_forget()
            self.visible = False
            print('Ocultando alarma')
        else:
            self.lbl_alarm.pack()
            self.visible = True
            print('Mostrando alarma')

