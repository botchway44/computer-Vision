import cv2;
import numpy as np;
from PIL import Image

#load image from file
#cv2.imwrite('imageName.png', img);

array = np.zeros([500, 500, 4], dtype=np.uint8)


array[:,100] = [0,0,255,10];


cv2.imshow('image', array);


while True:
    k = cv2.waitKey(5)

cv2.destroyAllWindows();


