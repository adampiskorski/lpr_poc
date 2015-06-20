# License Plate Recognition Proof of Concept

## Overview
This is a proof of concept project for the Catana Security Camera project.

What this system does, is detect when a complex gate is open, retrieve a single picture, 
from an IP camera, then use License Plate Recognition software to determine the license 
plate number of the vehicle(s) that passed through the gate.

It was developed with the Raspberry pi 2 Model B (though other models should work) and
uses the [Open ALPR](https://github.com/openalpr/openalpr) library.

## Requirements: 
### Hardware:
* 1x Raspberry pi
* 2x Female pin connector wires (or 1x double female connector from an ATX power switch 
   header connector, which is what I used)
* 1x Magnetic switch (I got mine from a R55 indoor door alarm/chime). The circuit should 
   be closed when the magnet is close
* 1x Magnet. I recommend a strong magnet, such as an old hard drive magnet, which is what 
   I used.
* 1x IP camera that is left unsecured (no authentication required), for development 
   purposes. I used my Note 3 and the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en)
   app to turn my phone into an IP camera.
* Something that you camera can take a picture of that has cars with license plates. It 
   be an image of (or an actual) car with the camera's FoV set to be able to see the whole 
   front of the car including headlamps, as capturing the license plate alone wont work.

### Software:
* Any OS with a working Python interpreter on it and the RPi library. I used Raspbian


## Setup:
1. Install [Open ALPR](https://github.com/openalpr/openalpr). You will most 
   probably need to install it ['the harder way'](https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux))
   , (I.E: Compile dependencies), assuming you are using Linux.
2. Download this project. You can use `git clone https://github.com/adampiskorski/lpr_poc.git`
3. Make sure the global variables at the start of `detect.py` are configured correctly:
  1. Set `LPR_PIN` to the GPIO pin you are going to use. 
     I used [this for reference](http://www.element14.com/community/servlet/JiveServlet/previewBody/73950-102-4-309126/GPIO_Pi2.png) 
     for my pi 2 Model B.
  2. Set `SOURCE` to the web address to get a fresh still image from your IP camera
     (the default value there is for the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) app).
  3. Set `FILE` to the path in which you want to store the captured image. Note that only
     one image will ever be saved as the previous one will be overwritten.
4. Solder the end of each wire with the female pin connectors to opposite ends of the 
   magnetic switch.
5. Connect one of the female pin connectors to a GPIO (21 is the default for this project)
   and the other to a GND pin.
6. Place the magnet next to the magnetic switch, or even touching it.  
7. Place something in front of the camera for it to capture.
    
    
## Run:
1. Execute `detect.py` by executing the command: `sudo python detect.py` (note that sudo 
   is necessary in order to use the GPIO pins)
2. Move the magnet away from the magnetic switch. An image will be saved, the message 
   `Gate has been opened!` will be displayed in the console, then the license plate number(s)
   that was in view of the camera.
3. Move the magnet back to it's original position next to the magnetic switch. You should
   then observe the message: `The gate has now closed!`.
   
   
## References:
* `detect.py` was started off the very basic [Burping Jelly Baby](https://www.raspberrypi.org/learning/burping-jelly-baby/worksheet/)
  tutorial.
* `lpr.py` is based on [lukagabric's](https://github.com/lukagabric/PyALPR) script.
