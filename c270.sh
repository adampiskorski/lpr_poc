#!/bin/bash
# set below your Raspberry PI IP address
myip="192.168.0.10"
port="5000"

gst-launch
-v v4l2src !
"image/jpeg,width=1280,height=720,framerate=30/1" !
multipartmux !
tcpserversink host=$myip port=$port sync=false