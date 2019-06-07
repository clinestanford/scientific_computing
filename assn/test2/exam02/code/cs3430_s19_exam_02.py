#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_02.py
# Stanford Cline
# a0154859
##############################################################

## add/modify the imports as needed
from const import const
from maker import make_const, make_plus, make_prod, make_pwr, make_e_expr, make_pwr_expr
from tof import tof
from antideriv import antideriv
from deriv import deriv
from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import cv2
import csv
import scipy as sp

# ************* Problem 1 (3 points) **********************

fexpr_01 = make_pwr('x', 2.0)
fexpr_02 = make_e_expr(make_prod(make_const(-2.0),
                                 make_pwr('x', 1.0)))
fexpr_03 = make_pwr('x', 0.5)
fexpr_04 = make_pwr('x', -2.0)
fexpr_05 = make_pwr('x', -1.0)
fexpr_06 = make_plus(make_pwr('x', -3.0),
                     make_prod(make_const(7.0),
                               make_e_expr(make_prod(make_const(5.0),
                                                     make_pwr('x', 1.0)))))
fexpr_06 = make_plus(fexpr_06, make_prod(make_const(4.0), make_pwr('x', -1.0)))
fexpr_07 = make_prod(make_const(4.0), make_pwr('x', 3.0))
fexpr_08 = make_plus(make_prod(make_const(5.0),
                               make_pwr('x', 1.0)),
                     make_const(-7.0))
fexpr_08 = make_pwr_expr(fexpr_08, -2.0)
fexpr_09 = make_prod(make_const(3.0), make_pwr_expr(make_plus(make_const(2.0),
                                                              make_pwr('x', 1.0)),
                                                    -1.0))
fexpr_10 = make_plus(make_prod(make_const(3.0), make_pwr('x', 1.0)),
                     make_const(2.0))
fexpr_10 = make_pwr_expr(fexpr_10, 4.0)

gt_01 = lambda x: (1.0/3.0)*(x**3)
gt_02 = lambda x: -0.5*(math.e**(-2*x))
gt_03 = lambda x: (2.0/3.0)*(x**1.5)
gt_04 = lambda x: -1.0/x
gt_05 = lambda x: math.log(x, math.e)
gt_06 = lambda x: -0.5*(x**-2.0) + (7.0/5.0)*(math.e**(5.0*x)) + 4*math.log(abs(x), math.e)
gt_07 = lambda x: x**4
gt_08 = lambda x: -0.2*(5.0*x - 7.0)**-1.0
gt_09 = lambda x: 3*math.log(abs(2.0 + x), math.e)
gt_10 = lambda x: 1.0/15*(3.0*x + 2.0)**5.0

# this is your unit test for problem 1.
def test_01():
    test_antideriv(fexpr_01, gt_01, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_02, gt_02, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_03, gt_03, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_04, gt_04, make_const(1), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_05, gt_05, make_const(1), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_06, gt_06, make_const(1), make_const(5), make_const(0.0001))
    test_antideriv(fexpr_07, gt_07, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_08, gt_08, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_09, gt_09, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_10, gt_10, make_const(0), make_const(10), make_const(0.0001))

def test_antideriv(fexpr, gt, lwr, uppr, err):
    assert isinstance(lwr, const)
    assert isinstance(uppr, const)
    assert isinstance(err, const)
    
    prime = antideriv(fexpr)
    func = tof(prime)

    for i in np.linspace(lwr.get_val(), uppr.get_val(), 10):
        assert abs(gt(i) - func(i)) < err.get_val()



# ************* Problem 2 (3 points) **********************

def taylor(fexpr, a, n):
    assert isinstance(a, const)
    assert isinstance(n, const)

    func = tof(fexpr)

    total = func(a.get_val())

    for i in range(n.get_val()-1):
        derNth = deriv(fexpr)
        fexpr = derNth
        funNth = tof(derNth)
        total += (funNth(n.get_val()) / math.factorial(i)) * a.get_val() ** i

    return total

# 3 function expressiosn for problem 2.
fexpr2_01 = make_prod(make_pwr('x', 1.0),
                      make_e_expr(make_pwr('x', 1.0)))
fexpr2_02 = make_plus(make_pwr('x', 4.0),
                      make_pwr('x', 1.0))
fexpr2_02 = make_plus(fexpr2_02, make_const(1.0))
fexpr2_03 = make_pwr_expr(make_plus(make_const(5.0),
                                    make_prod(make_const(-1.0),
                                              make_pwr('x', 1.0))),
                          -1.0)

# 3 gt functions for problem 2.
def gt21_02(x):
    ''' ground truth for 2nd taylor of fexpr2_01. '''
    f0 = tof(fexpr2_01)
    f1 = tof(deriv(fexpr2_01))
    f2 = tof(deriv(deriv(fexpr2_01)))
    return f0(2.0) + f1(2.0)*(x - 2.0) + (f2(2.0)/2)*(x - 2.0)**2

