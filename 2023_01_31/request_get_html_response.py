#!/usr/bin/env python
# encoding: utf-8

# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})
app.run()