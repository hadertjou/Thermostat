#!/usr/bin/env python2

from flask import Flask, request
import MySQLdb

"""
A simple script to test the registration process.
Must be run as root for now.
"""

app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def reg_client():
    uuid = request.form['id']
    retstr = "Registered {0}".format(uuid)
    print(retstr)
    return retstr


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
    


