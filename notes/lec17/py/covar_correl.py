#!/usr/bin/python

######################################################
# module: covar_correl.py
# description: page render time vs. puchase amount
# bugs to vladimir kulyukin via canvas
######################################################

import numpy as np
import matplotlib.pyplot as plt
import pylab as plb

def dev_from_mean(x):
  ''' compute devians from the mean of x. '''
  xmean = plb.mean(x)
  return [xi - xmean for xi in x]

def covariance(x, y):
  ''' covar b/w x and y '''
  n = len(x)
  x_dev = dev_from_mean(x)
  y_dev = dev_from_mean(y)
  return plb.dot(x_dev, y_dev) / (n-1)

## the mean page render time is 3 seconds w/ a
## standard dev of 1.
page_render_time = np.random.normal(3.0, 1.0, 1000)
## the mean purchase amount is 50 dollars w/ a
## standard dev of 10.
purchase_amount = np.random.normal(50.0, 10.0, 1000)

def plot_prt_vs_pa(prt, pa):
  ''' plot page render time (prt) vs. purchase amount (pa) '''
  fig1 = plt.figure(1)
  fig1.suptitle('Page Render Time vs. Purchase Amount')
  plt.xlabel('Page Render Time')
  plt.ylabel('Purcahse Amount')
  plt.grid()
  plt.scatter(prt, pa)
  print('covar = %f' % covariance(prt, pa))
  plt.show()

if __name__ == '__main__':
  plot_prt_vs_pa(page_render_time, purchase_amount)
  

