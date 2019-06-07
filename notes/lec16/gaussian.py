#!/usr/bin/python

#########################################
# module: gaussian.py
# description: various gaussian curves.
# bugs to vladimir kulyukin via canvas
#########################################

import math
import numpy as np
import matplotlib.pyplot as plt

def gaussian_pdf(x, sigma=1, mu=0):
    '''
    standard gaussian probability distribution with
    mu being the mean and sigma being the standard
    deviation.
    '''
    a = 1.0/(sigma*math.sqrt(2*math.pi))
    b = math.e**(-0.5*(((x - mu)/sigma)**2))
    return a*b

def gaussian_pdf_plots():
    xvals = np.linspace(-10, 10, 10000)
    gauss1 = lambda x: gaussian_pdf(x, sigma=0.447, mu=0)
    gauss2 = lambda x: gaussian_pdf(x, sigma=1, mu=0)
    gauss3 = lambda x: gaussian_pdf(x, sigma=2.24, mu=0)
    yvals1 = np.array([gauss1(x) for x in xvals])
    yvals2 = np.array([gauss2(x) for x in xvals])
    yvals3 = np.array([gauss3(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Gaussian Curves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([-10, 10])
    plt.ylim([0, 1])
    plt.grid()
    plt.plot(xvals, yvals1, label='s=0.447;mu=0', c='r')
    plt.plot(xvals, yvals2, label='s=1;mu=0', c='g')
    plt.plot(xvals, yvals3, label='s=2.24;mu=0', c='b')
    plt.legend(loc='best')
    plt.show()

def gaussian_pdf_plots2():
    xvals = np.linspace(-10, 10, 10000)
    gauss1 = lambda x: gaussian_pdf(x, sigma=0.447, mu=-2)
    gauss2 = lambda x: gaussian_pdf(x, sigma=1, mu=1)
    gauss3 = lambda x: gaussian_pdf(x, sigma=2.24, mu=2)
    yvals1 = np.array([gauss1(x) for x in xvals])
    yvals2 = np.array([gauss2(x) for x in xvals])
    yvals3 = np.array([gauss3(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Gaussian Curves 2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([-10, 10])
    plt.ylim([0, 1])
    plt.grid()
    plt.plot(xvals, yvals1, label='s=0.447;mu=-2', c='r')
    plt.plot(xvals, yvals2, label='s=1;mu=1', c='g')
    plt.plot(xvals, yvals3, label='s=2.24;mu=2', c='b')
    plt.legend(loc='best')
    plt.show()

def gaussian_iq_curve():
    xvals = np.linspace(0, 200, 10000)
    gauss1 = lambda x: gaussian_pdf(x, sigma=16.0, mu=100)
    yvals1 = np.array([gauss1(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Gaussian IQ Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([50, 150])
    #plt.ylim([0, 1])
    plt.grid()
    plt.plot(xvals, yvals1, label='s=16;mu=100', c='b')
    plt.legend(loc='best')
    plt.show() 
    
if __name__ == '__main__':
    gaussian_pdf_plots()
    gaussian_pdf_plots2()
    gaussian_iq_curve()
    pass
    


 
