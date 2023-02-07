#!/usr/bin/env python
# encoding: utf-8
# https://pythonbasics.org/flask-rest-api/

import json
from flask import Flask, request, jsonify
import os
import sqlite3

def select_all_from_table(conn,table,mat):
    """
    Query all rows in the properties table
    :param conn: the Connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table + "_table WHERE Material='" + mat + "' ")

    rows = cur.fetchall()

    for row in rows:
        print(row)

app = Flask(__name__)

#Chrome -> GET {'material':'*S355'}
@app.route('/', methods=['GET'])
def query_records():
    print('------------------------------------------------------------------------')
    material = request.args.get('material')
    #print(material)
    #open sql database (con)
    con = sqlite3.connect('2023_02_07\\data.db')
    
    #query sql
    with con:
        select_all_from_table(con,"material",material)
    
    #convert to json format <<<
    return jsonify({'material': '*S355'})

#Chrome -> PUT {"name":"Lajos","email":"lajos@gmail.com"}
"""
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
"""
app.run(debug=True)