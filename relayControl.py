#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

#set mode to BCM (may be redundant)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#set pins to output
pinList = [2, 3, 4, 17, 27, 22, 10, 9]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)


def recieveInput(pin = None):
    #If called from website will run this to get the argument from shell
    if (pin == None):
        pinRaw = sys.argv[1]
        pin = int(pinRaw)
    
    #Change input number to corresponding pin on the pi
    if(pin == 1):
        pin = 2
    elif(pin == 2):
        pin = 3
    elif(pin == 3):
        pin = 4
    elif(pin == 4):
        pin = 17
    elif(pin == 5):
        pin = 27
    elif(pin == 6):
        pin = 22
    elif(pin == 7):
        pin = 10
    elif(pin == 8):
        pin = 9
    
    switchOnOff(pin)

#Flip the switch on corresponding pin
def switchOnOff(pin):
    if(GPIO.input(pin) == 0):
        GPIO.output(pin, GPIO.HIGH)
    elif(GPIO.input(pin) == 1):
        GPIO.output(pin, GPIO.LOW)