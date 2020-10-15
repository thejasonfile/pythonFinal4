#!/usr/bin/env python3

import os
import requests

images_path = ("supplier-data/images/")
images = os.listdir(images_path)

url = "http://104.197.44.26/upload/"

# for image in images:
#     if image.endswith('.jpeg'):
#         with open(image, 'rb') as opened:
#             r = requests.post(url, files={'file': opened})

for image in images:
    if image.endswith('.jpeg'):
        filepath = images_path + image
        with open(filepath, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
