
import numpy as np 
import matplotlib.pyplot as plt

from maker import *
from deriv import deriv, logdiff
from tof import *


def graph(func, xlim, ylim):
	xvals = np.linspace(xlim[0], xlim[1], 10000)
	yvals1 = np.array([func(i) for i in xvals])
	fig1 = plt.figure(1)
	fig1.suptitle("f(x) and f'(x)")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylim(ylim[0], ylim[1])
	plt.xlim(xlim[0], xlim[1])
	plt.grid()
	plt.plot(xvals, yvals1, label="f(x)="+str(expr), c='r')
	plt.plot(xvals, yvals2, label="f'(x)="+str(der), c='b')
	plt.legend(loc='best')
	plt.show(block=True)

	return 