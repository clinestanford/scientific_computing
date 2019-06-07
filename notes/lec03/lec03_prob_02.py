#!/usr/bin/python

#####################################
# module: lec03_prob_02.py
# description: solution to problem 2 in
# lecture 3
# bugs to vladimir kulyukin on canvas.
####################################

import numpy as np
import matplotlib.pyplot as plt

def lec_03_prob_02():
    def f(x): return (1.0/3)*(x**3) - 2.0*(x**2) + 3.0*x + 1.0
    def drv1(x): return x**2 - 4.0*x + 3.0
    xvals1 = np.linspace(-5, 5, 10000)
    yvals0 = np.array([f(x) for x in xvals1])
    yvals1 = np.array([drv1(x) for x in xvals1])    

    fig1 = plt.figure(1)
    fig1.suptitle('Local extreme points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-2, 10])
    plt.xlim([-2, 5])
    plt.grid()
    plt.plot(xvals1, yvals0, label="f(x)=(1/3)x^3 - 2x^2 + 3x + 1", c='r') 
    plt.plot(xvals1, yvals1, label="f'(x)=x^2 - 4x + 3", c='g')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_03_prob_02()
