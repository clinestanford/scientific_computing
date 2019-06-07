#!/usr/bin/python

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

#################################################
# module: histo_01.py
# author: vladimir kulyukin
# description: plotting three separate color
# histograms for an image.
#
# to run:
# python histo_01.py -i <path_to_image>
#
# bugs to vladimir kulyukin via canvas
##################################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--img', required=True, help='path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['img'])

'''
OpenCV has the function cv2.calcHist() to calculate histograms
of images. Below is an excerpt from OpenCV documentation
with a couple of my notes.

cv2.calcHist(images, channels, mask, histSize, ranges)
    images: a list of images to compute histograms for.
    
    channels: a list of indexes specifying channels; to compute a histogram
    of a grayscale image, the list is [0]; to compute a histogram for all
    three blue, green, and red channels, the channels list is [0, 1, 2].
    
    mask: a mask is a uint8  image of the same shape as the original image,
    where pixels with a value of zero are ignored and pixels with a value
    greater than zero are included in the histogram computation. Using masks
    allows you to compute a histogram for a particular region of an image;
    if mast is None,  the histogram of the entire image is computed.
    
    histSize: This is the number of bins to use when computing a histogram; it
    is a list, one for each channel we are computing a histogram for. The bin
    sizes do not all have to be the same; if you want to use 8 bins for each
    channel, the list is [8, 8, 8].
    
    ranges: the range of possible pixel values; normally, this is [0, 256] for
    each channel, but if you are using a color space other than RGB (such as HSV),
    the ranges may be different.
'''

# I want to make a few comments on an OpenCV gotcha here. The RGB color space is
# [0, 255]. However, the specified range is [0, 256]. What gives? calcHist() uses numpy's
# histogram method that turns [0, 256] into [0, 256) which, in turn, becomes [0, 255].
# In most cases, there is no difference - you are just one color value short. However, this is
# definitely a gotcha. So, we are computing three 256-bin histograms: one for each
# color.
blu_histo_256 = cv2.calcHist([image], [0], None, [256], [0, 256])
grn_histo_256 = cv2.calcHist([image], [1], None, [256], [0, 256])
red_histo_256 = cv2.calcHist([image], [2], None, [256], [0, 256])

# This is another gotcha but this one is in matplotlib. Whenever, I display
# the image in matplotlib w/o converting it into the standard RGB format,
# the displayed image is grayish. Hence, explicit conversion from BGR to
# RGB to avoid the problem.
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig1 = plt.figure(1)
fig1.suptitle('Image')
plt.imshow(rgb)

## plot each 256-bin histogram in a separate plot
fig2 = plt.figure(2)
fig2.suptitle('256-Bin Histograms')
plt.xlim([0, 256])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.subplot(311)
plt.plot(blu_histo_256, color='b')
plt.subplot(312)
plt.plot(grn_histo_256, color='g')
plt.subplot(313)
plt.plot(red_histo_256, color='r')

# Let's compute 32-bin histograms for each color.
blu_histo_32 = cv2.calcHist([image], [0], None, [32], [0, 256])
grn_histo_32 = cv2.calcHist([image], [1], None, [32], [0, 256])
red_histo_32 = cv2.calcHist([image], [2], None, [32], [0, 256])

## plot each 32-bin histogram in a separate plot
fig3 = plt.figure(3)
fig3.suptitle('32-Bin Histograms')
plt.xlim([0, 33])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.subplot(311)
plt.plot(blu_histo_32, color='b')
plt.subplot(312)
plt.plot(grn_histo_32, color='g')
plt.subplot(313)
plt.plot(red_histo_32, color='r')

## Finally, here is an example of how to plot a 32-bin histogram
## of a grayscale image. Since grayscale images are one-channel,
## the channel list is [0].
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_histo_32 = cv2.calcHist([gray_image], [0], None, [32], [0, 256])
fig4 = plt.figure(4)
fig4.suptitle('32-Bin Grayscale Histogram')
plt.xlim([0, 33])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.subplot(111)
plt.plot(gray_histo_32)

# show the figures and plots
plt.show()