def gt21_03(x):
    ''' ground truth for 3rd taylor for fexpr2_01. '''
    f0 = tof(fexpr2_01)
    f1 = tof(deriv(fexpr2_01))
    f2 = tof(deriv(deriv(fexpr2_01)))
    f3 = tof(deriv(deriv(deriv(fexpr2_01))))
    return f0(2.0) + f1(2.0)*(x-2.0) + (f2(2.0)/2)*(x - 2.0)**2 + \
           (f3(2.0)/6)*(x - 2.0)**3

def gt22_02(x):
    ''' ground truth for 2nd taylor for fexpr2_02. '''
    f0 = tof(fexpr2_02)
    f1 = tof(deriv(fexpr2_02))
    f2 = tof(deriv(deriv(fexpr2_02)))
    return f0(5.0) + f1(5.0)*(x - 5.0) + (f2(5.0)/2)*(x-5.0)**2

def gt22_03(x):
    ''' ground truth for 3rd taylor for fexpr2_02. '''
    f0 = tof(fexpr2_02)
    f1 = tof(deriv(fexpr2_02))
    f2 = tof(deriv(deriv(fexpr2_02)))
    f3 = tof(deriv(deriv(deriv(fexpr2_02))))
    return f0(5.0) + f1(5.0)*(x-5.0) + (f2(5.0)/2)*(x-5.0)**2 + \
           (f3(5.0)/6)*(x - 5.0)**3

def gt23_02(x):
    ''' ground truth for 2nd taylor for fexpr_03. '''
    f0 = tof(fexpr2_03)
    f1 = tof(deriv(fexpr2_03))
    f2 = tof(deriv(deriv(fexpr2_03)))
    return f0(4.0) + f1(4.0)*(x - 4.0) + (f2(4.0)/2)*(x-4.0)**2

def gt23_03(x):
    ''' ground truth for 3rd taylor for fexpr_03. '''
    f0 = tof(fexpr2_03)
    f1 = tof(deriv(fexpr2_03))
    f2 = tof(deriv(deriv(fexpr2_03)))
    f3 = tof(deriv(deriv(deriv(fexpr2_03))))
    return f0(4.0) + f1(4.0)*(x-4.0) + (f2(4.0)/2)*(x-4.0)**2 + \
           (f3(4.0)/6)*(x-4.0)**3

def test_taylor(fexpr, x, n, err, gt):
    assert isinstance(x, const)
    assert isinstance(n, const)
    assert isinstance(err, const)

    print(gt(x.get_val()))

    print(taylor(fexpr, x, n))

    assert abs(gt(x.get_val()) - taylor(fexpr, x, n)) < err.get_val()

           
# this is the unit test for problem 2.   
def test_02():
    test_taylor(fexpr2_01, make_const(2.001), make_const(2), make_const(0.0001), gt21_02)
    test_taylor(fexpr2_01, make_const(2.001), make_const(3), make_const(0.0001), gt21_03)
    test_taylor(fexpr2_02, make_const(5.03), make_const(2), make_const(0.0001), gt22_02)
    test_taylor(fexpr2_02, make_const(5.03), make_const(3), make_const(0.0001), gt22_03)
    test_taylor(fexpr2_03, make_const(4.002), make_const(2), make_const(0.0001), gt23_02)
    test_taylor(fexpr2_03, make_const(4.002), make_const(3), make_const(0.0001), gt23_03)

# ************* Problem 3 (3 points) **********************

## change this variable accordingly if you need to use it.
IMGDIR = 'exam02/img/'

def generate_file_names(ftype, rootdir):
    '''
    recursively walk dir tree beginning from rootdir
    and generate full paths to all files that end with ftype.
    sample call: generate_file_names('.jpg', /home/pi/images/')
    '''
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and \
               file_name.endswith(ftype):
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(ftype, d)

def read_img_dir(ftype, imgdir):
    '''
    takes a file type (e.g., '.jpg') and a directory of images
    (e.g., /home/pi/images/') and returns a list of 2-tuples. In
    each 2-tuple, the first element is the full path to an image
    (e.g., /home/pi/images/img01.jpg') and the second is the numpy
    matrix of that image obtained with cv2.imread().
    '''
    imglst = []
    print(imgdir)
    for imgp in generate_file_names(ftype, imgdir):
        imglst.append((imgp, cv2.imread(imgp)))
    return imglst

def top_n_std(imglist, n, c='B'):

    allList = []
    
    for img in imglist:
        print(img)
        imgMat = img[1]
        b, g, r = cv2.split(imgMat)

        mean = 0
        stdev = 0

        if c == 'B':
            mean = b.mean()
            stdev = np.std(b)
        elif c == 'G':
            mean = g.mean()
            stdev = np.std(g)
        elif c == 'R':
            mean = r.mean()
            stdev = np.std(r)

        allList.append((img[0], mean, stdev))

    return sorted(allList, key=lambda x: x[2])[:n]


