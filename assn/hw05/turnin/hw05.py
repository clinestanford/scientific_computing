#!/usr/bin/python

#!/usr/bin/python

###########################################
# module: hw05.py
# YOUR NAME
# YOUR A#
###########################################

# place the imports necessary for your solution here
from maker import *
from deriv import deriv
from tof import tof



###################### Problem 1 ########################

def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)

    return make_e_expr(make_prod(make_const(k2.get_val()/k1.get_val()), make_pwr('x', 1)))

def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)
    
    return make_prod(y0, make_e_expr(make_prod(k, make_pwr('x', 1))))

############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)
    
    k = math.log(n.get_val()) / t.get_val()

    return make_prod(p0, make_e_expr(make_prod(make_const(k), make_pwr('x', 1))))

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)

    return make_prod(p0, make_e_expr(make_prod(make_const(-1 * lmbda.get_val()), make_pwr('x', 1))))

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    
    return make_const(math.ceil(math.log(c14_percent.get_val())/-.00012))

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    
    der = deriv(demand_eq)
    f_der = tof(der)
    f_eq = tof(demand_eq)

    return make_const((-1 * price.get_val() * f_der(price.get_val())) / f_eq(price.get_val()))

def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)

    elasticity = demand_elasticity(demand_eq, price)

    if elasticity.get_val() > 1:
        return True
    elif elasticity.get_val() < 1:
        return False
    else:
        return True
    

def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or \
           price_direction.get_val() == -1

    is_elastic = is_demand_elastic(demand_eq, price)

    print(is_elastic)

    if is_elastic:
        if price_direction.get_val() == 1:
            return make_const(-1)
        elif price_direction.get_val() == -1:
            return make_const(1)
    else:
        if price_direction.get_val() == 1:
            return make_const(1)
        elif price_direction.get_val() == -1:
            return make_const(-1)


    
