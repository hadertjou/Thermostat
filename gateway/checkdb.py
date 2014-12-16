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

curMode = 0
curTemp = 0

var = 1
while var == 1 :  # This constructs an infinite loop

    Results = Cursor.fetchall();
    if (int(Results(1)[:-1]) != curTemp):
        settemp();

    if (int(Results(2)[:-1]) != curMode):
        setMode();

    time.sleep(5);
    #tempResults = Results;
    curMode = int(Results(1))
    curTemp = int(Results(2))


Con.close()
