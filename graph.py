import cv2;
import numpy as np;
from PIL import Image

#load image from file
#cv2.imwrite('imageName.png', img);

width = 600;
height = 600;


array = np.zeros([width, height, 3], dtype=np.uint8)

for x in range(0,width) :
    for y in range(0,height,10) :
        
        if y % 100 == 0:
            array[x,y] = [255,0,0];
        
        else :
            array[x,y] = [0,0,255];
            
     

for x in range(0,width) :
    for y in range(0,height,10) :
        
        if y % 100 == 0:
            array[y,x] = [255,0,0];
        
        else :
            array[y,x] = [0,0,255];
            

     
##for x in range(0,500-1) :
##    for y in range(0,500-1,10) :
##        array[x,y] = [255,255,0];
##     

    
##for x in range(0,500,10) :
##    for y in range(0,500,10) :
##        array[x,y] = [0,0,255];


cv2.imshow('image', array);
img = Image.fromarray(array)
##img.save('testrgb2.png')

while True:
    k = cv2.waitKey(5)

cv2.destroyAllWindows();


