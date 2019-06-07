#!/usr/bin/python

#################################
# module: car_deaths_plot.py
# description: car-accident-related deaths
# bugs to vladimir kulyukin via canvas.
#################################

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 10, 15, 17, 18, 19])
y = np.array([46.8, 43.4, 45.3, 43.9, 39.7, 35.9])

def fit_regression_line(x, y):
  N = len(x)
  assert len(y) == N
  sum_xy = sum(xy[0] * xy[1] for xy in zip(x, y))
  sum_x = sum(xi for xi in x)
  sum_y = sum(yi for yi in y)
  sum_x_sqr = sum(xi**2 for xi in x)
  A = (1.0*(N*sum_xy - sum_x*sum_y))/(N*sum_x_sqr - sum_x**2)
  B = (sum_y - A*sum_x)/(1.0*N)
  rlf = lambda x: A*x + B
  return A, B, rlf

def plot_data_points(x, y):
  plt.title('Car-Accident-Related Deaths in U.S.')
  plt.xlabel('x (years since 1990)')
  plt.ylabel('y (deaths (in thousands)')
  plt.autoscale(tight=True)
  plt.xlim([0, 30])
  plt.ylim([0, 50])
  plt.scatter(x, y)
  plt.grid()
  plt.show()
  
def plot_regression_line(x, y):
  plt.title('Car-Accident-Related Deaths in U.S.')
  plt.xlabel('x (years since 1990)')
  plt.ylabel('y (deaths (in thousands)')
  plt.autoscale(tight=True)
  plt.xlim([0, 30])
  plt.ylim([0, 50])
  A, B, rlf = fit_regression_line(x, y)
  xvals = np.linspace(x[0], 30)
  yvals = np.array([rlf(xv) for xv in xvals])
  plt.plot(xvals, yvals, label='regression line', c='r')
  assert len(x) == len(y)
  plt.scatter(x, y)
  plt.legend(loc='best')
  plt.grid()
  plt.show()

if __name__ == '__main__':
  plot_data_points(x, y)
  plot_regression_line(x, y)
