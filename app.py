#!/usr/bin/env python

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    statement = 'Hello World!'
    return statement


#Calls the run method, runs the app on port 5000
# Create the main driver function
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port) 
#app.run(host='0.0.0.0', port=5000) 