#!/usr/bin/python

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

###########################################################
# module: histo_03.py
# author: vladimir kulyukin
# description: plotting normalized, flattened histograms
#
# to run:
# python histo_03.py -i <path_to_image>
#
# bugs to vladimir kulyukin via canvas
############################################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--img', required=True, help='path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['img'])

# show the image
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig1 = plt.figure(1)
fig1.suptitle('Image')
plt.imshow(rgb)

# Calculate a histogram of three colors with 8 bins per color.
# Since we have three colors with 8 bins per color, there will
# be 8^3 = 512 values in input_hist. The array [0, 256, 0, 256, 0, 256]
# specifies the ranges for each color. The first two numbers 0, 256
# specify the range for blue; the second two numbers 0, 256 specify the
# range for green; the third two numbers specify the range for red.

input_hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
# Below we plot a normalized histogram. What is
# a normalized histogram? It is a histogram where
# each pixel count is in [0, 1].
# cv2.normalize() ensures that the pixel counts are in [0, 1].
# flatten then flattens the array so that we can plot it.
# the second argument to normalize is the destination matrix where
# the normalized histogram is saved.
# Since the destination matrix is the same as the input matrix,
# the normalization is done in place. Normalized and flattened
# matrices are used as image feature vectors to find similar
# images. If you want to preserve the original matrix,
# you need to make a copy of the matrix and use that
# copy as your destination. For example,
# hist_copy = np.copy(input_hist)
norm_hist = cv2.normalize(input_hist, input_hist).flatten()
print(norm_hist.shape)

## Plot the normalized flattened histogram.
## Such histograms can be used as feature vectors.
fig2 = plt.figure(2)
fig2.suptitle('Normalized Histogram')
plt.xlim([0, 1])
plt.xlim([0, 513])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.plot(norm_hist)

# show the figures and plots
plt.show()










