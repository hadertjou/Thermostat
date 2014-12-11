#!/usr/bin/env python2

from flask import Flask, request
import MySQLdb
import requests

"""
A simple script to test the registration process.
Must be run as root for now.
"""

app = Flask(__name__)


desiredtemp = 0;

@app.route('/register', methods = ['POST'])
def reg_client():
    uuid = request.form['id']
    retstr = "Registered {0}".format(uuid)
    print(retstr)
    return retstr

@app.route('/temp', methods = ['GET'])
def calculate_avg():
    # temp1,temp2,temp3
    r1 = requests.get("http://remote1/temp")
    r2 = requests.get("http://remote2/temp")
    r3 = requests.get("http://remote3/temp")
    temp1 = int(r1.text)
    temp2 = int(r2.text)
    temp3 = int(r3.text)


    avg = temp1 + temp2 + temp3;
    return avg;

@app.route('/status', methods = ['GET'])
def state():
    if (heating):
        return "heating"
    if (cooling):
        return "cooling"
    return "idle"

@app.route('/settemp', method = ['GET'])
def curstate():
    return desiredtemp


@app.route('/settemp', method = ['POST'])
def settemp():
    #r = requests.
    desiredtemp = int(r.text)
    return desiredtemp


@app.route('/temp/<UUID>', method = ['GET'])
def nodetemp():
    r = requests.get("http://remote1/temp/<UUID>")
    temp = int(r.text)
    return temp


@app.route('/state', method = ['GET'])
def state():




@app.route('/state', method = ['POST'])
def setstate():
    payload = {'key1': 'heat', 'key2': 'cool', 'key3': 'off', 'key4': 'default'}
    r = requests.post("http://<gateway>/state", data=payload)
    

# Create a connection object and create a cursor
Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="dac_user", passwd="myPassword", db="tst")
Cursor = Con.cursor()

# Make SQL string and execute it
sql = "SELECT * FROM Users"
Cursor.execute(sql)

# Fetch all results from the cursor into a sequence and close the connection
Results = Cursor.fetchall()
Con.close()







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
    


