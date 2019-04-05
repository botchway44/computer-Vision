import numpy as np;
import cv2;


#opening camera
cap = cv2.VideoCapture(#camera_number);

while (True):
    isOpen,frame = cap.read();

    if(!isOpen):
        break;

    #do whatever you want
