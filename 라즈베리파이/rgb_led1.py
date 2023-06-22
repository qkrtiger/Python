import RPi.GPIO as GPIO
import time

pins = (14, 15, 18) # R: 14, G: 15, B:18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins[0], GPIO.OUT) #Red
GPIO.setup(pins[1], GPIO.OUT) #Green
GPIO.setup(pins[2], GPIO.OUT) #Blue

for i in range(5):
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.LOW)
    time.sleep(1)
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.LOW)
    time.sleep(1)
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)
    time.sleep(1)

GPIO.cleanup(pins)