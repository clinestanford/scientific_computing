#!/usr/bin/python

#############################################
# module: antideriv.py
# description: three antiderivatives of
# f(x) = x^2
# bugs to vladimir dot kulyukin via canvas. 
#############################################

import math
import numpy as np
import matplotlib.pyplot as plt


def plot_antiderivatives(t0, t1):
    xvals = np.linspace(t0, t1, 10000)
    a1 = lambda x: (1.0/3.0)*(x**3)
    a2 = lambda x: (1.0/3.0)*(x**3) + 2
    a3 = lambda x: (1.0/3.0)*(x**3) + 4
    yvals1 = np.array([a1(x) for x in xvals])
    yvals2 = np.array([a2(x) for x in xvals])
    yvals3 = np.array([a3(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Plots of Antiderivatives of f(x) = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([t0, t1])
    plt.grid()
    plt.plot(xvals, yvals1, label='(1/3)x^3', c='red')
    plt.plot(xvals, yvals2, label='(1/3)x^3+2', c='blue')
    plt.plot(xvals, yvals3, label='(1/3)x^3+4', c='green')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    plot_antiderivatives(-2, 2)



 
