#!/usr/bin/python

#########################################
# module: hw07_s19.py
# YOUR NAME
# YOUR A#
#########################################

import math
import numpy as np
import argparse
import cv2
import sys
import os
import re

## uses these command line options if you want to run your program
## in a command window.
ap = argparse.ArgumentParser()
ap.add_argument('-id', '--imgdir', required = True, help = 'image directory')
ap.add_argument('-ft', '--ftype', required = True, help = 'file type (e.g., .png)')
args = vars(ap.parse_args())


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

def read_img_dir(ftype, imgdir):
	return_list = []

	paths = generate_file_names(ftype, imgdir)
	for path in paths:
		image = cv2.imread(path, 1)
		return_list.append((path, image))
		# cv2.imshow('key',image)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()

	return return_list

def grayscale(i, imglst):
	img = imglst[i][1]

	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	cv2.imshow(imglst[i][0], img)
	cv2.imshow('grayscale', gray_image)


	return 

def set_others_to_zero(img, index):

	if index != 0:
		img[:, :, 0] = 0 
	if index != 1:
		img[:, :, 1] = 0
	if index != 2:
		img[:, :, 2] = 0

	return img    

def split_merge(i, imglst):
	img = imglst[i][1]

	b,g,r = cv2.split(img)

	zeros = np.zeros(img.shape[:2], dtype='uint8')

	cv2.imshow(imglst[i][0], img)
	cv2.imshow("Red", cv2.merge([zeros, zeros, r]))
	cv2.imshow("Green", cv2.merge([zeros, g, zeros]))
	cv2.imshow("Blue", cv2.merge([b, zeros, zeros]))

def amplify(i, imglst, c, amount):
	img = imglst[i][1]
	b, g, r = cv2.split(img)

	zeros = np.zeros(img.shape[:2], dtype='uint8')

	if c == 'b':
		b[:, :] += amount
	elif c == 'g':
		g[:, :] += amount 
	elif c == 'r':
		r[:, :] += amount 

	cv2.imshow(imglst[i][0], img)
	cv2.imshow("Amplified", cv2.merge([b, g, r]))


def verify_img_list(imglist):
	assert imglist != None

## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
	il = read_img_dir(args['ftype'], args['imgdir'])
	verify_img_list(il)
	grayscale(0, il)
	split_merge(0, il)
	amplify(0, il, 'r', 200)
	cv2.waitKey()
	cv2.destroyAllWindows()
	pass
	


 
