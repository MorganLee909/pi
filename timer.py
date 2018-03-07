#!/usr/bin/python
from datetime import datetime
import time
import relayControl
import RPi.GPIO as GPIO

#Set up the GPIO and the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)
GPIO.setup(5, GPIO.IN)
inSensor = GPIO.input(11)
outSensor = GPIO.input(5)

occupancy = 0
dayOfWeek = ""
currentTime = ""

def afterWork():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0450"):
            relayControl.recieveInput(8)

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
    motionCheck()
    time.sleep(0.1)
