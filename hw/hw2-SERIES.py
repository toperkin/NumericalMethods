################################################################################
#
#  	hw2.py
#
#	Fill in TODO to implement taylor expansions on exp, cos and arcsin
#
#       x = independent var.    d = number of digits precision required.
#
#################################################################################


import datetime
import random


def fact(n):
	if (n == 0):
		return 1
	else:
		return n * fact(n-1)


# TODO :: fill in the function below
def exp(x, d):


# TODO :: fill in the function below
def cos(x, d):


# TODO :: fill in the function below
def arcsin(x, d):


# TODO :: fill in the function below
def pi(d):


if __name__ == "__main__":
	f = open('output_hw2.txt', 'w')
	
	# TODO :: change my name to yours
	f.write("Tony Perkins \n\n")
	f.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")
	
	x = random.random()*2-1
	d = random.randint(1, 6)
	
	f.write( "Exponential of " + str( x ) + " to " + str( d ) + " decimal places is " + str(round(exp(x,d),d)) + "\n")
	f.write( "Cosine of " + str( x ) + " to " + str( d ) + " decimal places is " + str(round(cos(x,d),d)) + "\n")
	f.write( "Arcsine of " + str( x ) + " to " + str( d ) + " decimal places is " + str(round(arcsin(x,d),d)) + "\n")
	f.write( "Pi to " + str( d ) + " decimal places is " + str(round(pi(d),d)) + "\n")
	f.close()