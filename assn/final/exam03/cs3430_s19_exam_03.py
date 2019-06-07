#!/usr/bin/python

#########################################
# module: cs3430_s19_exam_03.py
# Your name
# Your A#
#########################################

## your imports
'''
import math
import numpy as np
from newton_raphson import nra_sqrt, nra
from maker import make_e_expr, make_prod, make_const
from maker import make_pwr, make_plus
import matplotlib.pyplot as plt
'''

# ========== PROBLEM 1 =================

###### Problem 1.1 ############

'''
No, I don't think Jaccard would perform the best because it deals mostly with 
the difference between the sets of the individual pictures and doesnt take
into consideration the lcation.I think that cosine would perform well because
it does take into consideration the location of the pixel.
'''

##### Problem 1.2 ############

'''
Canny will run through a gaussian filter which makes it great at detecting edges
in certain types of images but not necessarily with the given one because of the
blend from one color to the next. The graident-edge detection worked because it was
able to detect where the gradient and theta were above a certain threshold.
'''

#### Problem 1.3 #############

'''
it would be possible to vectorize the code. You could have a matrix representing
the gradients and another the thetas. by using Matrices, it would make it possible
to find the location of all pixels over the threshold and setting them to white.
'''

#### Problem 1.4 #############

'''
For this one, it would be useful to precompute all of the sines and cosines ahead
of time, because this is an operation that we are going to be using a lot, and repeating
the same computation. For this reason, if we precomputed them, we could call with O(1)
time rather than having to compute each time.
'''

#### Problem 1.5 #############

'''
textures each have its own look. Hough's Transform can be adapted to look for specific 
shapes in images. Depending on the kind of texture I am looking for, I can modify Hough's
Transform, and look for those types of edges.This would do well at detecting leopard spots,
or other such textures.
'''

#### Problem 1.6 #############

'''
I would begin by finding several instances of what we are looking for and average their
histograms to have a good idea of what I am looking for. From there i would use a sliding
image frame with different pixel sizes on the image to detect images that are going to be
similar to what I already have computed. Save the coordinates of the pixels, and see if it
worked.
'''

from cs3430_s19_hw11 import ht_detect_lines

#### Problem 1.7 #################

#def ht_detect_lines(img_fp, magn_thresh=20, spl=20):
def detect_lines(impath1, impath2, magn_thresh=20, spl=20):
  img, blue, edges, ht = ht_detect_lines(impath1, magn_thresh, spl)
  cv2.imwrite(impath2, blue)


# ========== PROBLEM 2 (3 points) =================

#### Problem 2.1 #############

'''
The objective function is the pounds of each bag, multiplied by its profit per bag
A is the matrix of each bag and what it used, b is the total pounds that we have of
each element. Solve this matrix, and use the objective function to try and maximize it.
'''

#### Problem 2.2 #############

'''
2.
'''

#### Problem 2.3 #############

'''
4. 
'''

#### Problem 2.4 #############

'''
4.
'''

#### Problem 2.5 #############

from linprog import line_intersection
from linprog import maximize_obj_fun

def problem_2_5():
  ln1 = make_line_eq(make_var('y'), make_const(0.0))
  ln2 = make_line_eq(make_var('x'), make_const(0.0))
  ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-.5),make_pwr('x', 1.0)),
                        make_const(3.0)))
  ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0),make_pwr('x', 1.0)),
                        make_const(4.0)))

  ln5 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-2.0),make_pwr('x', 1.0)),
                        make_const(8.0)))

  p1 = line_intersection(ln2, ln3)
  p2 = line_intersection(ln2, ln4)
  p3 = line_intersection(ln4, ln5)
  p4 = line_intersection(ln3, ln5)


  f = lambda x, y: x + y 

  corner_points = [p1, p2, p3, p4]

  p, val = minimize_obj_fun(f, corner_points)
  print(p, val)
  return (p, val)

# ========== PROBLEM 3 (3 points) =================

#### Problem 3.1 #############

def problem_3_1():
  x = None
  A = np.array([[1,1,2],
                [2,4,3],
                [3,6,-5]])
  b = np.array([9,1,0])

  x = np.linalg.solve(a, b)
  return x

#### Problem 3.2 #############

def problem_3_2():
  
  A = np.array([1,2,3])
  B = np.array([2,4,3])
  C = np.array([3,6,-5])
  y = np.array([9,1,0])

  det = np.linalg.det(np.transpose(np.array([A,B,C])))

  a = np.linalg.det(np.transpose(np.array([y,B,C]))) / det
  b = np.linalg.det(np.transpose(np.array([A,y,C]))) / det
  c = np.linalg.det(np.transpose(np.array([A,B,y]))) / det 

  return np.array([a,b,c])

#### Problem 3.3 #############

def satyamitra_numbers_in_range(lower, upper):
  
  factors = []  
  for i in range(lower, upper):
    factors.append(sum(x for x in range(i) if i % x == 0))

  sol = []

  for i in range(factors):
    cur = factors[i]
    other = factors[cur]

    if factors[cur - lower] == other and factors[other - lower] == cur:
      sol.append((cur, other))

    return sol

import math

def satyamitra_matrix(sn_list):
  square = math.sqrt(len(sn_list) * 2)

  all = []
  for i in len(sn_list):
    all.append(sn_list[0])
    all.append(sn_list[1])

  x = np.array(all)
  return np.reshape(x, (square, square))

def is_satyamitra_matrix_singular():
    
  mat = satyamitra_matrix(1,20000)
  square = satyamitra_matrix(mat)
  root = math.sqrt(len(mat) * 2)
  if np.linalg.matrix_rank(square) < root:
    return False
  else:
    return True




# ========== PROBLEM 4 (3 points) =================

#### Problem 4.1 #############

'''
4.
'''

#### Problem 4.2 #############

from grapher import graph 

def problem_4_2():
  f = lambda x: math.exp(5 * x) + 2 
  graph(f, [-2,2], [0,10])




#### Problem 4.3 #############

'''
1.
'''

#### Problem 4.4 #############

'''
2. 
'''

# ========== PROBLEM 5 (3 points) =================

#### Problem 5.1 #############

from cs3430_s19_hw11 import nra
from maker import *

def problem_5_1():
  exp1 = make_e_expr(make_plus(make_const(10.0), make_pwr('x', 1.0)))
  exp2 = make_plus(make_pwr('x', 1.0), make_const(-20))
  exp3 = make_plus(exp1, exp2)

  val = nra(exp3, make_const(4), make_const(20))

  return val.get_val()



#### Problem 5.2 #############

def pell_sqrt(n, lwr=0, upr=5000):

  ##no idea honestly

  for i in range(lwr, upr):
    root = int(math.sqrt(n))
    if root * root == i:
      continue


def test_pell_sqrt(lwr, uppr):
  for i in range(lwr, uppr+1):
    try:
      print('pell_sqrt(' + str(i) + ')=' + str(pell_sqrt(i)) + '; ' + \
            'math.sqrt(' + str(i) + ')=' + str(math.sqrt(i)))
    except Exception, e:
      print(str(i) + ' --> ' + str(e))




  



