#!/usr/bin/python


# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec_20_01():
    def f1(x): return x**3 - x - 2
    xvals = np.linspace(-5, 5, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Zero of p(x) = x^3 - x - 2, x in [1, 2].')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-1, 4])
    plt.xlim([1, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label='y=x^3 - x - 2', c='r')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_20_01()


