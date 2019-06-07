#!/usr/bin/python

import argparse
import cv2
import sys
import os
## use import pickle in Py3
import pickle as pickle
from matplotlib import pyplot as plt
from os.path import basename
from hist_image_index import hist_index_img

################################
# module: hist_image_index.py
# YOUR NAME
# YOUR A#
################################

def calc_diff(flat1, flat2, hist_sim):
  if hist_sim == 'correl':
    return cv2.compareHist(flat1, flat2, cv2.HISTCMP_CORREL)
  elif hist_sim == 'chisqr':
    return cv2.compareHist(flat1, flat2, cv2.HISTCMP_CHISQR)
  elif hist_sim == 'inter':
    return cv2.compareHist(flat1, flat2, cv2.HISTCMP_INTERSECT)
  elif hist_sim == 'bhatta':
    return cv2.compareHist(flat1, flat2, cv2.HISTCMP_BHATTACHARYYA)
  else: 
    print('no similarity matrix input')
    return None


def compute_hist_sim(inhist_vec, hist_index, hist_sim, topn=3):
  similarities = []

  for k, v in hist_index.items():
    similarities.append((k, calc_diff(inhist_vec, v, hist_sim)))

  return sorted(similarities, key=lambda x: x[1], reverse=True)[:topn]
 

def show_images(input_image, match_list):
  input_image = cv2.resize(input_image, (0,0), None, .2, .2)
  cv2.imshow('test_image', input_image)
  i=1
  for imgp in match_list:
    img = cv2.imread(imgp[0])
    img = cv2.resize(img, (0,0), None, .2, .2)
    cv2.imshow('matched: ' + imgp[0], img)
    i+=1

  cv2.waitKey(0)
  cv2.destroyAllWindows()

def find_sim_rgb_images(imgpath, bin_size, hist_index, hist_sim):
  bins = [bin_size for i in range(3)]
  img = cv2.imread(imgpath)
  hist = cv2.calcHist([img], [0,1,2], None, bins, [0, 256, 0, 256, 0, 256])
  flattened = cv2.normalize(hist, hist).flatten()

  return compute_hist_sim(flattened, hist_index, hist_sim)


def find_sim_hsv_images(imgpath, bin_size, hist_index, hist_sim):
  bins = [bin_size for i in range(3)]
  img = cv2.imread(imgpath)
  hist = cv2.calcHist([img], [0,1,2], None, bins, [0, 180, 0, 256, 0, 256])
  flattened = cv2.normalize(hist, hist).flatten()

  return compute_hist_sim(flattened, hist_index, hist_sim)

def load_hist_index(pick_path):
  with open(pick_path, 'rb') as histfile:
    return pickle.load(histfile)

## change the paths as you see fit and add calls to show_images()
## after you implement it.


## ============= Image Retrieval Tests ===========================

## change these as you see fit.
## IMGDIR is the directory for test images
## PICDIR is the directory where the pickle files are stored.
IMGDIR = '/home/stan/Desktop/Spring2019/SciPy/assn/hw12/img/hist_test/'
PICDIR = '/home/stan/Desktop/Spring2019/SciPy/assn/hw12/pickles/'

'''
My Py shell output:
images/123461762.JPG --> 2.69072864504
images/123465049.JPG --> 2.63319342056
images/123472255.JPG --> 2.43531483644
'''
def test_01():
  hist_index = load_hist_index(PICDIR + 'rgb_hist8.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'food_test/img01.JPG'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_rgb_images(imgpath,
		                    8, hist_index, 'inter')
  for imagepath, sim in top_matches[:3]:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index

'''
My Py shell output:
>>> test_02()
images/123472992.JPG --> 1.04123155377
images/123465793.JPG --> 0.778828541127
images/123465726.JPG --> 0.775194820913
'''
def test_02():
  hist_index = load_hist_index(PICDIR + 'hsv_hist8.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'food_test/img03.JPG'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_hsv_images(imgpath,
		                    8, hist_index, 'inter')
  for imagepath, sim in top_matches:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index

'''
My Py shell output:
images/123465245.JPG --> 15.8357133494
images/17_02_21_22_17_56_orig.png --> 21.0158345761
images/17_02_21_22_17_55_orig.png --> 21.401725557
'''
def test_03():
  hist_index = load_hist_index(PICDIR + 'rgb_hist8.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'food_test/img04.JPG'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_rgb_images(imgpath,
		                    8, hist_index, 'chisqr')
  for imagepath, sim in top_matches:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index

'''
My Py shell output:
images/17_02_21_22_14_24_orig.png --> 0.0952925097908
images/17_02_21_22_14_14_orig.png --> 0.190314746298
images/17_02_21_22_20_56_orig.png --> 0.282203709903
'''
def test_04():
  hist_index = load_hist_index(PICDIR + 'rgb_hist16.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'car_test/img22.png'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_rgb_images(imgpath,
		                    16, hist_index, 'bhatta')
  for imagepath, sim in top_matches:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index

'''
My Py shell output:
images/123472992.JPG --> 0.948968044156
images/123459060.JPG --> 0.957500781094
images/123465726.JPG --> 0.957573532491

Matching car_test/img023.png in HSV space on bhatta doesn't produce
good results.
''' 
def test_05():
  hist_index = load_hist_index(PICDIR + 'hsv_hist16.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'car_test/img02.png'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_hsv_images(imgpath,
		                    16, hist_index, 'bhatta')
  for imagepath, sim in top_matches:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index

'''
My Py shell output:
images/16_07_02_14_21_01_orig.png --> 0.0601641627891
images/16_07_02_14_21_06_orig.png --> 0.0626254148808
images/16_07_02_14_21_02_orig.png --> 0.0641319684534

Matching car_test/img023.png in RGB space on bhatta produces
excellent matches.
'''
def test_06():
  hist_index = load_hist_index(PICDIR + 'rgb_hist16.pck')
  assert len(hist_index) == 318
  imgpath = IMGDIR + 'car_test/img02.png'
  inimg = cv2.imread(imgpath)
  top_matches = find_sim_rgb_images(imgpath,
		                    16, hist_index, 'bhatta')
  for imagepath, sim in top_matches:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, top_matches)
  del hist_index


  
 
if __name__ == '__main__':
  test_01()

