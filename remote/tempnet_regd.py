#!/usr/bin/env python2

"""
A simple utility to discover tempnet gateways and register itself with them.
Currently requires tempnet be identified by _tempnet._tcp.local on port 80.

This should be run on boot with an init script.
"""

__author__ = "Matt Hazinski"

from zeroconf import raw_input, ServiceBrowser, Zeroconf
import socket
import time
import urllib
import urllib2
from uuid import getnode
import RPi.GPIO as GPIO

# Registers by POSTing to the gateway with id=mac_addr
def register(addr, uuid):
    response = ""

    print("Registering with %s as uuid %s" % (addr, uuid))
    expected_response = "Registered {0}".format(uuid)

    # Hacky stuff for LED
    # Sets pins 19(r), 21(g), and 23(b) as output pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)


    while response != expected_response:
        set_color('white')
        try:
            url = 'http://{0}/register'.format(addr)
            params = urllib.urlencode({
              'id': uuid
            })
            response = urllib2.urlopen(url, params).read()
            print("Registration response: \"{0}\"".format(response))
        except:
            print("Could not connect to gateway. Trying again in 3 seconds.")
        time.sleep(3)

    set_color('yellow')

    # TODO try again if response is not 200

# Gets a UUID of the raspberry pi. 
# This isn't robust if there are multiple interfaces.
def getUuid():
    hexmac = hex(getnode()).strip('0x').strip('L').upper()
    return hexmac

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




# Parts of this are taken from https://pypi.python.org/pypi/zeroconf

gw_list = []        # List of gateways we registered with. Possibly useful in the future.

class MyListener(object):

    def removeService(self, zeroconf, type, name):
        print("Service %s removed" % (name))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        addr = socket.inet_ntoa(info.address)
        server = info.server
        print("Service %s added, service info: %s" % (name, info))

        gw_list.append(addr) 

        uuid = getUuid()
        register(addr, uuid)


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_tempnet._tcp.local.", listener)

while True:
    time.sleep(3)

print("Finished service discovery.")
print(gw_list)
