#!/usr/bin/env python
# encoding: utf-8

#https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests
#response = requests.get("http://api.open-notify.org/astros.json")
#print(response)

#response.content() # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
#response.json() # This method is convenient when the API returns JSON


query = {'material':'*S355'}
response = requests.get('http://127.0.0.1:5000', params=query)
print(response.json())

# Create a new resource
#response = requests.get('http://127.0.0.1:5000', data = {"name":"Lajos"})
#print(response.json())
# Update an existing resource
#requests.put('https://httpbin.org/put', data = {'key':'value'})