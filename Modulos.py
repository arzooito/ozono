import RPi.GPIO as GPIO

PIN_A = 17
PIN_B = 18

def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_A, GPIO.OUT)
    GPIO.setup(PIN_B, GPIO.OUT)
    moduloUnoOff()
    moduloDosOff()

def moduloUnoOn():
    GPIO.output(PIN_A, GPIO.LOW)

def moduloUnoOff():
    GPIO.output(PIN_A, GPIO.HIGH)

def moduloDosOn():
    GPIO.output(PIN_B, GPIO.LOW)

def moduloDosOff():
    GPIO.output(PIN_B, GPIO.HIGH)