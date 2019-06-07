#!/usr/bin/python

#########################################
# module: lec_07_01.py
# description: graphs for slide 12 of
# lecture 7.
# bugs to vladimir kulyukin via canvas.
#########################################
import math
import numpy as np
import matplotlib.pyplot as plt

def exponential_decay():
  f1 = lambda x: 0.9**x
  f2 = lambda x: 0.7**x
  f3 = lambda x: 0.5**x
  f4 = lambda x: 0.3**x
  f5 = lambda x: 0.1**x
  xvals = np.linspace(-3, 3, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  yvals2 = np.array([f2(x) for x in xvals])
  yvals3 = np.array([f3(x) for x in xvals])
  yvals4 = np.array([f4(x) for x in xvals])
  yvals5 = np.array([f5(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Exponential Decay')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.ylim([0, 10])
  plt.xlim([-3, 3])
  plt.grid()
  plt.plot(xvals, yvals1, label='0.9^x', c='red')
  plt.plot(xvals, yvals2, label='0.7^x', c='green')
  plt.plot(xvals, yvals3, label='0.5^x', c='blue')
  plt.plot(xvals, yvals4, label='0.3^x', c='brown')
  plt.plot(xvals, yvals5, label='0.1^x', c='magenta')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  exponential_decay()

