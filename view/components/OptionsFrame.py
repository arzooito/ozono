from tkinter import Tk, PhotoImage, Frame, Label
from view.components.TimePicker import TimePicker

class OptionsFrame(Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.picker = TimePicker(self)
        self.picker.pack()