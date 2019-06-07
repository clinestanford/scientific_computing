#!/usr/bin/python

#####################################
# module: lec03_prob_01.py
# description: solution to problem 1 in
# lecture 3 - comparing instantaneous rate of
# change with average rate of change
# by shrinking the interval
# bugs to vladimir kulyukin on canvas.
####################################

intervals = ((1.0, 2.0), (1.0, 1.5), (1.0, 1.25),
             (1.0, 1.1), (1.0, 1.01), (1.0, 1.001),
             (1.0, 1.0001))

def f1(x): return x**2
def df1(x): return 2*x

def avrg_rate(f, l, u):
  return (f(u)-f(l))/(u - l)

def test_avrg_rates(f, df, intervals):
  for l, u in intervals:
    ar = avrg_rate(f, l, u)
    print ar, abs(df(l) - ar)

if __name__ == '__main__':
  test_avrg_rates(f1, df1, intervals)
