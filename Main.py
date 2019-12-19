from tkinter import Tk, PhotoImage, Frame, Label
from ClockToolbar import ClockToolbar as Toolbar
import R #Constantes
#import Modulos as MOD

msg_salida = R.MSG_VACIO
state = R.APAGADO
timer = R.VALOR_INICIAL
buttonBlocked = False

#MOD.initGPIO()

def onOffButtonClic(event):
    if state == R.APAGADO and not buttonBlocked:
        encender()
    elif state == R.ENCENDIDO and not buttonBlocked:
        parar()
    elif state == R.ARRANCANDO and not buttonBlocked:
        parar()


def encender():
    global state, msg_salida

    state = R.ARRANCANDO
    lblBoton.config(image=IMG_BUTTON_OFF)
    msg_salida = R.MSG_ARRANCANDO
    iniciarContador()
#MOD.moduloUnoOn()


def parar():
    global state, msg_salida

    state = R.PARANDO
    lblBoton.config(image=IMG_BUTTON_DISABLED)
    msg_salida = R.MSG_PARANDO
    iniciarContador()
#MOD.moduloDosOff()


def iniciarContador(contador = R.VALOR_INICIAL):
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



root = Tk()
root.config(cursor='', bg=R.BG)
#Para pantalla completa
#root.attributes('-fullscreen', True)
#Para eliminar el marco de la ventana    
#root.overrideredirect(True)

IMG_BUTTON_ON = PhotoImage(file='images/boton_on.png')
IMG_BUTTON_OFF = PhotoImage(file='images/boton_off.png')
IMG_BUTTON_DISABLED = PhotoImage(file='images/boton_disabled.png')

toolbar = Toolbar(root, R.BG)

marco = Frame(root, bg=R.BG, pady=50)
marco.pack(fill='both', expand=1)

lblBoton = Label(marco, image=IMG_BUTTON_ON, bg=R.BG)
lblBoton.bind('<Button-1>', onOffButtonClic)
lblBoton.pack(anchor='center')

lblEspacio = Label(marco, bg=R.BG)
lblEspacio.pack()

lblMensaje = Label(marco, font=("", "22"), bg=R.BG, fg="white")
lblMensaje.config(width="50")
lblMensaje.pack(anchor='center')

root.mainloop()
