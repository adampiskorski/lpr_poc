import time
import urllib

import RPi.GPIO as GPIO

# GPIO input pin to use
LPR_PIN = 21
# URL to get image from
SOURCE = 'http://192.168.0.13:8080/photoaf.jpg'
# Path to save image locally
FILE = 'img.jpg'

# Use GPIO pin numbers
GPIO.setmode(GPIO.BCM)
# Disable "Ports already in use" warning
GPIO.setwarnings(False)
# Set the pin to be an input
GPIO.setup(LPR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Try statement to cleanup GPIO pins
try:
    # Only save the image once per gate opening
    captured = False
    # Main loop
    while True:

        # Capture the image if not captured yet and switch is closed (open gate)
        if not captured and GPIO.input(LPR_PIN):
            urllib.urlretrieve(SOURCE, FILE)
            print "Gate has been opened!"
            captured = True

        # If there was a capture and the switch is now open (closed gate) then
        # ready the loop to capture again.
        if captured and not GPIO.input(LPR_PIN):
            print "The gate has now closed!"
            captured = False

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "GPIO pins cleaned up and script killed."
