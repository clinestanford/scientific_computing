#!/usr/bin/python

######################################################
# module: covar_correl_03.py
# description: modeling covariance b/w
# page render time and puchase amount w/ numpy
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

def correlation(x, y):
  stdx = x.std()
  stdy = y.std()
  return covariance(x, y) / stdx / stdy

## implementing negative covariance and correlation
## with numpy  
pageRenderTime = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageRenderTime

fig1 = plt.figure(1)
fig1.suptitle('Page Render Time vs. Purchase Amount')
plt.xlabel('Page Render Time')
plt.ylabel('Purcahse Amount')
plt.grid()
plt.scatter(pageRenderTime, purchaseAmount)

print('covar=%f' % covariance(pageRenderTime, purchaseAmount))
print('correl=%f' % correlation(pageRenderTime, purchaseAmount))

## here is how you can compute correlation and covariance w/ numpy.
print('Numpy Correlation')
print(np.corrcoef(pageRenderTime, purchaseAmount))
print('Numpy Covariance')
print(np.cov(pageRenderTime, purchaseAmount))

plt.show()

