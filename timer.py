#!/usr/bin/python
import RPi.GPIO as GPIO
from datetime import datetime
import time

def afterWork():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0545"):
            GPIO.output(7, GPIO.HIGH)
        if (currentTime == "0630"):
            GPIO.output(8, GPIO.LOW)

    if(dayOfWeek == "Sun"):
        if(currenttime == "0500"):
            GPIO.output(7, GPIO.HIGH)

dayOfWeek = ""
currentTime = ""

while True:
    dayOfWeek = datetime.now().strftime("%a")
    currentTime = datetime.now().strftime("%H%M")
    afterWork()
    time.sleep(60)
