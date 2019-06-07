#!/usr/bin/python

######################################
# module: defintegralapprox.py
# YOUR NAME
# YOUR A#
######################################

# modify these as you see fit.
import numpy as np
from const import const
from maker import make_plus, make_e_expr, make_prod, make_const, make_pwr, make_pwr_expr
from tof import tof
import matplotlib.pyplot as plt

 
def midpoint_rule(fexpr, a, b, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)
  
  interval = (b.get_val() - a.get_val()) / n.get_val() 
  offset = interval / 2
  area = 0
  func = fexpr

  for i in np.arange(a.get_val(), b.get_val(), interval):
    area += func(i + offset) * interval

  return make_const(area)

def trapezoidal_rule(fexpr, a, b, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)

  ### I have no idea why it isn't working
  
  window = (b.get_val() - a.get_val()) / n.get_val() 
  func = fexpr
  area = 0

  vals = [func(i) for i in np.arange(a.get_val(), b.get_val() + window, window)]

  for i in range(1, len(vals)):
    area += (vals[i-1] + vals[i]) * window * .5

  return make_const(area)



def simpson_rule(fexpr, a, b, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)
  
  interval = (b.get_val() - a.get_val()) / n.get_val()
  func = fexpr
  vals = [func(i) for i in np.arange(a.get_val(), b.get_val() + interval, interval)]

  area = vals[0] + vals[len(vals)-1]

  for i in range(1, len(vals) - 1):
    if i % 2 != 0:
      area += vals[i] * 4
    else:
      area += vals[i] * 2

  return make_const(area * interval * (1/3))

  

  


