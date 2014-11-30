#!/usr/bin/env python2

from flask import Flask, request

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
