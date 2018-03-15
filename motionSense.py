#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.IN)
pin = 2

while(True):
    if(GPIO.input(pin) == 0):
        print("output 0")
    elif(GPIO.input(pin) == 1):
        print("output 1")