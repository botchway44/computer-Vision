import numpy as np;
import cv2;

#load image from file
#cv2.imwrite('imageName.png', img);

img = cv2.imread('stanford.png',1);

red = np.matrix(img[:,:,2]);
green = np.matrix(img[:,:,1]);
blue = np.matrix(img[:,:,0]);

#red only
red_only = np.int16(red) - np.int16(green) - np.int16(blue);
red_only[red_only < 0] = 0;
red_only[red_only>255] = 255;
red_only = np.uint8(red_only);

cv2.imshow('image', img);
cv2.imshow('image-red', red);
cv2.imshow('image-green', green);
cv2.imshow('image-blue', blue);
cv2.imshow('red_only', red_only);

