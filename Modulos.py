import RPi.GPIO as GPIO


def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    moduloUnoOff()
    moduloDosOff()

def moduloUnoOn():
    GPIO.output(17, GPIO.LOW)

def moduloUnoOff():
    GPIO.output(17, GPIO.HIGH)

def moduloDosOn():
    GPIO.output(18, GPIO.LOW)

def moduloDosOff():
    GPIO.output(18, GPIO.HIGH)