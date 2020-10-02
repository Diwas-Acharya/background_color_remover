
import numpy as np 
import cv2 
import imutils
  
img = cv2.imread('mini.jpg')

img = imutils.resize(img , width = 480)
img_array = np.array(img)
shape = img_array.shape

# This program removes Green color in the background

u_green = np.array([40, 150, 10])
l_green = np.array([21,255,15])

# Specify a rgb color code for your color

#looping throung all the pixels of the image if pixels is green in color then replace with black color
for x in range(shape[0]):
	for y in range(shape[1]):
		if list(img[x][y]) < list(u_green) or list(img[x][y]) == list(l_green):
			img[x][y] = 0

cv2.imshow('image', img) 
k = cv2.waitKey(0) & 0xFF  
