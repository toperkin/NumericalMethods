################################################################################
#
#    hw3.py
#
#  Fill in TODO to implement simpson's rule to estimate e^(-x^2)
#
#       x = independent var.    d = number of digits precision required.
#
#################################################################################

import datetime
import random


# TODO: fill in this function
def simpson(f, n, a, b):


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
    return exp(-x**2, 6)


if __name__ == "__main__":
    file = open('output_hw3.txt', 'w')

    # TODO :: change my name to yours
    file.write("Tony Perkins \n\n")
    file.write( "Current date and time: " + str(datetime.datetime.now())+ "\n\n")

    a = random.random()*10-5
    b = random.random()*10-5
    area = simpson(int_this, 100, a, b)
    file.write("Integral of e^(-x^2) from " + str(round(a, 3)) + " to " + str(round(b, 3)) + " to 3 decimal places is " + str(round(area, 3)) +"\n")

    file.close()