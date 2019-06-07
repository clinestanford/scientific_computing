#!/usr/bin/python

#####################################
# module: antideriv.py
# YOUR NAME
# YOUR A#
#####################################

from maker import *
import math
from deriv import deriv
import os
import cv2    

def is_e_const(b):
    if isinstance(b, const) and b.get_val() - math.e < .000001:
        return True
    else:
        return False

def get_highest_pwr(expr):
    pass

def antideriv(i):
    ## CASE 1: i is a constant

    if isinstance(i, const):
        return make_prod(i, make_pwr('x', 1))


    elif isinstance(i, pwr):
        b = i.get_base()
        d = i.get_deg()

        #if base is variable, and d is a constant
        if isinstance(b, var) and isinstance(d, const):
            print(d)
            if d.get_val() == -1:
                return make_ln(make_absv(make_pwr('x', 1)))
            return make_prod(make_const(1/(d.get_val() + 1)), make_pwr('x', make_const(d.get_val() + 1)))

        elif is_e_const(b):
            return make_prod(make_quot(make_const(1), deriv(d)), make_e_expr(d))

        elif isinstance(b, plus) and isinstance(d, const):
            return make_prod(make_quot(make_const(1), make_prod(make_const(d.get_val() + 1), deriv(b))), make_pwr_expr(b, make_const(d.get_val() + 1)))

        else:
            raise Exception('antideriv: unknown case')
    


    ### CASE 3: i is a sum, i.e., a plus object.
    elif isinstance(i, plus):
        print(i)
        return make_plus(antideriv(i.get_elt1()), antideriv(i.get_elt2()))
    


    ### CASE 4: is is a product, i.e., prod object,
    ### where the 1st element is a constant.
    elif isinstance(i, prod):

        if isinstance(i.get_mult1(), const):

            if isinstance(i.get_mult2(), pwr):

                #handle case where d == -1
                if isinstance(i.get_mult2().get_deg(), const) and i.get_mult2().get_deg().get_val() == -1:
                    #test to see if x^-1, 
                    if isinstance(i.get_mult2().get_base(), var):
                        return make_prod(i.get_mult1(), make_ln(make_absv(make_pwr('x', 1)))) 

                    else:
                        return make_prod(i.get_mult1(), make_ln(make_absv(i.get_mult2().get_base())))
                return make_prod(i.get_mult1(), antideriv(i.get_mult2()))
            else:
                raise Exception('ANTIDERIV: constant * something uncontrollable')
        
        ##may 1st element whatever and 2nd const
        if isinstance(i.get_mult2(), const):
            if isinstance(i.get_mult1(), pwr):
                return make_prod(i.get_mult2(), antideriv(i.get_mult1()))
            else:
                raise Exception('ANTIDERIV: something uncontrollable * constant')
    else:
        raise Exception('antideriv: unknown case')

                     
            
    
    
