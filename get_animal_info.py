import numpy as np
from psycopg2.extensions import adapt, register_adapter, AsIs
import rootpath
import sys
from sqlalchemy import Sequence, select
import cv2
import base64
import os
import io
from PIL import Image
from array import array
path = rootpath.detect()
sys.path.append(path)
from entry_table import EntryCameraTable
class AnimalInfo():
    def __init__(self):
        pass
    def get_info(self, session):
        result = session.query(EntryCameraTable).all()
        count = 0
        for row in result:
            img = row.animal_image
            animal_name = row.animal_name
            if img is not None:
                imgdata = base64.b64decode(img)
                image = Image.frombytes("RGB", (480, 360), imgdata)
                print("Image state: ", type(image))
                image = np.array(image)
                print(image)
                cv2.imwrite(animal_name+str(count)+".png", image) 
                count += 1
        return result
