#!/usr/bin/env python3
import time
import os
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

import smbus2
import bme280

def do_nothing(obj):
    pass


# define our i2c LED location
serial = i2c(port=1, address=0x3C)
# We have an ssd1306 device so we initialize it at the
# serial address we created.
device = ssd1306(serial)
# This line keeps the display from immediately turning off once the
# script is complete.
device.cleanup = do_nothing

# Setup our Temperature sensor (bme280)
port = 4
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
def main():
    data = bme280.sample(bus, address, calibration_params)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((5,10), "Temp:%3.2f \u00b0F"%(data.temperature*(9/5)+32), fill="white")
        draw.text((5,20), "Humidity:%3.2f "%(data.humidity), fill="white")
        draw.text((5,30), "pressure:%3.2f"%(data.pressure), fill="white")
        draw.text((5,40), "time stamp:"+str(data.timeStamp), fill="white")

while True:
    main()
    time.sleep (5)

import requests

# use a global variable for your URL so you can change it ne place and it affects the entire script
API_URL = 'http://grisham.shelms.io/api/'
r = requests.post(API_URL, data.temperature)
print(r.text)
