##vid to img_to json


import os
import numpy 
import cv2
import csv
import numpy as np

ORIG_PATH="/home/jf/yolov4/vids/"
SAVE_PATH="/home/jf/yolov4/vids_aux/"
DARKNET_PATH='/home/jf/yolov4/darknet/'
desc=os.listdir(ORIG_PATH)
files = [ORIG_PATH+i for i in desc]

def vid_to_json(arch,path_dest,file_desc):
    
    cam = cv2.VideoCapture(arch)
    currentframe = 0
    
    try:
        os.mkdir(SAVE_PATH+file_desc)
    except OSError:
        print (f"{file_desc} already exists failed")
    else:
        print ("Successfully created the directory")

    files_list=[]
    while(True):
        ret,frame = cam.read()
        if ret:
            name = path_dest+file_desc+'/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name,frame)
            files_list.append(name)
            currentframe += 1
            if currentframe%1000==0:
                print(f'saving frames...{currentframe}...done') 
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

    print('images done, saving paths in txt')
    ### SAVE ALL PATHS TO A CSV 
    files_list=np.reshape(files_list,(-1,1))
    np.savetxt(f"{SAVE_PATH}{file_desc}.txt", files_list, delimiter=';',fmt='%s')

    ##USE DARKNET TO PREDICT ALL IMAGES
    os.chdir(DARKNET_PATH)
    commands=["./darknet detector test data/obj.data cfg/yolov4-obj.cfg yolov4-obj_best.weights -ext_output -dont_show -out "+SAVE_PATH+file_desc+".json < "+SAVE_PATH+file_desc+".txt"]
    os.system("".join(commands))


#vid_to_json(files[0],SAVE_PATH,desc[0])
vid_to_json(files[4],SAVE_PATH,desc[4].split('.')[0])
