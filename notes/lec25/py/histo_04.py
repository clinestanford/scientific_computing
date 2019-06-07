#!/usr/bin/python

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

##############################################################
# module: histo_04.py
# author: vladimir kulyukin
# description: matching histograms with four different
# metrics. Two input images are taken, their normalized
# flattened histrograms are computed and matched.
#
# to run:
# python histo_04.py -i1 <path_to_image1> -i2 <path_to_image2>
#
# bugs to vladimir kulyukin via canvas.
###############################################################

ap = argparse.ArgumentParser()
ap.add_argument('-i1', '--img1', required=True, help='path to image 1')
ap.add_argument('-i2', '--img2', required=True, help='path to image 2')
args = vars(ap.parse_args())

image1 = cv2.imread(args['img1'])
image2 = cv2.imread(args['img2'])

# show image 1
rgb1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
fig1 = plt.figure(1)
fig1.suptitle('Image 1')
plt.imshow(rgb1)

# show image 2
rgb2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
fig2 = plt.figure(2)
fig2.suptitle('Image 2')
plt.imshow(rgb2)

# compute histogram feature vectors
hist1 = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist2 = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
# normalize and flatten feature vectors
norm_hist1 = cv2.normalize(hist1, hist1).flatten()
norm_hist2 = cv2.normalize(hist2, hist2).flatten()

fig3 = plt.figure(3)
fig3.suptitle('Normalized Histogram 1')
plt.xlim([0, 1])
plt.xlim([0, 513])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.plot(norm_hist1)

fig4 = plt.figure(4)
fig4.suptitle('Normalized Histogram 2')
plt.xlim([0, 1])
plt.xlim([0, 513])
plt.xlabel('Bins')
plt.ylabel('Pixel Counts in Bins')
plt.plot(norm_hist2)

##################### Histogram Matching ##################

'''
OpenCV has a built in method to facilitate an easy comparison of histograms:
cv2.compareHist(). Here is the signature.

cv2.compareHist(H1, H2, method)

The cv2.compareHist() function takes three arguments: H1, which is the first histogram
to be compared, H2, the second histogram to be compared, and method, which is a
flag indicating which comparison method should be performed.

The method flag can be any of the following:

cv2.HISTCMP_CORREL: Computes the correlation H1 and H2.
cv2.HISTCMP_CHISQR:  Computes the Chi-Squared distance b/w H1 and H2.
cv2.HISTCMP_INTERSECT Calculates the intersection between b/w H1 and H2.
cv2.HISTCMP_BHATTACHARYYA: Bhattacharyya distance measures the “overlap” b/w H1 and H2.

Note that for cv2.HISTCMP_CORREL and cv2.HISTCMP_INTERSECT the large the matching
score, the higher the similarity; for cv2.HISTCMP_CHISQR and cv2.HISTCMP_BHATTACHARYYA,
the smaller the matching score, the higher the similarity
'''

# let's create a dictionary mapping metrics to matching scores
dist_table = {}
dist_table['cv2.HISTCMP_CORREL'] = cv2.compareHist(norm_hist1, norm_hist2,
                                               cv2.HISTCMP_CORREL)
dist_table['cv2.HISTCMP_CHISQR'] = cv2.compareHist(norm_hist1, norm_hist2,
                                               cv2.HISTCMP_CHISQR)
dist_table['cv2.HISTCMP_INTERSECT'] = cv2.compareHist(norm_hist1, norm_hist2,
                                               cv2.HISTCMP_INTERSECT)
dist_table['cv2.HISTCMP_BHATTA'] = cv2.compareHist(norm_hist1, norm_hist2,
                                               cv2.HISTCMP_BHATTACHARYYA)

# let's display the metrics and the scores
for metric, score in dist_table.items():
    print(metric + ' = ' + str(score))

# show figs and plots
plt.show()















