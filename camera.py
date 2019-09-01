import numpy as np;
import cv2;


#opening camera
cap = cv2.VideoCapture(0);

while (True):
    isOpen,frame = cap.read();

    if(not isOpen):
        print('camera is busy');
        break;
    

    cv2.imshow('frame',frame);
    #do whatever you want
    k = cv2.waitKey(5)
    if k == 27: # wait for ESC key to exit
        break;
    
cv2.destroyAllWindows();
