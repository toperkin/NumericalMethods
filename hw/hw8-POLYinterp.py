################################################################################
#
#  	hw8
#
#	Fill in TODO to implement Polynomial Interpolation (Curve-fitting) using Lagrange Polynomial
#
#       
#
#################################################################################


import numpy as np
import random
from matplotlib import pyplot as plt


# TODO :: fill in the function below to calculate the
#  interpolating polynomial at => x <= going through the => points <=
def interpolate(x, points):


def draw_curve(points, nTimes=1000):

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    xVals = np.linspace(0.0, nPoints-1, nTimes)
	
    yVals = [interpolate(x, points) for x in xVals]
	
    return xVals, yVals


if __name__ == "__main__":
    nPoints = 10  

    xPoints = [j for j in range(nPoints)]
    yPoints = [random.randint(0,10) for j in range(nPoints)]
    points = [[xPoints[j], yPoints[j]]  for j in range(nPoints)]
    xVals, yVals = draw_curve(points, nTimes=1000)

    # TODO :: Change my name to yours
    plt.title('Tony Perkins')
    plt.plot(xVals, yVals)
    plt.plot(xPoints, yPoints, "ro")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)

    plt.show()
    plt.savefig("hw8_poly.png")
