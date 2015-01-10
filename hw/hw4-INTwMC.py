################################################################################
#
#  Numerical Methods   ---   Homework
#
#  Fill in TODO to implement Monte Carlo method to estimate e^(-x^2)
#
#  This is one of the only non-deterministic methods we will consider.
#
#
#       f = function to be integrated  n = number of random samples
#       a = left endpoint   b = right endpoint
#
#           Note: make sure your implementation works even if a>b
#
#
#
#   HW question:  Experiment with different values for n (default here n=1000)
#
#       run this program 50 times for n = 10, 100, 1000, 10000
#
#       what is the mean and standard deviation of the output?
#
#   How do you think this is effected by the choice of f?  If I gave you a different
#    f, a, and b, how would you decide what n to use to have the integral accurate
#    to within +/- 0.0001?
#
#
#
#################################################################################


import datetime
import random


# TODO :: fill in the function below
def monte_carlo(f, n, a, b):


def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

def exp(x, d):
  n = 0
  f = 0.0
  r = 100.0
  while ( abs(r) ) > ( 10 ** (-d) ):
	r = x**n / fact(n)
	f += r
	n += 1
  return f


def int_this(x):
	return exp(-x**2, 12)


if __name__ == "__main__":
	n=1000

	file = open('output_hw4.txt', 'w')

	# TODO :: change my name to yours
	file.write("Tony Perkins \n\n")
	file.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")

	a = random.random()*10-5
	b = random.random()*10-5
	area = monte_carlo(int_this, n, a, b)
	file.write("Integral of e^(-x^2) from " + str(round(a, 3)) + " to " + str(round(b, 3)) + " to 3 decimal places is " + str(round(area, 3)) +"\n")

	file.close()