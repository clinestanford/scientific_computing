#!/usr/bin/python

######################################################
# module: covar_correl_02.py
# description: modeling inverse covariance b/w
# page render time and puchase amount
# bugs to vladimir kulyukin via canvas
######################################################
import numpy as np
import matplotlib.pyplot as plt
import pylab as plb

def dev_from_mean(x):
  xmean = plb.mean(x)
  return [xi - xmean for xi in x]

def covariance(x, y):
  n = len(x)
  x_dev = dev_from_mean(x)
  y_dev = dev_from_mean(y)
  return plb.dot(x_dev, y_dev) / (n-1)
  
## modeling inverse relationship b/w page rendition time
## and purchase amount
page_render_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 10.0, 1000) / page_render_time

fig1 = plt.figure(1)
fig1.suptitle('Page Render Time vs. Purchase Amount')
plt.xlabel('Page Render Time')
plt.ylabel('Purcahse Amount')
plt.grid()
plt.scatter(page_render_time, purchase_amount)

print(covariance(page_render_time, purchase_amount))
plt.show()

