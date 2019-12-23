import R
from tkinter import FLAT, SUNKEN
# from Modulo import Modulo

MODULO_A = 0
MODULO_B = 1


class ControladorArranque:

    def __init__(self, pantalla, state=R.APAGADO, button_blocked=False, msg_salida=R.MSG_VACIO):
        self.state = state
        self.button_blocked = button_blocked
        self.msg_salida = msg_salida
        self.pantalla = pantalla
        self.timer = R.VALOR_INICIAL

        self.boton_on_off = self.pantalla.lblBoton
        self.boton_on_off.bind('<Button-1>', self.on_off_button_click)

        self.boton_opciones = self.pantalla.toolbar.lbl_options_button
        self.boton_opciones.bind('<Button-1>', self.abrir_pantalla_prog)

        self.marco_inicio = self.pantalla.marco
        self.marco_programa = self.pantalla.pantalla_prog

        self.marco_inicial_visible = True

        self.modulos = [
            # Modulo('Módulo A', 17),
            # Modulo('Módulo B', 18)
            'Módulo A',
            'Módulo B'
        ]

    def on_off_button_click(self, event):
        if self.state == R.APAGADO and not self.button_blocked:
            self.encender()
        elif self.state == R.ENCENDIDO and not self.button_blocked:
            self.parar()
        elif self.state == R.ARRANCANDO and not self.button_blocked:
            self.parar()

    def encender(self):
        self.state = R.ARRANCANDO
        self.boton_on_off.config(image=self.pantalla.IMG_BUTTON_OFF)
        self.msg_salida = R.MSG_ARRANCANDO.format(self.modulos[MODULO_A], self.modulos[MODULO_B])
        self.iniciar_contador()
        # self.modulos[MODULO_A].on()

    def parar(self):
        self.state = R.PARANDO
        self.boton_on_off.config(image=self.pantalla.IMG_BUTTON_DISABLED)
        self.msg_salida = R.MSG_PARANDO.format(self.modulos[MODULO_B], self.modulos[MODULO_A])
        self.iniciar_contador()
        # self.modulos[MODULO_B].off()

    def iniciar_contador(self, contador=R.VALOR_INICIAL):
        self.parar_contador()
        segundos = '{:2d}'.format(contador)
        self.pantalla.lblMensaje['text'] = self.msg_salida + R.MSG_CONTADOR.format(segundos)
        if contador > 0:
            self.timer = self.pantalla.lblMensaje.after(1000, self.iniciar_contador, (contador - 1))
        else:
            self.proceso_completado()

    def parar_contador(self):
        if self.timer != R.VALOR_INICIAL:
            self.pantalla.lblMensaje['text'] = R.MSG_VACIO
            self.pantalla.lblMensaje.after_cancel(self.timer)
            self.button_blocked = False

    def proceso_completado(self):

        if self.state == R.ARRANCANDO and not self.button_blocked:
            self.button_blocked = True
            # self.modulos[MODULO_B].on()
            self.pantalla.lblMensaje['text'] = R.MSG_FIN_ARRANQUE
            self.pantalla.lblMensaje.after(1500, self.parar_contador)
            self.state = R.ENCENDIDO

        elif self.state == R.PARANDO and not self.button_blocked:
            self.button_blocked = True
            # self.modulos[MODULO_A].off()
            self.pantalla.lblMensaje['text'] = R.MSG_FIN_PARADA
            self.pantalla.lblMensaje.after(1500, self.parar_contador)
            self.state = R.APAGADO
            self.pantalla.lblBoton.config(image=self.pantalla.IMG_BUTTON_ON)

    def abrir_pantalla_prog(self, event):
        if self.marco_inicial_visible:
            width = self.marco_inicio.winfo_width()
            height = self.marco_inicio.winfo_height()
            self.marco_inicio.pack_forget()
            self.marco_programa.config(width=width, height=height)
            self.marco_programa.pack(fill='both', expand=1)
            self.boton_opciones.config(relief=SUNKEN)
            self.marco_inicial_visible = False
        else:
            self.marco_inicio.pack()
            self.marco_programa.pack_forget()
            self.boton_opciones.config(relief=FLAT)
            self.marco_inicial_visible = True