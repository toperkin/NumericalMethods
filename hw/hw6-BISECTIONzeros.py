################################################################################
#
#  NUMERICAL METHODS - HOMEWORK - ZEROS BY BISECTION
#
#  Fill in TODO to implement the BISECTION method to find the zeros of f
#
#
#
#################################################################################


import datetime


# TODO: fill in the function below
def bisection(f, gminus, gplus, error):


def f(x):
	return x**3-x-2


if __name__ == "__main__":
	d = 5
	error = 10**(-d)
	gminus = 1.4
	gplus  = 2

	file = open('output_hw6.txt', 'w')

	# TODO :: change my name to yours
	file.write("Tony Perkins \n\n")
	file.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")

	zero = bisection(f, gminus, gplus, error)
	file.write("The zero is " + str(round(zero, d)) +"\n")

	file.close()