def blur_img_list(imglist, kz):

    allList = []
    
    for img in imglist:
        curMat = img[1]
        blurred_img = cv2.filter2D(curMat, -1, kz)
        allList.append((img[0], curMat, blurred_img))

    return allList

# ************* Problem 4 (4 points) **********************

### use this definition if you're in Py2. For Py3, use the
### commented out definition below.
def read_bee_traffic_csv_file(csv_file_path):
    '''
    Takes a bee traffic csv file path and returns 4 numpy
vectors. The first vector contains the time readinds in
seconds (i.e., the firs column values); the second vector
-- the float estimates of the upward bee traffic;
the third vector -- the float estimates of the downward bee
traffic, and the fourth -- the float estimates of the lateral bee
traffic.
    '''
    secsv, upv, downv, latv = [], [], [], []
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        reader.next() #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                  float(row[2]), float(row[3])
            secsv.append(secs)
            upv.append(up)
            downv.append(down)
            latv.append(lat)
    return np.array(secsv), np.array(upv),\
           np.array(downv), np.array(latv)

"""
def read_bee_traffic_csv_file(csv_file_path):
    '''
    Takes a bee traffic csv file path and returns 4 numpy
vectors. The first vector contains the time readinds in
seconds (i.e., the firs column values); the second vector
-- the float estimates of the upward bee traffic;
the third vector -- the float estimates of the downward bee
traffic, and the fourth -- the float estimates of the lateral bee
traffic.
    '''
    secsv, upv, downv, latv = [], [], [], []
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        next(reader) #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                  float(row[2]), float(row[3])
            secsv.append(secs)
            upv.append(up)
            downv.append(down)
            latv.append(lat)
    return np.array(secsv), np.array(upv),\
           np.array(downv), np.array(latv)

"""

### change this variable accordingly.
csv_dir = 'exam02/csv/'
csv_fp_01 = csv_dir + '192_168_4_5-2018-07-01_08-00-10.csv'

def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)

def fit_regression_line(x, y):
    f1 = sp.poly1d(sp.polyfit(x,y,1))
    return f1

def analyze_bee_traffic_data(csv_fp, d='u'):
    beeData = read_bee_traffic_csv_file(csv_fp)

    data = []

    if d == 'u':
        data = beeData[1]
    elif d == 'd':
        data = beeData[2]
    elif d == 'l':
        data = beeData[3]

    time = beeData[0]

    first = fit_regression_line(time, data)
    first_err = error(first, x, y)

    second_vals = sp.polyfit(x,y,2)
    second = lambda x: second_vals[0] * x**2 + second_vals[1] * x + second_vals[2]
    second_err = error(second, x, y)

    third_vals = sp.polyfit(x,y,3)
    third = lambda x: third_vals[0] * x**3 + third_vals[1] * x**2 + third_vals[2] * x + second_vals[3]
    third_err = error(second, x, y)

    tenth_vals = sp.polyfit(x,y,3)
    tenth = lambda x: tenth_vals[0] * x ** 10 +tenth_vals[1] * x ** 9 +tenth_vals[2] * x ** 8 +tenth_vals[3] * x ** 7 +tenth_vals[4] * x ** 6 +tenth_vals[5] * x ** 5 +tenth_vals[6] * x ** 4 +tenth_vals[7] * x ** 3 +tenth_vals[8] * x ** 2 +tenth_vals[9] * x ** 1 + tenth_vals[10]
    tenth_err = error(tenth, x, y)

    print("least squares error: ", first_err)
    print("sp.polyfit 2 error: ", second_err)
    print("sp.polyfit 3 error: ", third_err)
    print("sp.polyfit 10 error: ", tenth_err)

# ************* Problem 5 (2 points) **********************

def gaussia_pdf(x, sigma=1, mu=0):
    a = 1.0 / (sigma * math.sqrt(2*math.pi))
    b = math.e**(-.5*(((x-mu)/sigma)**2))
    return a * b

def bell_curve_iq(a, b, r='m', n=2):

    iqc = lambda x: gaussia_pdf(x, sigma=16, mu=100)

    ### I went through and modified the rules to take in a straight
    ### lambda function instead of taking in an exression.
    
    a = make_const(a)
    b = make_const(b)
    n = make_const(n)

    area = 0

    if r == 'm':
        area += midpoint_rule(iqc, a, b, n).get_val()
    elif r == 't':
        area += trapezoidal_rule(iqc, a, b, n).get_val()
    elif r == 's':
        area += simpson_rule(iqc, a, b, n).get_val()

    return area

if __name__ == '__main__':
    midpoint_rule()

    


    
