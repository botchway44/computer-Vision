import numpy as np;
import cv2;

#load image from file
#cv2.imwrite('imageName.png', img);
rgb_red_pos = 2;
rgb_blue_pos = 0;
rgb_green_pos = 1;

img_1 = cv2.imread('red1.png',1);
##img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

##extract the red component image 1
red_only1 = np.int16( np.matrix(img_1[:,:,rgb_red_pos])) - np.int16( np.matrix(img_1[:,:,rgb_blue_pos])) - np.int16( np.matrix(img_1[:,:,rgb_green_pos]));
red_only1 = np.uint8(red_only1);
red_only1[red_only1 < 0] = 0;
red_only1[red_only1 > 255] = 0;
cv2.imshow('Image 1',red_only1);



img_2 = cv2.imread('red1.png',1);
##img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

##extract the red component of image 2
red_only2 =  np.int16( np.matrix(img_2[:,:,rgb_red_pos])) - np.int16( np.matrix(img_2[:,:,rgb_blue_pos])) - np.int16( np.matrix(img_2[:,:,rgb_green_pos]))
red_only2 = np.uint8(red_only2);
red_only2[red_only2 < 0] = 0;
red_only2[red_only2 > 255] = 0;
cv2.imshow('Image 2',red_only2);


##differences between two frames
subtracted = np.int16(red_only1) - np.int16(red_only2);
subtracted =  np.uint8(subtracted);
subtracted[subtracted < 0] = 0;
subtracted[subtracted > 255] = 0;
cv2.imshow('subtracted',subtracted);


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
    print('the column total is'+str(total));
    print('the column all total is'+str(all_total));
    
    #column location
    #col_location = total / all_total;
    
    return 0 if all_total == 0 else total / all_total;

cofm = calculateCenterOfMass(subtracted);
if(cofm == 0):
    print('no object detected ');
else:
    print(' object detected ');


if cv2.waitKey(1) & 0xFF == ord('q'): break
# When everything done, release the capture cap.release() cv2.destroyAllWindows()


