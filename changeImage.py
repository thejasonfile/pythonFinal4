#!/usr/bin/env python3


#use PIL library
#change resolution to 600x400
#change format from .TIFF to .JPEG
#convert RGBA to RGB using convert("RGB")
#save files to ~/supplier-data/images with JPEG extension

import PIL
import os
from PIL import Image

images_path = ("supplier-data/images/")
images = os.listdir(images_path)

for image in images:
    if image.endswith('tiff'):
        filename = image.split('.')[0]
        filepath = images_path + image
        im = Image.open(filepath).convert("RGB").resize((600,400)).save(images_path+filename+'.jpeg', format="jpeg")
