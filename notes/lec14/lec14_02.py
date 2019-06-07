#!/usr/bin/python

# area under f(x) = -x+4, x in [2, 3]
# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec14_02():
    def f1(x): return -x + 4.0
    #def f2(x): return 2*x - 1
    xvals = np.linspace(0, 4, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    #yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Area under f(x) = -x + 4, x in [2, 3]')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 5])
    plt.xlim([0, 5])
    plt.grid()
    plt.plot(xvals, yvals1, label='f(x)=-x+4', c='r')
    #plt.plot(xvals, yvals2, label='y=2x-1', c='g')
    x1, y1 = [2, 2], [0, int(f1(2))] ## line passing thru (0, 0) and (0, 4)
    x2, y2 = [3, 3], [0, int(f1(3))] ## line passing thru (3, 0) and (3, 4)
    plt.plot(x1, y1, color='b')
    plt.plot(x2, y2, color='b')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec14_02()


