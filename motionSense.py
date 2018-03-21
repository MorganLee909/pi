import RPi.GPIO as GPIO
import time

def roomOccupiedLoop():
    GPIO.output(lightPin, GPIO.LOW)
    while(GPIO.input(motionPin) == 1):
        time.sleep(300)
    GPIO.output(lightPin, GPIO.HIGH)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motionPin = 14
lightPin = 9
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(lightPin, GPIO.OUT)

while True:
    if(GPIO.input(motionPin) == 1):
        roomOccupiedLoop()
        time.sleep(1)
