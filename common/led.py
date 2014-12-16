#!/usr/bin/env python2

""" 
A library for interfacing with our status LEDs
"""

import RPi.GPIO as GPIO

def setup_led():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)


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
 
