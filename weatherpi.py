#!/usr/bin/env python3

import requests

# use a global variable for your URL so you can change it ne place and it affects the entire script
API_URL = 'http://grisham.shelms.io/api/'
#data = {'celesius':32.1}
r = requests.post(API_URL, data.temperature)
print(r.text)

