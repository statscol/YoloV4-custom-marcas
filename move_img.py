##move txt and jpeg files to one folder

import glob
import os
import shutil as sht
import numpy as np

PATH_IMG="E:/Gdrive/img/"
DEST_PATH="E:/Gdrive/img_end/"


if not os.path.isdir(DEST_PATH):
    print('dir not exists, creating new one...')
    os.mkdir(DEST_PATH)
else:
    print('Exeption: dir already exists')


files=glob.glob(os.path.join(PATH_IMG, '*.txt'))
#print(files[0])

def copy_img_txt(AUX_PATH):
    
    if "classes" not in AUX_PATH:
        fout=[AUX_PATH,AUX_PATH.replace(".txt",".jpg")]
        [sht.copyfile(i,DEST_PATH+i.split("\\")[1]) for i in fout]
        #print(AUX_PATH+"...Done")

################COPYING ALL IMAGES WHICH HAVE BEEN LABELED##################
i=0
for arch in files:
    copy_img_txt(arch)
    i+=1
    if (i%50==0):
        print(f"{str(np.round(100*i/len(files),2))}% completed")


