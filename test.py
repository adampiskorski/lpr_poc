import time
import urllib

import RPi.GPIO as gpio

# GPIO input pin to use
LPR_PIN = 3
# URL to get image from
SOURCE = 'http://192.168.0.13:8080/photoaf.jpg'
# Path to save image locally
FILE = 'img.jpg'

# Use GPIO pin numbers
gpio.setmode(gpio.BCM)
# Disable "Ports already in use" warning
gpio.setwarnings(False)
# Set the pin to be an input
gpio.setup(LPR_PIN, gpio.IN)

# Try statement to cleanup GPIO pins
try:
    # Only save the image once per gate opening
    captured = False
    # Main loop
    while True:

        # Capture the image if not captured yet and switch is closed (open gate)
        if not captured and gpio.input(LPR_PIN) is True:
            urllib.urlretrieve(SOURCE, FILE)
            print "Gate has been opened!"
            captured = True

        # If there was a capture and the switch is now open (closed gate) then
        # ready the loop to capture again.
        if captured and gpio.input(LPR_PIN) is False:
            print "The gate has now closed!"
            captured = False

        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()