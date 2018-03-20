import RPi.GPIO as GPIO
import time

def roomOccupiedLoop():
    GPIO.output(lightPin, GPIO.HIGH)
    while(GPIO.input(motionPin) == 1):
        time.sleep(300)
    GPIO.output(lightPin, GPIO.LOW)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motionPin = 26
lightPin = 10
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(lightPin, GPIO.OUT)

while True:
    if(GPIO.input(motionPin) == 1):
        roomOccupiedLoop()
        sleep(1)