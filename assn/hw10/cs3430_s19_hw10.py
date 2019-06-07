#!/usr/bin/python

import math
from PIL import Image
import numpy as np

#######################################################
# module: cs3430_s19_hw10.py
# YOUR NAME
# YOUR A#
########################################################

##################### Problem 1 (4 points) ####################

## a function to convert an rgb 3-tuple to a grayscale value.
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def save_gd_edges(input_fp, output_fp, magn_thresh=20):
    print(output_fp)
    input_image  = Image.open(input_fp)
    output_image = gd_detect_edges(input_image, magn_thresh=magn_thresh)
    output_image.save(output_fp)
    del input_image
    del output_image

def set_borders(img):
    width, height = img.size 
    for i in range(1, width):
        for j in range(1, height):
            assert img.getpixel((i,j)) == 0

    for i in range(0, width):
        img.putpixel((i, 0), 255)
        img.putpixel((i, height-1), 255)

    for j in range(0, height):
        img.putpixel((0, j), 255)
        img.putpixel((width-1, j), 255)

    return img

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


def gd_detect_edges(rgb_img, magn_thresh=30):
    width, height = rgb_img.size

    grayed = get_gray_lumin(rgb_img)

    new = Image.new("L", (width, height))
    new = set_borders(new)

    for i in range(1,width-1):
        for j in range(1,height-1):
            #thetas[i,j], grads[i,j] = get_theta_grad(grayed, (i,j))
            theta, grad = get_theta_grad(grayed, (i,j))
            direction = abs(math.degrees(theta)) / 90
            if grad * theta > magn_thresh:
                new.putpixel((i,j), 255)

    return new

###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    assert img1.size == img2.size
    
    width, height = img1.size

    num = left = right = 0

    for i in range(width):
        for j in range(height):
            num += img1.getpixel((i,j)) * img2.getpixel((i,j))
            left += img1.getpixel((i,j)) ** 2 
            right += img2.getpixel((i,j)) ** 2

    return num / (math.sqrt(left) * math.sqrt(right))
'''
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
0.512202985103
>>> test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.352152693884
>>> test_cosine_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.352152693884
'''
def test_cosine_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = cosine_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def euclid_sim(img1, img2):
    assert img1.size == img2.size
    width, height = img1.size 

    tot = 0

    for i in range(width):
        for j in range(height):
            tot += (img1.getpixel((i,j)) - img2.getpixel((i,j)))**2

    return math.sqrt(tot)


'''
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
0.0
>>> test_euclid_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
16981.9278941
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
16981.9278941
'''
def test_euclid_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = euclid_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def jaccard_sim(img1, img2):
    assert img1.size == img2.size
    width, height = img1.size 

    set1 = set() 
    set2 = set()

    for i in range(width):
        for j in range(height):
            set1.add(img1.getpixel((i,j)))
            set2.add(img2.getpixel((i,j)))



    return len(set.intersection(set1, set2)) / len(set.union(set1, set2))



'''
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.934065934066
>>> test_jaccard_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.934065934066
'''
def test_jaccard_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = jaccard_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def test_01():
    #save_gd_edges('img/1b_bee_01.png', 'img/1b_bee_01_ed.png', magn_thresh=20)
    #save_gd_edges('img/output11885.jpg', 'img/1b_bee_01_ed.png', magn_thresh=20)
    #save_gd_edges('img/EdgeImage_03.jpg', 'img/EdgeImage_03_ed.jpg', magn_thresh=20)
    #save_gd_edges('img/EdgeImage_03.jpg', 'img/EdgeImage_03_ed.jpg', magn_thresh=20)
    # save_gd_edges('img/1b_bee_10.png', 'img/1b_bee_10_ed.png', magn_thresh=20)
    # save_gd_edges('img/2b_nb_10.png', 'img/2b_nb_10_ed.png', magn_thresh=20)
    # save_gd_edges('img/2b_nb_21.png', 'img/2b_nb_21_ed.png', magn_thresh=20)
    save_gd_edges('img/elephant.jpg', 'img/elephant_ed.jpg', magn_thresh=30)
    # save_gd_edges('img/output11885.jpg', 'img/output11885_ed.jpg', magn_thresh=20)
    # save_gd_edges('img/2b_nb_09.png', 'img/2b_nb_09_ed.png', magn_thresh=20)
    # save_gd_edges('img/output11884.jpg', 'img/output11884_ed.jpg', magn_thresh=20)

## testing the PIL/PILLOW installation
def test_02():
    img = Image.open('img/1b_bee_01.png').convert('LA')
    img2 = img.save('img/1b_bee_01_gray.png')
    del img
    del img2
    
if __name__ == '__main__':
    #test_01()
    #test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
    #test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
    test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
    test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')

