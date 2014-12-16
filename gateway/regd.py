#!/usr/bin/env python2

#192.168.0.3 /16 subnet

from flask import Flask, request
import MySQLdb
import time
import RPi.GPIO as GPIO
import requests

"""
A simple script to test the registration process.
Must be run as root for now.
"""

app = Flask(__name__)


desiredtemp = 0
state = 0

#nodes = {'remote1': 0, 'remote2': 0, 'remote3': 0}
nodes = {}


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
    ip = request.remote_addr;
    if uuid not in nodes.keys():
        nodes[uuid] = ip;
    print(retstr)
    return retstr



@app.route('/temp', methods = ['GET'])
def get_avg():
    return str(calculate_avg())

def calculate_avg():
    temp = 0;

    if len(nodes) == 0:
        mynodes = {'B827EB5D4F2C':'192.168.0.4', 'B827EB82DA58': '192.168.0.3', 'B827EB9D0DB3':'192.168.0.1'}
    else:
        mynodes = nodes
	
    successes = 0
    for x in mynodes:
        try:
	    r = requests.get("http://" + str(mynodes[x]) + "/temp");
	    temp += int(float(r.text));
            successes += 1
        except:
            pass


    if successes != 0:
        avg = temp / successes;
    else:
        avg = 0;

    try:

        Cursor.execute("""
	UPDATE projectDB
	SET avg_temp=%s
	WHERE db_index=%s
	""", (avg,0))
    except:
        pass

    return avg;



#From Database
@app.route('/status', methods = ['GET'])
def setMode():
    Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
    Cursor = Con.cursor()
    sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
    Cursor.execute(sql)
    
    Results = Cursor.fetchall();
    desiredtemp = int(Results[0][1])
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
            return str(0);
        if (desiredtemp < calculate_avg()):
            #turn LEDs Blue
            set_color("blue");
            return str(1);

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
    Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
    Cursor = Con.cursor()
    sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
    Cursor.execute(sql)
    Results = Cursor.fetchall()
    desiredtemp = int(Results[0][1])
    
    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (newtemp ,0))

    if (desiredtemp > calculate_avg()):
        #turn LEDS Red
        set_color("red");
        return str(0);
    if (desiredtemp < calculate_avg()):
        #turn LEDs Blue
        set_color("blue");
        return str(1);

    if (desiredtemp == calculate_avg()):
        #idle/off
        set_color("white");


def setdbtemp(newtemp):
    Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
    Cursor = Con.cursor()
    sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
    Cursor.execute(sql)
    Results = Cursor.fetchall()
    desiredtemp = int(Results[0][1])
    
    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (newtemp ,0))

    if (desiredtemp > calculate_avg()):
        #turn LEDS Red
        set_color("red");
        return str(0);
    if (desiredtemp < calculate_avg()):
        #turn LEDs Blue
        set_color("blue");
        return str(1);

    if (desiredtemp == calculate_avg()):
        #idle/off
        set_color("white");
        return str(2)



#from remote node
@app.route('/temp/<uuid>', methods = ['GET'])
def nodetemp(uuid):

    r = requests.get("http://" + str(nodes[uuid]) + "/temp")
    temp = r.text
    return temp



# Database
@app.route('/state', methods = ['POST'])
def currentStatus():
    #Always Heating, always cooling, idle
    if (setdbtemp() == "0"):
        Cursor.execute("""
        UPDATE projectDB
        SET status=%s
        WHERE db_index=%s
        """, (0 ,0))
        return "Heating"

    elif (setdbtemp() == "1"):
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
    app.run(host='0.0.0.0', port=80, debug=True)






