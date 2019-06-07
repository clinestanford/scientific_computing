#!/usr/bin/python

# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt
import math

def lec_20_04():
    def f1(x): return math.e**x - 4.0
    def f2(x): return x
    xvals = np.linspace(0, 2, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('e^x - 4 = x.')
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.ylim([-1, 2])
    plt.xlim([1, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label='y=e^x - 4', c='r')
    plt.plot(xvals, yvals2, label='y=x', c='g')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_20_04()


