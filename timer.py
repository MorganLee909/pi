#!/usr/bin/python
from datetime import datetime
import time
import relayControl

def afterWork():
    if (dayOfWeek == "Tue" or "Wed" or "Thu" or "Fri" or "Sat"):
        if (currentTime == "0116"):
            relayControl.recieveInput(8)

dayOfWeek = ""
currentTime = ""

while True:
    dayOfWeek = datetime.now().strftime("%a")
    currentTime = datetime.now().strftime("%H%M")
    afterWork()
    time.sleep(60)
