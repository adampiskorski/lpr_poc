import time
import urllib

import RPi.GPIO as GPIO

# GPIO input pin to use
LPR_PIN = 3

# Use GPIO pin numbers
GPIO.setmode(GPIO.BCM)
# Disable "Ports already in use" warning
GPIO.setwarnings(False)
# Set the pin to be an input
GPIO.setup(LPR_PIN, GPIO.IN)

# Main loop
while True:
    if GPIO.input(LPR_PIN) == True:
        # save the image if switch is closed
        urllib.urlretrieve('http://192.168.0.13:8080/photoaf.jpg', 'img.jpg')
        print "Gate has been opened!"
        time.sleep(10)
    time.sleep(2)
