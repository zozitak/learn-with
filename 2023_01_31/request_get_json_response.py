#!/usr/bin/env python
# encoding: utf-8

# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    print("hello world")
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()