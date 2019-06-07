#!/usr/bin/python

#############################################
# module: hw06_s19.py
# YOUR NAME
# YOUR A#
#############################################

# These are the imports I used to implement my 
# solutions. Modify them as you see fit but
# make sure all your imports are zipped in your
# submission.

import math
import numpy as np
import matplotlib.pyplot as plt

from const import const
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from tof import tof
from deriv import deriv

## ************* Problem 1 ******************

def percent_retention_model(lmbda, a):
	assert isinstance(lmbda, const)
	assert isinstance(a, const)

	e_expr = make_e_expr(make_prod(make_const(-1 * lmbda.get_val()), make_pwr('x', 1)))
	sub_expr = make_plus(make_const(100), make_const(-1 * a.get_val()))
	expr = make_plus(make_prod(sub_expr, e_expr), a)
	print(expr)
	print('here')

	return expr

def plot_retention(lmbda, a, t0, t1):
	assert isinstance(lmbda, const)
	assert isinstance(a, const)
	assert isinstance(t0, const)
	assert isinstance(t1, const)

	xvals = np.linspace(t0.get_val(), t1.get_val(), 10000)
	expr = percent_retention_model(lmbda, a)
	der_expr = deriv(expr)

	func_expr = tof(expr)
	func_der = tof(der_expr)

	yvals1 = np.array([func_expr(i) for i in xvals])
	yvals2 = np.array([func_der(i) for i in xvals])

	ally = np.concatenate([yvals1, yvals2])

	ymin = np.amin(ally)
	ymax = np.amax(ally)
	
	fig1 = plt.figure(1)
	fig1.suptitle("Ebbinghaus Model of Forgetting")
	plt.xlabel('t')
	plt.ylabel('prf and dprf')
	plt.ylim(ymin, ymax)
	plt.xlim(t0.get_val(), t1.get_val())
	plt.grid()
	plt.plot(xvals, yvals1, label="prf", c='r')
	plt.plot(xvals, yvals2, label="dprf", c='b')
	plt.legend(loc='best')
	plt.show(block=True)


## ************* Problem 2 ******************

def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
	assert isinstance(p, const) and isinstance(t0, const)
	assert isinstance(p0, const) and isinstance(t1, const)

	xvals = np.linspace(tl.get_val(), tu.get_val(), 10000)
	expr = spread_of_disease_model(p, t0, p0, t1, p1)
	print(expr)

	der_expr = deriv(expr)

	func_expr = tof(expr)
	func_der = tof(der_expr)

	yvals1 = np.array([func_expr(i) for i in xvals])
	yvals2 = np.array([func_der(i) for i in xvals])

	ally = np.concatenate([yvals1, yvals2])

	ymin = np.amin(ally)
	ymax = np.amax(ally)
	
	fig1 = plt.figure(1)
	fig1.suptitle("Spread of Disease")
	plt.xlabel('t')
	plt.ylabel('sdf and dsdf')
	plt.ylim(ymin, ymax)
	plt.xlim(tl.get_val(), tu.get_val())
	plt.grid()
	plt.plot(xvals, yvals1, label="sdf", c='r')
	plt.plot(xvals, yvals2, label="dsdf", c='b')
	plt.legend(loc='best')
	plt.show(block=True)



def spread_of_disease_model(p, t0, p0, t1, p1):
	assert isinstance(p, const) and isinstance(t0, const)
	assert isinstance(p0, const) and isinstance(t1, const)
	
	b = (p.get_val() / p0.get_val()) - 1 
	c = math.log(((p.get_val()/p1.get_val())-1)/b)/t1.get_val()

	e_expr = make_e_expr(make_prod(make_const(c), make_pwr('x', 1)))
	denom = make_plus(make_const(1), make_prod(make_const(b), e_expr))

	return make_quot(p, denom)


	
## ************* Problem 3 ******************

def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
	assert isinstance(m, const) and isinstance(t1, const)
	assert isinstance(x1, const) and isinstance(t2, const)
	assert isinstance(x2, const) and isinstance(tl, const)
	assert isinstance(tu, const)

	xvals = np.linspace(tl.get_val(), tu.get_val(), 10000)
	expr = plant_growth_model(m, t1, x1, t2, x2)
	print(expr)

	der_expr = deriv(expr)

	func_expr = tof(expr)
	func_der = tof(der_expr)

	yvals1 = np.array([func_expr(i) for i in xvals])
	yvals2 = np.array([func_der(i) for i in xvals])

	ally = np.concatenate([yvals1, yvals2])

	ymin = np.amin(ally)
	ymax = np.amax(ally)
	
	fig1 = plt.figure(1)
	fig1.suptitle("Spread of Disease")
	plt.xlabel('t')
	plt.ylabel('sdf and dsdf')
	plt.ylim(ymin, ymax)
	plt.xlim(tl.get_val(), tu.get_val())
	plt.grid()
	plt.plot(xvals, yvals1, label="sdf", c='r')
	plt.plot(xvals, yvals2, label="dsdf", c='b')
	plt.legend(loc='best')
	plt.show(block=True)

def plant_growth_model(m, t1, x1, t2, x2):
	assert isinstance(m, const) and isinstance(t1, const)
	assert isinstance(x1, const) and isinstance(x2, const)
	assert isinstance(x2, const)

	t_1 = t1.get_val()
	t_2 = t2.get_val()
	h_1 = x1.get_val()
	h_2 = x2.get_val()
	m_init = m.get_val()

	r = math.log(((m_init/h_2) - 1)/((m_init/h_1) - 1)) / (t_2 - t_1)
	print(r)
	a_1 = ((m_init/h_1) - 1) / (math.e ** (r * t_1))
	a_2 = ((m_init/h_2) - 1) / (math.e ** (r * t_2))

	num = m 
	denom = make_plus(make_const(1), make_prod(make_const(a_1), make_e_expr(make_prod(make_const(r), make_pwr('x', 1)))))

	return make_quot(num, denom)
									  
## ************* Problem 4 ******************

def spread_of_news_model(p, k):
	assert isinstance(p, const) and isinstance(k, const)
	exponent = make_prod(make_const(-1 * k.get_val()), make_pwr('x', 1))
		
	expr = make_plus(p, make_prod(make_const(-1), make_prod(p, make_e_expr(exponent))))
	return expr


def plot_spread_of_news(p, k, tl, tu):
	assert isinstance(p, const) and isinstance(k, const)
	assert isinstance(tl, const) and isinstance(tu, const)

	expr = spread_of_news_model(p, k)
	
	der_expr = deriv(expr)

	func_expr = tof(expr)
	func_der = tof(der_expr)

	xvals = np.linspace(tl.get_val(), tu.get_val(), 10000)
	yvals1 = np.array([func_expr(i) for i in xvals])
	yvals2 = np.array([func_der(i) for i in xvals])

	ally = np.concatenate([yvals1, yvals2])

	ymin = np.amin(ally)
	ymax = np.amax(ally)

	fig1 = plt.figure(1)
	fig1.suptitle("Spread of News")
	plt.xlabel('t')
	plt.ylabel('snf and dsnf')
	plt.ylim(ymin-2000, ymax+2000)
	plt.xlim(tl.get_val(), tu.get_val())
	plt.grid()
	plt.plot(xvals, yvals1, label="snf", c='r')
	plt.plot(xvals, yvals2, label="dsnf", c='b')
	plt.legend(loc='best')
	plt.show(block=True)



 
