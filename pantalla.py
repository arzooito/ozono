from tkinter import Tk, PhotoImage, Frame, Label
from time import strftime
#import Modulos as MOD

APAGADO = 0
ENCENDIDO = 1
ARRANCANDO = 2
PARANDO = 3

MSG_ARRANCANDO = 'Módulo A conectado, arrancando módulo B en '
MSG_PARANDO = 'Módulo B desconectado, parando módulo A en '
MSG_FIN_ARRANQUE = 'Arranque completo'
MSG_FIN_PARADA = 'Parada completa'
MSG_VACIO = ''

BG = "slate blue"

VALOR_INICIAL = 30
msg_salida = MSG_VACIO
state = APAGADO
timer = VALOR_INICIAL
buttonBlocked = False

#MOD.initGPIO()

def mostrarHora():
    clock['text'] = strftime('%H:%M:%S ')
    actualizarReloj()

def actualizarReloj():
    clock.after(1000, mostrarHora)

def abrirOpciones(event):
    print('Abriendo opciones')

def onOffButtonClic(event):
	if state == APAGADO and not buttonBlocked:
		encender()
	elif state == ENCENDIDO and not buttonBlocked:
		parar()
	elif state == ARRANCANDO and not buttonBlocked:
		parar()


def encender():
	global state, msg_salida
	
	state = ARRANCANDO
	lblBoton.config(image = IMG_BUTTON_OFF)
	msg_salida = MSG_ARRANCANDO 
	iniciarContador()
	#MOD.moduloUnoOn()


def parar():
	global state, msg_salida

	state = PARANDO
	lblBoton.config(image = IMG_BUTTON_DISABLED)
	msg_salida = MSG_PARANDO
	iniciarContador()
	#MOD.moduloDosOff()


def iniciarContador(contador = VALOR_INICIAL):
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

	if(timer != VALOR_INICIAL):
		lblMensaje['text'] = MSG_VACIO
		lblMensaje.after_cancel(timer)
		buttonBlocked = False


def procesoCompletado():
	global state, buttonBlocked

	if state == ARRANCANDO and not buttonBlocked:
		buttonBlocked = True
		#MOD.moduloDosOn()
		lblMensaje['text'] = MSG_FIN_ARRANQUE
		lblMensaje.after(1500, pararContador)
		state = ENCENDIDO

	elif state == PARANDO and not buttonBlocked:
		buttonBlocked = True
		#MOD.moduloUnoOff()
		lblMensaje['text'] = MSG_FIN_PARADA
		lblMensaje.after(1500, pararContador)
		state = APAGADO
		lblBoton.config(image = IMG_BUTTON_ON)




root = Tk()
root.config(cursor = '', bg=BG)
#Para pantalla completa
#root.attributes('-fullscreen', True)
#Para eliminar el marco de la ventana    
#root.overrideredirect(True)

IMG_BUTTON_ON = PhotoImage(file = 'images/boton_on.png')
IMG_BUTTON_OFF = PhotoImage(file = 'images/boton_off.png')
IMG_BUTTON_DISABLED = PhotoImage(file = 'images/boton_disabled.png')
IMG_OPTIONS = PhotoImage(file = 'images/ruleta32.png')

toolbar = Frame(root, pady=10, padx=10, bg= 'green')
toolbar.pack(fill= 'x')

marco = Frame(root, bg=BG, pady=50)
marco.pack(fill= 'both', expand= 1)

clock = Label(toolbar, font=("","20"), padx= 10, bg= BG, fg="white")
clock.pack(side= 'left')

lbl_options = Label(toolbar, image = IMG_OPTIONS, bg=BG)
lbl_options.bind('<Button-1>', abrirOpciones)
lbl_options.pack(side = 'right')

lblBoton = Label(marco, image = IMG_BUTTON_ON, bg=BG)
lblBoton.bind('<Button-1>', onOffButtonClic)
lblBoton.pack(anchor = 'center')

lblEspacio = Label(marco, bg=BG)
lblEspacio.pack()

lblMensaje = Label(marco, font=("","22"), bg=BG, fg="white")
lblMensaje.config(width= "50")
lblMensaje.pack(anchor = 'center')

actualizarReloj()

root.mainloop()