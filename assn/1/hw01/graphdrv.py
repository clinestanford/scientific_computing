#!/usr/bin/python

###########################################
# module: graph_drv.py
# Your Name
# Your A#
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt
import math

def graph_drv(fexpr, xlim, ylim):
	der = deriv(fexpr)
	eqF  = tof(fexpr)
	derF = tof(der)
	xvals = np.linspace(xlim[0], xlim[1], 10000)
	yvals1 = np.array([eqF(i) for i in xvals])
	yvals2 = np.array([derF(i) for i in xvals])
	fig1 = plt.figure(1)
	fig1.suptitle("f(x) and f'(x)")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylim(ylim[0], ylim[1])
	plt.xlim(xlim[0], xlim[1])
	plt.grid()
	plt.plot(xvals, yvals1, label="f(x)="+str(fexpr), c='r')
	plt.plot(xvals, yvals2, label="f'(x)="+str(der), c='b')
	plt.legend(loc='best')
	plt.show(block=True)




    