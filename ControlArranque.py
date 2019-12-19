import R
from Modulo import Modulo

MODULO_A = 0
MODULO_B = 1

MSG_ARRANCANDO = '{} conectado, arrancando {} en {} s'
MSG_PARANDO = '{} desconectado, parando {} en {} s'
MSG_FIN_ARRANQUE = 'Arranque completo'
MSG_FIN_PARADA = 'Parada completa'
MSG_VACIO = ''

class ControladorArranque:

    def __init__(self, pantalla, state=R.APAGADO, button_blocked=False, msg_salida=R.MSG_VACIO):
        self.state = state
        self.button_blocked = button_blocked
        self.msg_salida = msg_salida
        self.pantalla = pantalla
        self.timer = R.VALOR_INICIAL

        self.modulos = [
            Modulo('Módulo A', 17),
            Modulo('Módulo B', 18)
        ]

    def onOffButtonClic(self, event):
        if self.state == R.APAGADO and not self.buttonBlocked:
            accion = self.encender
        elif self.state == R.ENCENDIDO and not self.buttonBlocked:
            accion = self.parar
        elif self.state == R.ARRANCANDO and not self.buttonBlocked:
            accion = self.parar

        return accion()

    def encender(self):
        self.state = R.ARRANCANDO
        self.msg_salida = R.MSG_ARRANCANDO.format(self.modulos[MODULO_A], self.modulos[MODULO_B])
        self.iniciarContador()
        self.modulos[MODULO_A].on()
        return self.state

    def parar(self):
        self.state = R.PARANDO
        self.msg_salida = R.MSG_PARANDO.format(self.modulos[MODULO_B], self.modulos[MODULO_A])
        self.iniciarContador()
        self.modulos[MODULO_B].off()
        return self.state

    def iniciarContador(self, contador=R.VALOR_INICIAL):
        self.pararContador()
        segundos = '{:2d}'.format(contador)
        self.pantalla.lblMensaje['text'] = self.msg_salida + R.MSG_CONTADOR.format(segundos)
        if (contador > 0):
            self.timer = self.pantalla.lblMensaje.after(1000, self.iniciarContador, (contador - 1))
        else:
            self.procesoCompletado()

    def pararContador(self):
        if self.timer != R.VALOR_INICIAL:
            self.pantalla.lblMensaje['text'] = R.MSG_VACIO
            self.lblMensaje.after_cancel(self.timer)
            self.buttonBlocked = False

    def procesoCompletado(self):
        global state, buttonBlocked

        if state == R.ARRANCANDO and not buttonBlocked:
            buttonBlocked = True
            # MOD.moduloDosOn()
            lblMensaje['text'] = R.MSG_FIN_ARRANQUE
            lblMensaje.after(1500, pararContador)
            state = R.ENCENDIDO

        elif state == R.PARANDO and not buttonBlocked:
            buttonBlocked = True
            # MOD.moduloUnoOff()
            lblMensaje['text'] = R.MSG_FIN_PARADA
            lblMensaje.after(1500, pararContador)
            state = R.APAGADO
            lblBoton.config(image=IMG_BUTTON_ON)
