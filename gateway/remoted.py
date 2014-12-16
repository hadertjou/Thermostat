#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

tempsensor_sn = '28-000005abe684'   # Varies depending on sensor
sensor = '/sys/bus/w1/devices/' + tempsensor_sn + '/w1_slave'

# Sets pins 19(r), 21(g), and 23(b) as output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

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
    GPIO.output(19, r)
    GPIO.output(21, g)
    GPIO.output(23, b)
    
def set_color(color):
    """Receives name of color and sets the LED"""
    if color == 'red':
        set_led(0, 1, 1)
    elif color == 'green':
        set_led(1, 0, 1)
    elif color == 'blue':
        set_led(1, 1, 0)
    elif color == 'yellow':
        set_led(0, 0, 1)
    elif color == 'magenta':
        set_led(0, 1, 0)
    elif color == 'cyan':
        set_led(1, 0, 0)
    elif color == 'white':
        set_led(0, 0, 0)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

