#!/usr/bin/python
import RPi.GPIO as GPIO
from datetime import datetime
import time
<<<<<<< HEAD
<<<<<<< HEAD
import relayControl
import RPi.GPIO as GPIO

#Set up the GPIO and the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)
GPIO.setup(5, GPIO.IN)
inSensor = GPIO.input(11)
outSensor = GPIO.input(5)
=======

def afterWork():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0545"):
            GPIO.output(7, GPIO.HIGH)
        if (currentTime == "0630"):
            GPIO.output(8, GPIO.LOW)

    if(dayOfWeek == "Sun"):
        if(currentTime == "0500"):
            GPIO.output(7, GPIO.HIGH)
>>>>>>> master

occupancy = 0
dayOfWeek = ""
currentTime = ""
=======
>>>>>>> master

def afterWork():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0545"):
            GPIO.output(7, GPIO.HIGH)
        if (currentTime == "0630"):
            GPIO.output(8, GPIO.LOW)

    if(dayOfWeek == "Sun"):
        if(currentTime == "0500"):
            GPIO.output(7, GPIO.HIGH)

def motionCheck():
    if(inSensor == 1):
        time.sleep(0.1)
        if(outSensor ==1):
            occupancy -= 1
            if(occupancy == 0):
                relayControl.recieveInput(8)
    if(outSensor == 1):
        time.sleep(0.1)
        if(inSensor == 1):
            if(occupancy == 0)
                relayControl.recieveInput(8)
            occupancy += 1

while True:
    dayOfWeek = datetime.now().strftime("%a")
    currentTime = datetime.now().strftime("%H%M")
    afterWork()
<<<<<<< HEAD
<<<<<<< HEAD
    motionCheck()
    time.sleep(0.1)
=======
    time.sleep(60)
>>>>>>> master
=======
    time.sleep(60)
>>>>>>> master
