#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

#set mode to BCM (may be redundant)
GPIO.setmode(GPIO.BCM)

#set pins to output
pinList = [2, 3, 4, 17, 27, 22, 10, 9]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)

#Get the pin number passed by PHP and cast to int
#determine whether the relay is on or off and switch it
#TODO change input to 1-8 and convert to pin number
def switchOnOff(pin = None):
    #Get pin input from terminal and cast to int
    if (pin == None):
        pinRaw = sys.argv[1]
        pin = int(pinRaw)

    if(GPIO.input(pin) == 0):
        GPIO.output(pin, GPIO.HIGH)
    elif(GPIO.input(pin) == 1):
        GPIO.output(pin, GPIO.LOW)

#return the state of the particular pin to determine if it is on or off
def getState(pin):
    return GPIO.input(pin)
