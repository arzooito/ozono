import R
from Modulo import Modulo

MODULO_A = 0
MODULO_B = 1


class ControladorArranque:

    def __init__(self, state=R.APAGADO, button_blocked=False, msg_salida=R.MSG_VACIO):
        self.state = state
        self.button_bloqued = button_blocked
        self.msg_salida = msg_salida

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
        self.msg_salida = R.MSG_ARRANCANDO
        self.modulos[MODULO_A].on()
        return self.state

    def parar(self, boton):
        self.state = R.PARANDO
        self.msg_salida = R.MSG_PARANDO
        self.modulos[MODULO_B].off()
        return self.state
