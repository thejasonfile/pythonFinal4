#!/usr/bin/env python3


#use PIL library
#change resolution to 600x400
#change format from .TIFF to .JPEG
#convert RGBA to RGB using convert("RGB")
#save files to ~/supplier-data/images with JPEG extension

import PIL
import os
from PIL import Image

images_path = ("./supplier-data/images")
for image in os.listdir(images_path):
    if image.endswith(".tiff"):
        print(image)
