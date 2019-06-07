#!/usr/bin/python

#########################################
# module: hw08_s19.py
# YOUR NAME
# YOUR A#
#########################################

### modify these as you see fit.
import math
import numpy as np
import argparse
import cv2
import sys
import os
import re

def generate_file_names(ftype, rootdir):
	'''
	recursively walk dir tree beginning from rootdir
	and generate full paths to all files that end with ftype.
	sample call: generate_file_names('.jpg', /home/pi/images/')
	'''
	for path, dirlist, filelist in os.walk(rootdir):
		for file_name in filelist:
			if not file_name.startswith('.') and \
			   file_name.endswith(ftype):
				yield os.path.join(path, file_name)
		for d in dirlist:
			generate_file_names(ftype, d)


def amplify_grayscale_blur_img_dir(ftype, in_img_dir, kz, c, amount):  
	generator = generate_file_names(ftype, in_img_dir)

	for file in generator:
		img = cv2.imread(file, 1)
		b,g,r = cv2.split(img)
		# cv2.imshow('original', img)

		if c == 'b':
			b[:, :] += amount
		elif c == 'g':
			g[:, :] += amount 
		elif c == 'r':
			r[:, :] += amount

		img_amped = cv2.merge([b,g,r])
		# cv2.imshow('amplified', img_amped)
		img_gray = cv2.cvtColor(img_amped, cv2.COLOR_BGR2GRAY)
		# cv2.imshow('grayscaled', img_gray)
		kernel = np.ones((kz, kz), np.float32) / (kz ** 2)
		blurred_img = cv2.filter2D(img_gray, -1, kernel)
		# cv2.imshow('blurred by ' + str(kz), blurred_img)
		cv2.imwrite(file[:-4] + '_blur.jpg', blurred_img)
		# cv2.waitKey()
		# cv2.destroyAllWindows()




	


 
