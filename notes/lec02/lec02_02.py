#!/usr/bin/python

# source code to generate the graph on slide 29
# of lecture 2.
# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec_02_02():
    def f1(x): return 3*(x**2) - 3*x
    def f2(x): return 6*(x**2) - 6*x
    xvals = np.linspace(-5, 5, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Function Plus a Constant vs. Constant Times a Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-2, 5])
    plt.xlim([-1, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label="y=f'(x)=3x^2-3x", c='r')
    plt.plot(xvals, yvals2, label="y=(2f(x))'=6x^2-6x", c='g')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_02_02()
