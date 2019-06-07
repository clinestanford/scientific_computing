
from matplotlib import pyplot as plt 


def fit_regression_line(x, y):
	N = len(x)
	assert len(y) == N
	sum_xy = sum(xy[0] * xy[1] for xy in zip(x,y))
	sum_x = sum(xi for xi in x)
	sum_y = sum(yi for yi in y)
	sum_x_sqr = sum(xi**2 for xi in x)
	A = (1.0 * (N*sum_xy - sum_x*sum_y))/(N*sum_x_sqr - sum_x**2)
	B = (sum_y - A*sum_x)/(1.0 * N)
	rlf: lambda x: A*x + B 
	return A, B, rlf
 
def plot(x, y):
	plt.title('title')
	plt.xlabel('xlabel')
	plt.ylabel('ylabel')
	plt.autoscale(tight=True)
	plt.xlim([0,30])
	plt.ylim([0,50])
	A, B, rlf = fit_regression_line(x, y)
	xvals = np.linspace(x[0], 30)
	yvals = np.array([rlf(xv) for xv in xvals])
	plt.plot(xvals, yvals, label='regression line', c='r')
	plt.scatter(x,y)
	plt.legend(loc='best')
	plt.grid()
	plt.show(block=True)


