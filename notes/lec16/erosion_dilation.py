#!/usr/bin/python

########################################################
# module: erosion_dilation.py
# description: examples of eroding and dilating images
# bugs to vladimir kulyukin via canvas
########################################################

import cv2
import sys

## read an image from the path specified on
## the command line
img = cv2.imread(sys.argv[1])
cv2.imshow('Original', img)

## erode it with a 5x5 kernel and display
er_img = cv2.erode(img, (20, 20))
cv2.imshow('Eroded', er_img)

## dilate it with a 5x5 kernel and display
dl_img = cv2.dilate(img, (20, 20))
cv2.imshow('Dilated', dl_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
