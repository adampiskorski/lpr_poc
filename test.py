import time
import urllib

import RPi.GPIO as GPIO

# GPIO input pin to use
LPR_PIN = 3
# URL to get image from
SOURCE = 'http://192.168.0.13:8080/photoaf.jpg'
# Path to save image locally
FILE = 'img.jpg'

# Use GPIO pin numbers
GPIO.setmode(GPIO.BCM)
# Disable "Ports already in use" warning
GPIO.setwarnings(False)
# Set the pin to be an input
GPIO.setup(LPR_PIN, GPIO.IN)

# Only save the image once per gate openning
captured = False
# Main loop
while True:

    # Capture the image if not captured yet and switch is closed (open gate)
    if not captured and GPIO.input(LPR_PIN) == True:
        urllib.urlretrieve(SOURCE, FILE)
        print "Gate has been opened!"
        captured = True

    # If there was a capture and the switch is now open (closed gate) then
    # ready the loop to capture again.
    if captured and GPIO.input(LPR_PIN) == False:
        print "The gate has now closed!"
        captured = False

    time.sleep(0.1)
