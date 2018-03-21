#!/usr/bin/python
import RPi.GPIO as GPIO
from datetime import datetime
import time

#Set up the GPIO and the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

light = 9
GPIO.setup(light, GPIO.OUT)


dayOfWeek = ""
currentTime = ""

def checkDateTime():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        print("day correct")
        if (currentTime == "0545"):
            print("time correct")
            GPIO.output(light, GPIO.LOW)
        if (currentTime == "0630"):
            GPIO.output(light, GPIO.HIGH)

    if(dayOfWeek == "Sun"):
        if(currentTime == "0500"):
            GPIO.output(light, GPIO.LOW)

while True:
    dayOfWeek = datetime.now().strftime("%a")
    currentTime = datetime.now().strftime("%H%M")
    checkDateTime()
    time.sleep(60)
