################################################################################
#
#  NUMERICAL METHODS - HOMEWORK - FIXED POINT BY ITERATIONS
#
#  Fill in TODO to implement the method to find the fixed point of f
#
#
#
#################################################################################


import datetime


# TODO: fill in the function below
def find_fixed(f, x0, error):


def f(x):
	return x-0.01*x**3+2

if __name__ == "__main__":
	first_guess = 1.0
	file = open('output_hw5.txt', 'w')

	# TODO :: change my name to yours
	file.write("Tony Perkins \n\n")
	file.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")

	fixie = find_fixed(f, first_guess, 0.0001)
	file.write("The fixed point is " + str(round(fixie, 3)) +"\n")

	file.close()