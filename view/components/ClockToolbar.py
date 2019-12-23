from tkinter import PhotoImage, Frame, Label
from view.components.ClockLabel import Clock

IMG_OPTIONS_PATH = 'resources/images/components/ruleta32.png'
IMG_ALARM_PATH = 'resources/images/components/alarm32.png'


class ClockToolbar(Frame):

    def __init__(self, parent, bg):
        self.IMG_OPTIONS = PhotoImage(file=IMG_OPTIONS_PATH)
        self.IMG_ALARM = PhotoImage(file=IMG_ALARM_PATH)
        self.bg = bg
        self.parent = parent

        super().__init__(parent, pady=10, padx=10, bg=bg)
        self.clock = Clock(self, bg)

        self.lbl_options_button = Label(self, image=self.IMG_OPTIONS, bg=self.bg)
        self.lbl_options_button.pack(side='right')

        self.lbl_alarm = Label(self, image=self.IMG_ALARM, bg=self.bg)
        self.lbl_alarm.pack()

        self.pack(fill='x')



