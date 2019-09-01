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
    return red;

def subtractGreen(cv2,img):
    #gives red only without background
    green = np.int16( np.matrix(img[:,:, rgb_green_pos])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
    green[green < 0] = 0;
    green[green > 255] = 0;
    green = np.uint8(green);
    cv2.imshow('green', green);
    return green;
    
def subtractBlue(cv2,img):
    #gives red only without background
    blue = np.int16( np.matrix(img[:,:,rgb_blue_pos ])) - np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos]));
    blue[blue < 0] = 0;
    blue[blue > 255] = 0;
    blue = np.uint8(blue);
    cv2.imshow('blue', blue);
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


def detectIntensity(red,green,blue):
    if(calculateCenterOfMass(red) == 0):
        print('');
    else:
        print('red light detected')
        
    if(calculateCenterOfMass(green) == 0):
        print('');
    else:
        print('green light detected')
           
    if(calculateCenterOfMass(blue) == 0):
       print('');
    else:
       print('blue light detected')
        

#opening camera
cap = cv2.VideoCapture(0);

while (True):
    isOpen,frame = cap.read();

    if(not isOpen):
        print('camera is busy');
        break;
    
    red_only = subtractRed(cv2,frame);
    green_only = subtractGreen(cv2,frame);
    blue_only = subtractBlue(cv2,frame);

    detectIntensity(red_only,green_only,blue_only );
    
    
    #do whatever you want
    k = cv2.waitKey(5)
    if k == 27: # wait for ESC key to exit
        break;
    
cv2.destroyAllWindows();
