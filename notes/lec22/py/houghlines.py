#!/usr/bin/python

import cv2
import numpy as np
import argparse

#########################################
# module: houghlines.py
# description: apply standard HT to
# user-specified image at user-specified support level
# to run:
# python houghlines.py -i <path_to_image> -spl <support_level>
# e.g. python houghlines.py -i 01.jpg -spl 100
# bugs to vladimir kulyukin at usu dot edu
#########################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--img', required=True, help='path to image')
ap.add_argument('-spl', '--spl', required=True, help='support level', type=int)
args = vars(ap.parse_args())

# Let's load a simple image with 3 black squares
image = cv2.imread(args['img'])
# Grayscale and Canny Edges extracted
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Run HoughLines using a rho accuracy of 1 pixel
# theta accuracy of np.pi / 180 which is 1 degree
# Set the line threshold (support level) is set to the value
# of the command line argument given by the user.
# Generally, the lower the support level, the more lines are detected. 
lines = cv2.HoughLines(edges, 1, np.pi/180, args['spl'])

# Iterate through each line and convert it to the format
# required by cv.lines (i.e. requiring end points)
if not lines is None:
    for ln in lines:
        rho, theta = ln[0]
        # this is some trigonometry to conver rho and theta
        # to two points on the rho-theta line: (x1, y1) and (x2, y2).
        # once we have them, we can use cv2.line procedure
        # to draw the line in the image.
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

cv2.imshow('Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



















