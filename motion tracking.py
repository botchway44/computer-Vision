import numpy as np;
import cv2;
import time;

rgb_red_pos = 2;
rgb_blue_pos = 0;
rgb_green_pos = 1;

def subtractRed(img):
    #gives red only without background
    red = np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
    red[red < 0] = 0;
    red[red > 255] = 255;
    red = np.uint8(red);
    ##cv2.imshow('red', red);
    return red;

def subtractGreen(img):
    #gives red only without background
    green = np.int16( np.matrix(img[:,:, rgb_green_pos])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
    green[green < 0] = 0;
    green[green > 255] = 255;
    green = np.uint8(green);
    ##cv2.imshow('green', green);
    return green;
    
def subtractBlue(img):
    #gives red only without background
    blue = np.int16( np.matrix(img[:,:,rgb_blue_pos ])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos]));
    blue[blue < 0] = 0;
    blue[blue > 255] = 255;
    blue = np.uint8(blue);
    ##cv2.imshow('blue', blue);
    return blue;


def calculateCenterOfMass(subtracted) :
    rows = np.shape(np.matrix(subtracted))[0];
    cols = np.shape(np.matrix(subtracted))[1];
    ##calculate the center of mass
    #np.sum() #0 for columns 1 for rows
    column_sums = np.matrix(np.sum(subtracted,0));
    column_numbers = np.matrix(np.arange(cols));
    column_mult = np.multiply(column_sums, column_numbers);
    total = np.sum(column_mult);
     
    #sum the total of the image matrix
    all_total = np.sum(np.sum(subtracted));
    ##print('the column total is'+str(total));
    ##print('the column all total is'+str(all_total));
    
    #column location
    #col_location = total / all_total;
    
    return 0 if all_total == 0 else total / all_total;

def calculateCenterOfMassRow(subtracted) :
    rows = np.shape(np.matrix(subtracted))[0];
    cols = np.shape(np.matrix(subtracted))[1];
    
    ##calculate the center of mass
    #np.sum() #0 for columns 1 for rows
    row_sums = np.matrix(np.sum(subtracted,1));
    row_sums = row_sums.transpose();
    row_numbers = np.matrix(np.arange(rows));
    row_mult = np.multiply(row_sums, row_numbers);
    total = np.sum(row_mult);
     
    #sum the total of the image matrix
    all_total = np.sum(np.sum(subtracted));
    ##print('the row total is'+str(total));
    ##print('the row all total is'+str(all_total));
    
    #column location
    #col_location = total / all_total;
    
    return 0 if all_total == 0 else total / all_total;

def differenceImages(img1, img2):
    subtracted = np.int16(img1) - np.int16(img2);
    subtracted =  np.uint8(subtracted);
    subtracted[subtracted < 0] = 0;
    subtracted[subtracted > 0] = 255;
    #cv2.imshow('subtracted',subtracted);
    return subtracted;

def construction(red, green, blue):
    constructed = np.int16(red) + np.int16(green) + np.int16(blue);
    constructed =  np.uint8(constructed);
    #constructed[constructed < 0] = 0;
    #constructed[constructed > 255] = 0;
    cv2.imshow('constructed',constructed);
    return constructed;

    
def detectIntensity(red,green,blue):
    if(calculateCenterOfMass(red) == 0):
        print('');
    else:
        print('red motion light detected')
        
    if(calculateCenterOfMass(green) == 0):
        print('');
    else:
        print('green motion  detected')
           
    if(calculateCenterOfMass(blue) == 0):
       print('');
    else:
       print('blue motion detected')
        

#opening camera
cap = cv2.VideoCapture(0);

while (True):
    isOpen,frame1 = cap.read();

    if(not isOpen):
        print('camera is busy');
        break;
    
    cv2.imshow('frame1', frame1);

    #pause for sometime
    time.sleep(0.1);

    _,frame2 = cap.read();
    cv2.imshow('frame2', frame2);


    ##rgb only
    red1 = subtractRed(frame1);
    red2 = subtractRed(frame2);

    green1 = subtractGreen(frame1);
    green2 = subtractGreen(frame2);

    blue1 = subtractBlue(frame1);
    blue2 = subtractBlue(frame2);
    
    ##differences
    red_only = differenceImages(red1, red2);
    blue_only = differenceImages(green1, green2);
    green_only = differenceImages(blue1, blue2);

    ##construct image
    detectIntensity(red_only, blue_only, green_only);
    
    cv2.imshow('red 1',red1);
    cv2.imshow('red 2 ',red2);
    print(red_only);
    cv2.imshow('red only',red_only);
    cv2.imshow('blue_only',blue_only);
    cv2.imshow('green_only',green_only);

    
    #do whatever you want
    k = cv2.waitKey(5)
    if k == 27: # wait for ESC key to exit
        break;
    
cv2.destroyAllWindows();
