#!/usr/bin/python

###############################################
# module: riemann.py
# YOUR NAME
# YOUR A#
###############################################

## modify these imports as you see fit.
import numpy as np
from const import const
from antideriv import antiderivdef, antideriv
from tof import tof
import matplotlib.pyplot as plt
from maker import make_const

def riemann_approx(fexpr, a, b, n, pp=0):
  '''
  pp=0 - approximate with reimann midpoint
  pp=+1 - approximate with reimann right point
  pp=-1 - approximate with reiman left point
  '''
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)
  windows = n.get_val()
  interval = (b.get_val() - a.get_val()) / windows
  offset = 0
  if pp == -1:
    offset = 0
  elif pp == 0:
    offset = interval / 2
  elif pp == 1:
    offset = interval
  else:
    raise Exception("didnt have Riemann sum of -1, 0, or 1")

  func = tof(fexpr)
  area = 0
  for i in np.arange(a.get_val(), b.get_val(), interval):
    val = i + offset
    area += func(val) * interval

  return make_const(area)


def riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n_upper, const)

  sol = []
  for i in np.arange(1, n_upper.get_val()+1):
    sol.append((i, abs(gt.get_val() - riemann_approx(fexpr, a, b, make_const(i), pp).get_val())))

  return sol


def plot_riemann_error(fexpr, a, b, gt, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n, const)
  
  left = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=-1)
  right = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=1)
  center = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=0)

  left_val = [i[1] for i in left]
  right_val = [i[1] for i in right]
  center_val = [i[1] for i in center]

  # print(left_val[-5:])
  # print(right_val[-5:])
  # print(center_val[-5:])

  xvals = [i for i in range(1, n.get_val()+1)]

  ymax = max(left_val + right_val + center_val)

  fig1 = plt.figure(1)
  fig1.suptitle("Riemann Approximation Error")
  plt.xlabel('n')
  plt.ylabel('err')
  plt.ylim(0, ymax)
  plt.xlim(-1, n.get_val())
  plt.grid()
  plt.plot(xvals, right_val, label="right", c='b')
  plt.plot(xvals, left_val, label="left", c='g')
  plt.plot(xvals, center_val, label="center", c='r')
  plt.legend(loc='best')
  plt.show(block=True)

