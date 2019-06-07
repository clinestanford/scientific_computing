#!/usr/bin/python

#####################################
# module: lec03_prob_04.py
# description: solution to problem 4 in
# lecture 3
# bugs to vladimir kulyukin on canvas.
####################################

import numpy as np
import matplotlib.pyplot as plt

def lec_03_prob_04():
    def f(x): return (x**3) - 3.0*(x**2) + 5.0
    def drv1(x): return 3.0*(x**2) - 6.0*x
    xvals1 = np.linspace(-5, 5, 10000)
    yvals0 = np.array([f(x) for x in xvals1])
    yvals1 = np.array([drv1(x) for x in xvals1])    

    fig1 = plt.figure(1)
    fig1.suptitle('Local extreme points and concavity')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-4, 6])
    plt.xlim([-2, 4])
    plt.grid()
    plt.plot(xvals1, yvals0, label="f(x) = x^3 - 3x^2 + 5", c='r') 
    plt.plot(xvals1, yvals1, label="f'(x) = 3x^2 - 6x", c='g')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_03_prob_04()
