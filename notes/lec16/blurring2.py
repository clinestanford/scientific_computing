#!/usr/bin/python

import cv2
import numpy as np
import sys

#######################################
# module: blurring2.py
# author: vladimir kulyukin
# description: blurring images
#######################################

image = cv2.imread(sys.argv[1])
cv2.imshow('Original Image', image)

blur = cv2.blur(image, (3, 3))
cv2.imshow('Mean (3x3)', blur)

gauss = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian (7x7)', gauss)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median (5x5)', median)

## this is great for keeping the edges sharp.
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral 9', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
















