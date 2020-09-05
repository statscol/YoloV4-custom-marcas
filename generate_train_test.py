import os
import glob
import random
import shutil as sht
import numpy as np

PATH_IMG="E:/Gdrive/img_end/"

PATH_TRAIN=PATH_IMG+"obj/"
PATH_TEST=PATH_IMG+"test/"

def create_paths(PATH_AUX):
       
    if not os.path.isdir(PATH_AUX):
        print('Dir not exists, creating new one...')
        os.mkdir(PATH_AUX)
    else:
        print('Exeption: Dir already exists')


create_paths(PATH_TRAIN)
create_paths(PATH_TEST)
files=os.listdir(PATH_IMG)
random.shuffle(files) 

countf=0
for filename in files:
    if filename.endswith(".txt"):
        countf+=1
        if (countf%10==0):
            print(f"{str(np.round(100*countf/(len(files)/2),2))}% completed")

        fout=[filename,filename.replace(".txt",".jpg")]
        if np.random.binomial(1,0.85,size=None)==1:
            [sht.copyfile(PATH_IMG+i,PATH_TRAIN+i) for i in fout]
        else:
            [sht.copyfile(PATH_IMG+i,PATH_TEST+i) for i in fout]
        
print("all train & test files copied successfully...")
        
    


      

