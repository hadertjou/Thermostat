#!/usr/bin/env python2

#192.168.0.3 /16 subnet

from flask import Flask, request
import MySQLdb
import time
import RPi.GPIO as GPIO


"""
A simple script to test the registration process.
Must be run as root for now.
"""

app = Flask(__name__)


desiredtemp = 0
state = 0

nodes = {'remote1': 0, 'remote2': 0, 'remote3': 0}


GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
Cursor = Con.cursor()

# Make SQL string and execute it
sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
Cursor.execute(sql)



#Putting IP addressees to UUIDs
@app.route('/register', methods = ['POST'])
def reg_client():
    uuid = request.form['id']
    retstr = "Registered {0}".format(uuid)
    #while (iter(nodes)):
    #    ip = request.remote_addr;
    for x in range (0, len(nodes)):
        ip = request.remote_addr;
        nodes[x] = ip;
    print(retstr)
    return retstr



@app.route('/temp', methods = ['GET'])
def calculate_avg():
    temp = 0;
    for x in range (0, len(nodes)):
        r = request.get("http://" + str(nodes[x]) + "/temp");
        temp += int(r.text);

    avg = temp / len(nodes);

    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (avg,0))

    return avg;



#From Database
@app.route('/status', methods = ['GET'])
def setMode():

    Results = Cursor.fetchall();
    #(avgtemp, settemp, mode, status)
    if (int(Results[0][2]) == 0):
        set_color("red");
        return "heating"
    if (int(Results[0][2]) == 1):
        set_color("blue");
        return "cooling"
    if (int(Results[0][2]) == 2):


        if (desiredtemp > calculate_avg()):
            #turn LEDS Red
            set_color("red");
            return 0;
        if (desiredtemp < calculate_avg()):
            #turn LEDs Blue
            set_color("blue");
            return 1;

        if (desiredtemp == calculate_avg()):
            #idle/off
            set_color("white");

        return "default"
    if (int(Results[0][2]) == 3):
        set_color("white");
        return "off"

    return "error"

#From remote node
#@app.route('/settemp', methods = ['GET'])
#def get_temp():
#    return desiredtemp

#from Database
@app.route('/settemp', methods = ['POST'])
def settemp():
    r = request.form['temp']
    newtemp = int(r.text)
    Results = Cursor.fetchall()
    desiredtemp = int(Results[0][1])

    if (desiredtemp > calculate_avg()):
        #turn LEDS Red
        set_color("red");
        return 0;
    if (desiredtemp < calculate_avg()):
        #turn LEDs Blue
        set_color("blue");
        return 1;

    if (desiredtemp == calculate_avg()):
        #idle/off
        set_color("white");

    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (newtemp ,0))


def setdbtemp(newtemp):
    Results = Cursor.fetchall()
    desiredtemp = int(Results[0][1])

    if (desiredtemp > calculate_avg()):
        #turn LEDS Red
        set_color("red");
        return 0;
    if (desiredtemp < calculate_avg()):
        #turn LEDs Blue
        set_color("blue");
        return 1;

    if (desiredtemp == calculate_avg()):
        #idle/off
        set_color("white");

    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (newtemp ,0))


#from remote node
@app.route('/temp/<uuid>', methods = ['GET'])
def nodetemp(uuid):

    r = request.get("http://" + str(nodes[uuid]) + "/temp")
    temp = int(r.text)
    return temp



# Database
@app.route('/state', methods = ['POST'])
def currentStatus():
    #Always Heating, always cooling, idle
    if (settemp() == 0):
        Cursor.execute("""
        UPDATE projectDB
        SET status=%s
        WHERE db_index=%s
        """, (0 ,0))
        return "Heating"

    if (settemp() == 1):
        Cursor.execute("""
        UPDATE projectDB
        SET status=%s
        WHERE db_index=%s
        """, (1 ,0))
        return "Cooling"

    else:
        Cursor.execute("""
        UPDATE projectDB
        SET status=%s
        WHERE db_index=%s
        """, (2 ,0))
        return "Idle"


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






