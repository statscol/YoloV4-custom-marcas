##labels stats

import os
import numpy
import glob
import io
import collections
import shutil as sht

#DEST_PATH="D:/Jhon Lopez/Tesis Icesi/img/"
DEST_PATH="E:/test/"



files = glob.glob(os.path.join(DEST_PATH, '*.txt'))
class_aux=open("E:/Gdrive/"+"classes.txt","r")
classes=[line.strip() for line in class_aux]
class_aux.close()

marcas=[]

for file in files:
    with io.open(file, mode="r", encoding="utf-8") as f:
        try:
            for line in f:
                clase,ymin,ymax,xmin,xmax=line.split()
                marcas.append(classes[int(clase)])
        except:
            print(f"Warning: {file} does not contain any valid data")
      
##show counts                
print(len(marcas))
print(collections.Counter(marcas))



