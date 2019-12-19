from tkinter import Tk, PhotoImage, Frame, Label

TIMER_INICIAL = 30

class Crono(Label):

    def __init__(self):
        super().__init__()




    def iniciarContador(contador = TIMER_INICIAL):
        global timer

        pararContador()
        segundos = '{:2d}'.format(contador)
        lblMensaje['text'] = msg_salida + segundos + ' s'
        if(contador > 0):
            timer = lblMensaje.after(1000, iniciarContador, (contador-1))
        else:
            procesoCompletado()


    def pararContador():
        global timer, buttonBlocked

        if(timer != R.VALOR_INICIAL):
            lblMensaje['text'] = R.MSG_VACIO
            lblMensaje.after_cancel(timer)
            buttonBlocked = False


    def procesoCompletado():
        global state, buttonBlocked

        if state == R.ARRANCANDO and not buttonBlocked:
            buttonBlocked = True
            #MOD.moduloDosOn()
            lblMensaje['text'] = R.MSG_FIN_ARRANQUE
            lblMensaje.after(1500, pararContador)
            state = R.ENCENDIDO

        elif state == R.PARANDO and not buttonBlocked:
            buttonBlocked = True
             #MOD.moduloUnoOff()
            lblMensaje['text'] = R.MSG_FIN_PARADA
            lblMensaje.after(1500, pararContador)
            state = R.APAGADO
            lblBoton.config(image=IMG_BUTTON_ON)