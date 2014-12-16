#!/usr/bin/env python2

from flask import Flask, request
import MySQLdb
import time

"""
A simple script to test the registration process.
Must be run as root for now.
"""

app = Flask(__name__)


desiredtemp = 0;
state = 0;
remote1 = 0;
remote2 = 0;
remote3 = 0;
nodes = {'remote1': 0, 'remote2': 0, 'remote3': 0}


# Create a connection object and create a cursor
Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="dac_user", passwd="myPassword", db="tst")
Cursor = Con.cursor()

# Make SQL string and execute it
sql = "SELECT * FROM Users"
Cursor.execute(sql)

# Fetch all results from the cursor into a sequence and close the connection




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
    # temp1,temp2,temp3
    r1 = request.get("http://" + str(nodes[0]) + "/temp")
    r2 = request.get("http://" + str(nodes[1]) + "/temp")
    r3 = request.get("http://" + str(nodes[2]) + "/temp")
    temp1 = int(r1.text)
    temp2 = int(r2.text)
    temp3 = int(r3.text)


    avg = temp1 + temp2 + temp3;

    Cursor.execute("""
    UPDATE projectDB
    SET avg_temp=%s
    WHERE db_index=%s
    """, (avg,0))

    return avg;



#From Database
@app.route('/status', methods = ['GET'])
def state():

    Results = Cursor.fetchall();
    #(avgtemp, settemp, mode, status)
    if (Results(2) == 0):
        return "heating"
    if (Results(2) == 1):
        return "cooling"
    if (Results(2) == 2):
        return "idle"

    return "error"

#From remote node
@app.route('/settemp', method = ['GET'])
def get_temp():
    return desiredtemp

#from Database
@app.route('/settemp', method = ['POST'])
def settemp():
    #r = requests.
    Results = Cursor.fetchall()
    desiredtemp = Results(1);
    return desiredtemp

#from remote node
@app.route('/temp/<UUID>', method = ['GET'])
def nodetemp(uuid):

    r = request.get("http://" + str(nodes[uuid]) + "/temp")
    temp = int(r.text)
    return temp

#To Database
@app.route('/state', method = ['GET'])
def state():

    return state;



#From Database
@app.route('/state', method = ['POST'])
def setstate():
    #r = request.post("http://<gateway>/state", data=payload)



def updateDB():
    print("updated")



var = 1
while var == 1 :  # This constructs an infinite loop
    Results = Cursor.fetchall();
    time.sleep(5);

print "Good bye!"






Con.close()





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)






