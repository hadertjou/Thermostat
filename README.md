tempnet
=======

ECE 4564 final project: a distributed thermostat network 

Installation
============
- Git clone this into /srv
- Install screen, python-pip

For remotes:
- Install dependencies listed in remote/requirements.txt with pip
- chmod +x tempnet-remote and copy it to /etc/init.d/
- run "update-rc.d tempnet-remote defaults" to enable the script at boot
- Edit remote/regd.py to change the serial number of the temperature sensor
- Use the example /etc/networking/interfaces provided, or setup your own network

For gateway:
- Install dependencies listed in gateway/requirements.txt with pip
