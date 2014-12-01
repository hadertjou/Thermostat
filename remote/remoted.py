#!/usr/bin/env python

import os
import time
from flask import Flask
app = Flask(__name__)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

tempsensor_sn = 'Enter Temperature Sensor Serial Number'

sensor = 'sys/bus/w1/devices/' + tempsensor_sn + 'w1_slave'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

