import numpy as np;
import cv2;


rgb_red_pos = 2;
rgb_blue_pos = 0;
rgb_green_pos = 1;

def subtractRed(cv2,img):
    #gives red only without background
    red = np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
    red[red < 0] = 0;
    red[red > 255] = 0;
    red = np.uint8(red);
    cv2.imshow('red', red);

def subtractGreen(cv2,img):
    #gives red only without background
    green = np.int16( np.matrix(img[:,:, rgb_green_pos])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
    green[green < 0] = 0;
    green[green > 255] = 0;
    green = np.uint8(green);
    cv2.imshow('green', green);
    
def subtractBlue(cv2,img):
    #gives red only without background
    blue = np.int16( np.matrix(img[:,:,rgb_blue_pos ])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos]));
    blue[blue < 0] = 0;
    blue[blue > 255] = 0;
    blue = np.uint8(blue);
    cv2.imshow('blue', blue);

    
#opening camera
cap = cv2.VideoCapture(0);

while (True):
    isOpen,frame = cap.read();

    if(not isOpen):
        print('camera is busy');
        break;
    
    subtractRed(cv2,frame);
    subtractGreen(cv2,frame);
    subtractBlue(cv2,frame);
    
    #do whatever you want
    k = cv2.waitKey(5)
    if k == 27: # wait for ESC key to exit
        break;
    
cv2.destroyAllWindows();
