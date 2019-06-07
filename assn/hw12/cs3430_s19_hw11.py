#!/usr/bin/python

########################################
# module: cs3430_s19_hw11.py
# YOUR NAME
# YOUR A#
########################################

## add your imports here
import math
from PIL import Image
import sys
import numpy as np
import cv2

from tof import tof
from const import const
from var import var
from pwr import pwr
from maker import make_const, make_pwr, make_prod, make_quot
from maker import make_plus, make_ln, make_absv
from maker import make_pwr_expr, make_e_expr
from plus import plus
from prod import prod
from deriv import deriv


################# Problem 1 (1 point) ###################

def nra(poly_fexpr, g, n):
    
    der = deriv(poly_fexpr)
    func = tof(poly_fexpr)
    der_func = tof(der)
    x = g.get_val()
    for _ in range(n.get_val()):
        x = x - (func(x) / der_func(x))

    print(x)
    return make_const(x)

################# Unit Tests for Problem 1 ###################

def nra_ut_01():
    ''' Approximating x^2 - 2 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_02():
    ''' Approximating x^2 - 3 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-3.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_03():
    ''' Approximating x^2 - 5 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-5.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_04():
    ''' Approximating x^2 - 7 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-7.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_05():
    ''' Approximating e^-x = x^2. '''
    fexpr = make_e_expr(make_prod(make_const(-1.0),
                                  make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr,
                      make_prod(make_const(-1.0),
                                make_pwr('x', 2.0)))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_06():
    ''' Approximating 11^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-11.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_07():
    ''' Approximating 6^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-6.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_08():
    ''' Approximating x^3 + 2x + 2. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_prod(make_const(2.0),
                                make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr, make_const(2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_09():
    ''' Approximating x^3 + x - 1. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-1.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_10():
    ''' Approximating e^(5-x) = 10 - x. '''
    fexpr = make_e_expr(make_plus(make_const(5.0),
                                  make_prod(make_const(-1.0),
                                            make_pwr('x', 1.0))))
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-10.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


# =================== Problem 2 (4 points) ===================

def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def get_theta_grad(img, pix):
    x, y = pix

    dy = img.getpixel((x, y-1)) - img.getpixel((x, y+1))
    dx = img.getpixel((x-1, y)) - img.getpixel((x+1, y))

    if dy < 1: dy = 1.0 
    if dx < 1: dx = 1.0 

    return (math.atan(dy/dx), abs(math.sqrt(dy ** 2 + dx ** 2)))

def get_gray_lumin(img):
    width, height = img.size
    grayed = Image.new('L', (width, height))

    for i in range(width):
        for j in range(height):
            grayed.putpixel((i,j), math.floor(luminosity(img.getpixel((i,j)))))

    return grayed

def get_gradient_img(img, magn_thresh):
    width, height = img.size 
    grads = Image.new("L", (width,height))

    for i in range(1,width-1):
        for j in range(1,height-1):
            #thetas[i,j], grads[i,j] = get_theta_grad(grayed, (i,j))
            theta, grad = get_theta_grad(img, (i,j))
            direction = abs(math.degrees(theta)) / 90
            if grad * theta > magn_thresh:
                grads.putpixel((i,j), 255)

    return grads

def get_x_and_y(theta, p):
    return (p * math.cos(theta), p * math.sin(theta))

def get_func(x1, y1, m):
    return lambda x: m * x - m * x1 + y1

def deg_to_rad(x):
    return x * (math.pi/180)

def ht_detect_lines(img_fp, magn_thresh=20, spl=20):
    print(spl)
    img  = Image.open(img_fp)
    blue = img.copy()

    width, height = img.size

    gray = 0

    if len(img.getpixel((0,0))) >= 3:
        gray = get_gray_lumin(img)
    else:
        gray = img

    edges = get_gradient_img(gray, magn_thresh)

    print(edges.getpixel((100,10)))

    ht_width = 180
    ht_height = int(math.sqrt(width**2 + height**2))

    ht = np.zeros((ht_width, ht_height)) ##need to figure out the first number

    for i in range(width):
        for j in range(height):
            if edges.getpixel((i,j)) == 255:
                for k in range(ht_width):
                    # k represents theta in degrees
                    theta = deg_to_rad(k)
                    p = int(i * math.cos(theta) + j * math.sin(theta))
                    if p >= 0 and p < ht_height:
                        ht[k, p] += 1

    for i in range(ht_width):
        for j in range(ht_height):
            if ht[i, j] >= spl:
                theta = deg_to_rad(i)
                x, y = get_x_and_y(theta, j)
                m = -1 * (math.cos(theta) / math.sin(theta))
                func = get_func(x, y, m)

                for x in range(width):
                    try:
                        blue.putpixel((x, int(func(x))), (0,0,255))
                    except Exception:
                        pass
                        #print('index out of bounds')

    return (img, np.array(blue), edges, ht)

################ Unit Tests for Problem 2 ####################
##        
## I used Image for edge detection and numpy image representation
## to draw lines. Hence, I am using cv2.imwrite to save the
## image with drawn line (lnimg) and image.save to save the image
## with the edges. Feel free to modify but keep the signatures
## of these tests the same.
        
def ht_test_01(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im01_ln.png', lnimg)
    edimg.save('im01_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_02(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im02_ln.png', lnimg)
    edimg.save('im02_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_03(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im03_ln.png', lnimg)
    edimg.save('im03_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_04(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im04_ln.png', lnimg)
    edimg.save('im04_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_05(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im05_ln.png', lnimg)
    edimg.save('im05_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_06(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im06_ln.png', lnimg)
    edimg.save('im06_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_07(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im07_ln.png', lnimg)
    edimg.save('im07_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_08(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im08_ln.png', lnimg)
    edimg.save('im08_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_09(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im09_ln.png', lnimg)
    edimg.save('im09_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_10(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im10_ln.png', lnimg)
    edimg.save('im10_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_11(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im11_ln.png', lnimg)
    edimg.save('im11_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_12(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im12_ln.png', lnimg)
    edimg.save('im12_ed.png')
    del img
    del lnimg
    del edimg
    
if __name__ == '__main__':
    ht_test_01('img/EdgeImage_01.jpg', 20, 60)
    #ht_test_01('img/kitchen.jpeg')
    #nra_ut_05()

    # x,y = get_x_and_y(deg_to_rad(60), 4)

    # func = get_func(x, y, -1 * math.cos(deg_to_rad(60))/math.sin(deg_to_rad(60)))
    # print(func(4))
