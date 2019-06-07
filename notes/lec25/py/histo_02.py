#!/usr/bin/python

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

#######################################################
# module: histo_02.py
# author: vladimir kulyukin
# description: plotting color histormas for an image
# in loops.
#
# to run:
# python histo_02.py -i <path_to_image>
#
# bugs to vladimir kulyukin via canvas
########################################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--img', required=True, help='path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['img'])

# show the image
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig1 = plt.figure(1)
fig1.suptitle('Image')
plt.imshow(rgb)

# split the image into channels, initialize the 3-tuple of colors
# for plotting in a for-loop below.
chans = cv2.split(image)
colors = ('b', 'g', 'r')
fig2 = plt.figure(2)
fig2.suptitle('256-Bin Color Histograms')
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')

# list of histograms to flatten after the loop
histo_list_256 = [] 
# loop over channels and colors and plot 256-bin
# histograms in figure 2.
for (chn, clr) in zip(chans, colors):
    # compute 
    hist = cv2.calcHist([chn], [0], None, [256], [0, 256])
    histo_list_256.extend(hist)
    # plot the histogram
    plt.plot(hist, color = clr)
    plt.xlim([0, 256])

# note let's plot 32-bin color histograms
# in figure 3.
fig3 = plt.figure(3)
fig3.suptitle('32-Bin Color Histograms')
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')

# list of histograms to flatten after the loop
histo_list_32 = [] 
# loop over channels and colors and plot
# in figure 3.
for (chn, clr) in zip(chans, colors):
    # compute 
    hist = cv2.calcHist([chn], [0], None, [32], [0, 256])
    histo_list_32.extend(hist)
    # plot the histogram
    plt.plot(hist, color = clr)
    plt.xlim([0, 33])

# note let's plot 16-bin color histograms
# in figure 3.
fig4 = plt.figure(4)
fig4.suptitle('16-Bin Color Histograms')
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')

# list of histograms to flatten after the loop
histo_list_16 = [] 
# loop over channels and colors and plot
# in figure 4.
for (chn, clr) in zip(chans, colors):
    # compute 
    hist = cv2.calcHist([chn], [0], None, [16], [0, 256])
    histo_list_16.extend(hist)
    # plot the histogram
    plt.plot(hist, color = clr)
    plt.xlim([0, 17])
 
# show the dimensionality of the flattened color histograms.
# hist_list_256, when flattened, has 256 bins for each channel x 3 channels = 768 values.
# histo_list_32, when flattened, has 32 bins for each channel x 3 channels =
# 96 values.
# hist_list_16, when flattened, hast 16 bins for each channel x 3 channels = 48 values.
print 'flattened histo_list_256 size: %d' % (np.array(histo_list_256).flatten().shape)
print 'flattened histo_list_32 size: %d' % (np.array(histo_list_32).flatten().shape)
print 'flattened histo_list_16 size: %d' % (np.array(histo_list_16).flatten().shape)

# show the figures and plots
plt.show()










