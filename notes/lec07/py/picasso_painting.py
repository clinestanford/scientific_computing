#!/usr/bin/python

######################################
# module: picasso_painting.py
# graphs on slide 40 of lecture 7.
# bugs to vladimir kulyukin via canvas.
######################################

import math
import numpy as np
import matplotlib.pyplot as plt

def picasso_painting_price(t):
  return 31.87*(math.e**(0.096*t))

def picasso_painting_price_change(t):
  return 31.87*0.096*(math.e**(0.096*t))

def picasso_price_curves():
  xvals = np.linspace(0, 20, 10000)
  yvals1 = np.array([picasso_painting_price(t)
                     for t in xvals])
  yvals2 = np.array([picasso_painting_price_change(t)
                     for t in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Picasso\'s Painting\'s Price')
  plt.xlabel('t')
  plt.ylabel('price')
  plt.grid()
  plt.plot(xvals, yvals1, label='price', c='red')
  plt.plot(xvals, yvals2, label='rate', c='green')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  picasso_price_curves()
