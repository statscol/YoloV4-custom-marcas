import pandas as pd
import pytube as pyt
import os
import cv2
import shutil as sht


###PUT YOUR PATH HERE
SAVE_PATH="E:/videos/"


data=pd.DataFrame({'desc':['Ame-Nac','Mill-Cal','Once-Med','Tol-Env','SFE-Tol','Cuc-Hui','Jun-Equi','Umag-Jag','Pas-Buc','Per-Chi','Cal-Per','Ame-Med','Nac-Per','Cuc-Jun','SFE-Mill','Umag-Pas'],'link':['https://www.youtube.com/watch?v=KXJvGQo2dvU','https://www.youtube.com/watch?v=KVlE0QRfPUg','https://www.youtube.com/watch?v=6a3pC37L0Iw','https://www.youtube.com/watch?v=4_OyO8k8eiU','https://www.youtube.com/watch?v=15OIMePro3E','https://www.youtube.com/watch?v=IRRVQLWQo7s','https://www.youtube.com/watch?v=3lU7UkI8Qps','https://www.youtube.com/watch?v=ZNVkpLUvb40','https://www.youtube.com/watch?v=jI6L4vtOyqc','https://www.youtube.com/watch?v=8kDoRwURAXM','https://www.youtube.com/watch?v=Ury4lSJHmPU','https://www.youtube.com/watch?v=8WGs2s7xxMc','https://www.youtube.com/watch?v=PfoUiPOjgnc','https://www.youtube.com/watch?v=4H1LwFcWLqM','https://www.youtube.com/watch?v=sXOWWzSMeso','https://www.youtube.com/watch?v=V20OTe5u4BI']})



def yout_to_img(link_vid,path_dest,file_desc):
    yt = pyt.YouTube(link_vid)
    ##DOWNLOAD VIDEO AT 720p Res
    yt.streams.filter(res="720p").first().download(path_dest+file_desc+"/")
    cam = cv2.VideoCapture(path_dest+file_desc+'/YouTube.mp4')
    currentframe = 0
    
    while(True):
        ret,frame = cam.read()
        if ret:
            name = path_dest+file_desc+'/frame' + str(currentframe) + '.jpg'
            
            if currentframe%5==0:
                cv2.imwrite(name,frame)
                
           
            if currentframe%1000==0:
            	print("Creating..."+name)

            
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()
    os.remove(path_dest+file_desc+'/YouTube.mp4')


##DOWNLOAD ALL VIDEOS AND CONVERTING TO IMAGES

data.apply(lambda x: yout_to_img(x[1],SAVE_PATH,x[0]),axis=1)


DEST_PATH="E:/Gdrive/"
newpath = f'{DEST_PATH}img' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

    
for i in os.listdir(SAVE_PATH):
    subf=os.listdir(SAVE_PATH+i)
    [sht.copyfile(SAVE_PATH+i+"/"+file,DEST_PATH+"img/"+i+"_"+file)  for file in subf]
    print(i+"..done")
        
sht.copyfile("E:/videos/Ame-Nac/frame0.jpg","E:/Gdrive/img/Ame-Nacframe0.jpg")