################################################################################
#
#    hw11
#
#  Fill in TODO to implement Euler and Runge-Kutta
#
#      Solve y'=(2t)y  y(1)=1 over 0 <= t <= 10 numerically
#
#      Use SciPy notation:  y' = f(t, y)
#
#        This is first order.  However recall there is an ODE trick to convert
#        higher order ODEs into systems of first order.
#
#
#################################################################################


import numpy as np
from math import exp
from matplotlib import pyplot as plt


# TODO :: implement the Runge-Kutta algorithm below
def rk4(f, t0, y0, tmin, tmax, step_size):


# TODO :: implement the EULER algorithm below
def euler(f, t0, y0, tmin, tmax, step_size):


def f(t, y):
	return (2*t)*y


def exact(t):
	return exp(t**2 - 1)


if __name__ == "__main__":
	t0 = 1
	y0 = 1
	tMIN = 1
	tMAX = 2.5
	step_size = 0.25

	# TODO :: Change my name to yours
	plt.title('Tony Perkins :: ODE solver')

	SOLN_tvals = np.linspace(tMIN, tMAX, 100)
	SOLN_yvals = [exact(t) for t in SOLN_tvals]
	soln, = plt.plot(SOLN_tvals, SOLN_yvals, linewidth = 2)


	tvals, yvals = rk4( f, t0, y0, tMIN, tMAX, step_size)
	rk, = plt.plot(tvals, yvals, marker='o')

	tvals, yvals = euler( f, t0, y0, tMIN, tMAX, step_size)
	e, = plt.plot(tvals, yvals, marker='o')

	plt.legend([soln, rk, e], ['Exact Solution', 'Runge-Kutta', 'Euler'], loc=2)
	plt.savefig("hw11_rk4.png")
	plt.show()
