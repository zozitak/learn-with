#!/usr/bin/env python
# encoding: utf-8
# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

#Chrome -> GET {"name":"Lajos"}
@app.route('/', methods=['GET'])
def query_records():
    print('------------------------------------------------------------------------')
    name = request.args.get('name')
    print(name)
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        print(records)
        for record in records:
            print(record)
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

#Chrome -> PUT {"name":"Lajos","email":"lajos@gmail.com"}
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

#Chrome -> POST {"name":"Lajos","email":"lajos@gmail.com"}
@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

#Chrome -> DELETE {"name":"Lajos"}
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open(os.getcwd() + '\\2023_01_31\\tmp\\data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(debug=True)