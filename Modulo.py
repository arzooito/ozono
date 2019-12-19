import RPi.GPIO as GPIO


class Modulo:
    ACTIVADO = GPIO.LOW
    DESACTIVADO = GPIO.HIGH
    ENTRADA = GPIO.IN
    SALIDA = GPIO.OUT

    def __init__(self, nombre, pin, estado=DESACTIVADO, modo=SALIDA):
        self.nombre = nombre
        self.pin = pin
        self.estado = estado
        self.modo = modo

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, self.modo)
        GPIO.output(self.pin, self.estado)

    def on(self):
        self.estado = Modulo.ACTIVADO
        GPIO.output(self.pin, self.estado)

    def off(self):
        self.estado = Modulo.DESACTIVADO
        GPIO.output(self.pin, self.estado)

    def __str__(self):
        return self.nombre
