#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

tempsensor_sn = '28-000005abe684'   # Varies depending on sensor
sensor = 'sys/bus/w1/devices/' + tempsensor_sn + '/w1_slave'

# GPIO pin output is 3.3V
GPIO.setmode(GPIO.BOARD)
chan_list = [19, 21, 23]
GPIO.setup(chan_list, GPIO.OUT) # Sets pins 19(r), 21(g), and 23(b) as output pins

def raw_data():
    """Retrieves the raw data from the temperature sensor on the Raspberry Pi"""

    x = open(sensor, 'r')
    data = x.readlines()
    x.close()
    return data

@app.route('/temp')
def get_temp():
    """Retrieves current fahrenheit temperature value"""

    data = raw_data()
    while data[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        data = raw_data()

    temp_val = data[1].find('t=')
    if temp_val != -1:
        temp_string = data[1].strip()[temp_val + 2:]
        temp_fahrenheit = 32.0 + ((float(temp_string) / 1000.0) * 1.8)
        return temp_fahrenheit

def set_led(r, g, b):
    """Set the color of the LED"""
    GPIO.output(chan_list, (r, g, b))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

