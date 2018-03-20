#!/usr/bin/python
import RPi.GPIO as GPIO
from datetime import datetime
import time

#Set up the GPIO and the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

dayOfWeek = ""
currentTime = ""

def checkDateTime():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0545"):
            GPIO.output(7, GPIO.HIGH)
        if (currentTime == "0630"):
            GPIO.output(7, GPIO.LOW)

    if(dayOfWeek == "Sun"):
        if(currentTime == "0500"):
            GPIO.output(7, GPIO.HIGH)

while True:
    dayOfWeek = datetime.now().strftime("%a")
    currentTime = datetime.now().strftime("%H%M")
    checkDateTime()
    time.sleep(60)
