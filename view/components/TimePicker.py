from tkinter import Entry, PhotoImage, Frame, Label

IMG_ARROW_UP_PATH = 'resources/images/components/flecha-up64.png'
IMG_ARROW_DOWN_PATH = 'resources/images/components/flecha-down64.png'


class TimePicker(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg=parent['bg'])

        self.IMG_ARROW_UP = PhotoImage(file=IMG_ARROW_UP_PATH)
        self.IMG_ARROW_DOWN = PhotoImage(file=IMG_ARROW_DOWN_PATH)

        self.hours_spinner = Frame(self)
        self.hours_up = Label(self.hours_spinner, image=self.IMG_ARROW_UP, bg=parent['bg'])
        self.hours_up.pack()

        self.hours_textbox = Entry(self.hours_spinner, bg=parent['bg'], fg="white", font=("", "22"))
        self.hours_up.pack()

        self.hours_down = Label(self.hours_spinner, image=self.IMG_ARROW_DOWN, bg=parent['bg'])
        self.hours_down.pack()

        self.hours_spinner.pack()