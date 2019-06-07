#!/usr/bin/python

# source code to generate the graph on slide 18
# of lecture 1.
# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec_02_01():
    def f1(x): return x**3 - (3.0/2.0)*(x**2)
    def f2(x): return f1(x) + 1
    def f3(x): return f1(x) + 2
    def f4(x): return 2*f1(x)
    xvals = np.linspace(-10, 10, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    yvals3 = np.array([f3(x) for x in xvals])
    yvals4 = np.array([f4(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Function Plus a Constant vs. Constant Times a Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 5])
    plt.xlim([-1, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label='y=f(x)', c='r')
    plt.plot(xvals, yvals2, label='y=f(x)+2', c='g')
    plt.plot(xvals, yvals3, label='y=f(x)+3', c='b')
    plt.plot(xvals, yvals4, label='y=2f(x)', c='m')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_02_01()
