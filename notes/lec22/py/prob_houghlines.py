#!/usr/bin/python

import cv2
import numpy as np
import argparse

#########################################
# module: prob_houghlines.py
# description: apply standard HT to
# user-specified image at user-specified support level
# to run:
# python prob_houghlines.py -i <path_to_image> -spl <support_level>
# e.g. python prob_houghlines.py -i 01.jpg -spl 100
# bugs to vladimir kulyukin at usu dot edu
#########################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--img', required=True, help='path to image')
ap.add_argument('-spl', '--spl', required=True, help='support level', type=int)
args = vars(ap.parse_args())

# Let's load the image
image = cv2.imread(args['img'])
# Grayscale and Canny Edges extracted
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Run HoughLines using a rho accuracy of 1 pixel
# theta accuracy of np.pi / 180 which is 1 degree at
# the user specified support level
lines = cv2.HoughLinesP(edges, 1, np.pi/180, args['spl'], 10, 15)
# print lines.shape

# iterate through each line and convert it to the format
# required by cv.lines (i.e. requiring end points)
if lines is not None:
    for ln in lines:
        x1, y1, x2, y2 = ln[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
else:
    print 'No lines detected'

cv2.imshow('Probabilistic Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



















