#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
## use import pickle in Py3.
import pickle as pickle

################################
# module: hist_image_index.py
# YOUR NAME
# YOUR A#
################################


## indexing dictionary.
HIST_INDEX = {}
valid_types = ['.jpg', '.png']

#access the global HIST_INDEX and stores normalized pictures into it
def hist_index_img(imgp, color_space, bin_size=8):
  global HIST_INDEX

  image = cv2.imread(imgp)

  bins = [bin_size for i in range(3)]
  input_hist = 0

  if color_space == 'hsv':
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    input_hist = cv2.calcHist([image], [0,1,2], None, bins, [0, 180, 0, 256, 0, 256])
  elif color_space == 'rgb':
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    input_hist = cv2.calcHist([image], [0,1,2], None, bins, [0, 256, 0, 256, 0, 256])

  norm_hist = cv2.normalize(input_hist, input_hist).flatten()
  HIST_INDEX[imgp] = norm_hist


def hist_index_img_dir(imgdir, color_space, bin_size, pick_file):
  global HIST_INDEX

  for f in os.listdir(imgdir):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_types:
      continue
    path = imgdir + "/" + f
    print('indexing... ' + f)
    hist_index_img(path, color_space, bin_size)
    print('done indexing ', f)

  pickle_out = open(pick_file, 'wb')
  pickle.dump(HIST_INDEX, pickle_out)
  pickle_out.close()

  print('indexing finished')


## ========================= Image Indexing Tests =====================
  
## change these as you see fit.
## IMGDIR is the directory where the images to be indexed are saved.
## PICDIR is the directory where pickled dictionaries are saved.
##          /home/stan/Desktop/Spring2019/SciPy/assn/hw12
IMGDIR = '/home/stan/Desktop/Spring2019/SciPy/assn/hw12/img/all'
PICDIR = '/home/stan/Desktop/Spring2019/SciPy/assn/hw12/pickles/'

def test_01():
  HIST_INDEX = {}
  hist_index_img_dir(IMGDIR, 'rgb', 8, PICDIR + 'rgb_hist8.pck')

def test_02(): 
  HIST_INDEX = {}
  hist_index_img_dir(IMGDIR, 'rgb', 16, PICDIR + 'rgb_hist16.pck')

def test_03():
  HIST_INDEX = {}
  hist_index_img_dir(IMGDIR, 'hsv', 8, PICDIR + 'hsv_hist8.pck')

def test_04():
  HIST_INDEX = {}
  hist_index_img_dir(IMGDIR, 'hsv', 16, PICDIR + 'hsv_hist16.pck')


if __name__ == '__main__':
  test_01()
  test_02()
  test_03()
  test_04()



