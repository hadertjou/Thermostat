from flask import Flask, request
import MySQLdb
import time
from regd import *




# Create a connection object and create a cursor
# Fetch all results from the cursor into a sequence and close the connection


Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
Cursor = Con.cursor()

# Make SQL string and execute it
sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
Cursor.execute(sql)

curMode = -1
curTemp = -1


while True :  # This constructs an infinite loop
    Con = MySQLdb.Connect(host="69.65.10.232", port=3306, user="timuster_ece4564", passwd="netApps4564", db="timuster_ece4564")
    Cursor = Con.cursor()

    curTemp = int(get_avg())
    print(curTemp)
    sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB"
    Cursor.execute(sql)

    Results = Cursor.fetchall();
    if (int(Results[0][1]) != curTemp):
        setdbtemp(curTemp);

    if (int(Results[0][2]) != curMode):
        setMode();

    time.sleep(5);
    #tempResults = Results;
    #curMode = int(Results[0][1])
    #curTemp = int(Results[0][2])


Con.close()
