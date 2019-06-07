#!/usr/bin/python

# source code to generate the graph on slide 23
# of lecture 2.
# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec_02_03():
    def f(x): return x**2 + 2.0*x
    def fderiv1(x): return (2.0*x) + 2.0
    def fderiv2(x): return 2.0
    xvals1 = np.linspace(-5, 5, 10000)
    yvals0 = np.array([f(x) for x in xvals1])
    yvals1 = np.array([fderiv1(x) for x in xvals1])    
    yvals2 = np.array([fderiv2(x) for x in xvals1])

    fig1 = plt.figure(1)
    fig1.suptitle('1st and 2nd Derivatives')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-3, 8])
    plt.xlim([-2, 2])
    plt.grid()
    plt.plot(xvals1, yvals0, label="f(x) = x^2 + 2x", c='r') 
    plt.plot(xvals1, yvals1, label="f'(x) = 2x + 2", c='g')
    plt.plot(xvals1, yvals2, label="f''(x) = 2", c='b')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_02_03()
