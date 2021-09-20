from PIL import ImageGrab # using pillow to grab the ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics # windows api to capture the size of windows display
import datetime


width=GetSystemMetrics(0) #width of the screen
height=GetSystemMetrics(1) #height of the screen
time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %h-%M-%S")
file_name=f"{time_stamp}.mp4"
fourcc=cv2.VideoWriter_fourcc('m','p','4','v') # video encoding type
captured=cv2.VideoWriter(file_name,fourcc,20.0,(width,height)) # here the final output of the video is described that is the putput name,encoding type,fps, the size


while True:
    img=ImageGrab.grab(bbox=(0,0,width,height)) #pre setting the border
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)# the actual image fives negitive color effect this is here to give the rgb for the recording
    cv2.imshow("Recoder window",img_final)# this gives the name to the recording window
    
    captured.write(img_final) #the captured image goes to the caputed to form a output file
    if cv2.waitKey(10)==ord("q"):# delay key here it's 10
        break
