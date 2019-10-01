import cv2;
import numpy as np;
from PIL import Image

#load image from file
#cv2.imwrite('imageName.png', img);

array = np.zeros([500, 500, 3], dtype=np.uint8)

for x in range(0,500,2) :
        array[x,x] = [0,0,255];
        array[(500-1) - x,x] = [0,0,255];


for x in range(0,500,2) :
    for y in range(0,500,2) :
        array[x,y] = [0,0,255];

for x in range(0,500,4) :
    for y in range(0,500,4) :
        array[x,y] = [70,180,0];
        array[(500-1) - x,x] = [0,200,255];

cv2.imshow('image', array);


while True:
    k = cv2.waitKey(5)

cv2.destroyAllWindows();


