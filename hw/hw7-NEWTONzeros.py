################################################################################
#
#  NUMERICAL METHODS - HOMEWORK - NEWTON'S METHOD TO FIND ZEROS
#
#  Fill in TODO to implement NEWTON'S method
#
#
#
#################################################################################


import datetime


#### TODO :: implement Newton's method
def newton(f, x0, error):


# TODO: steal this from two assignments back
def find_fixed(f, x0, error):


# Calculates the first derivative of 'f' at 'x'
def diff(f, x, error):
	h = error
	dfdx = (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
	return dfdx

def f(x):
	return x**3-x-2

if __name__ == "__main__":
	d = 8
	error = 10**(-d)
	x0=0.0

	file = open('output_hw7.txt', 'w')

	# TODO :: change my name to yours
	file.write("Tony Perkins \n\n")
	file.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")

	zero = newton(f, x0, error)
	file.write("The zero is " + str(round(zero, d)) +"\n")

	file.close()