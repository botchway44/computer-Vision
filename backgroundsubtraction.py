import numpy as np;
import cv2;

#load image from file
#cv2.imwrite('imageName.png', img);
rgb_red_pos = 2;
rgb_blue_pos = 0;
rgb_green_pos = 1;

img = cv2.imread('all.png',1);
##img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

#gives red only without background
red = np.int16( np.matrix(img[:,:, rgb_red_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos]));
red[red < 0] = 0;
red[red > 255] = 0;
red = np.uint8(red);
cv2.imshow('red', red);

#gives green only without background
green = np.int16( np.matrix(img[:,:, rgb_green_pos])) - np.int16( np.matrix(img[:,:,rgb_blue_pos])) - np.int16( np.matrix(img[:,:,rgb_red_pos]));
green[green < 0] = 0;
green[green > 255] = 0;
green = np.uint8(green);
cv2.imshow('green', green);

#gives blue only without background
blue = np.int16( np.matrix(img[:,:, rgb_blue_pos])) - np.int16( np.matrix(img[:,:,rgb_green_pos])) - np.int16( np.matrix(img[:,:,rgb_red_pos]));
blue[blue < 0] = 0;
blue[blue > 255] = 0;
blue = np.uint8(blue);
cv2.imshow('blue', blue);

cv2.imshow('img', img);


