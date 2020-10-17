#!/usr/bin/env python3

#process the text files under descriptions
#weight should be converted to an int and 'lbs' removed ('500 lbs' = 500)
#turning the data into JSON
#upload JSON data to <linux-instance-external-IP>/fruits using the 'requests' library

import os
import requests
import json
import re

files_path = ("supplier-data/descriptions/")
files = os.listdir(files_path)
images_path = ("supplier-data/images/")
images = os.listdir(images_path)
url = "http://104.154.100.255/fruits/"

for file in files:
    supplier_data = {}
    basename = (file.split('.')[0])
    filename = basename + '.txt'
    filepath = files_path + file
    imagename = basename + '.jpeg'
    with open(filepath, 'rb') as openfile:
        lines = openfile.readlines()
        supplier_data['name'] = lines[0].decode("utf-8").rstrip('\n')
        weight_text = lines[1].decode("utf-8").rstrip('\n')
        just_weight = re.search(r'^\d*', weight_text)
        weight_int = int(just_weight[0])
        supplier_data['weight'] = weight_int
        supplier_data['description'] = lines[2].decode("utf-8").rstrip('\n')
        supplier_data['image_name'] = imagename
    r = requests.post(url, json=supplier_data)
    print(r.request.url)
    print(r.status_code)
