#!/usr/bin/python

#################################################
# module: approx_slopes.py
# description: approximating slopes of
# various exponential functions on slides 15-17, 20.
# bugs to vladimir kulyukin via canvas.
#################################################

import math

def slope_of_b_to_x(b):
  for d in range(1, 11):
    h = 1.0/(10.0**d)
    print((b**h-1.0)/h)

def slope_of_2_to_x():
  print('\nApproximating f\'(x) = 2^x, at (0, 1):')
  slope_of_b_to_x(2.0)
  print('********')

def slope_of_3_to_x():
  print('\nApproximating f\'(x) = 3^x, at (0, 1):')
  slope_of_b_to_x(3.0)
  print('********')

def slope_of_4_to_x():
  print('\nApproximating f\'(x) = 4^x, at (0, 1):')
  slope_of_b_to_x(4.0)
  print('********')

def slope_of_5_to_x():
  print('\nApproximating f\'(x) = 5^x, at (0, 1):')
  slope_of_b_to_x(5.0)
  print('********')

def slope_of_e_to_x():
  print('\nApproximating f\'(x) = e^x, at (0, 1):')
  slope_of_b_to_x(math.e)
  print('********')

if __name__ == '__main__':
  slope_of_2_to_x()
  slope_of_3_to_x()
  slope_of_4_to_x()
  slope_of_5_to_x()
  slope_of_e_to_x()

