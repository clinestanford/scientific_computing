#!/usr/bin/python

####################################################
# module: info_diffusion.py
# description: information diffusion model
# bugs to vladimir kulyukin via canvas.
#####################################################

import math
import numpy as np
import matplotlib.pyplot as plt

def information_diffusion(P, k):
  f1 = lambda t: P*(1.0 - (math.e**(-k*t)))
  xvals = np.linspace(0, 200, 10000)
  yvals1 = np.array([f1(x) for x in xvals])
  fig1 = plt.figure(1)
  fig1.suptitle('Diffusion of Information by Mass Media')
  plt.xlabel('t (time)')
  plt.ylabel('Numfer of \'Informed\' People')
  #plt.ylim([0, 10])
  plt.xlim([0, 25])
  plt.grid()
  plt.plot(xvals, yvals1, label='v(t) = ' + str(P) + '(1 - e^{-' + str(k) + 't})', c='g')
  plt.legend(loc='best')
  plt.show()

if __name__ == '__main__':
  information_diffusion(50, 0.15)
