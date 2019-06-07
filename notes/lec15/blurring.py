#!/usr/bin/python
import cv2
import numpy as np
import sys

#######################################
# module: blurring.py
# author: vladimir kulyukin
# description: blurring images with
# mean filters
#######################################

image = cv2.imread(sys.argv[1])
cv2.imshow('Original Image', image)

kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred_3x3 = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred_3x3)

kernel_5x5 = np.ones((5, 5), np.float32) / 25
blurred_5x5 = cv2.filter2D(image, -1, kernel_5x5)
cv2.imshow('5x5 Kernel Blurring', blurred_5x5)

kernel_7x7 = np.ones((7, 7), np.float32) / 49
blurred_7x7 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred_7x7)

cv2.waitKey(0)
cv2.destroyAllWindows()
















