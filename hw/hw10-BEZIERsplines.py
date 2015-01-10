################################################################################
#
#  	hw10
#
#	Fill in TODO to implement interactive Bezier splines
#
#
#
#################################################################################


import numpy as np
import random
from matplotlib import pyplot as plt


# TODO :: fill in the the following function to calculate the Bezier interpolating
#            spline at 't' through the 'points'
def bezier_interp(t, points):


def make_curve(points, nTimes = 1000):
	xVals = []
	yVals = []
	for t in np.linspace(0, 1, nTimes):
		x, y = bezier_interp(t, points)
		xVals.append(x)
		yVals.append(y)
	return xVals, yVals


if __name__ == "__main__":
	nPoints = 4

	xPoints = [random.random()*10  for j in range(nPoints)]
	yPoints = [random.random()*10 for j in range(nPoints)]
	points = [[xPoints[j], yPoints[j]]  for j in range(nPoints)]

	# TODO :: Change my name to yours
	plt.title('Tony Perkins')
	xVals, yVals = make_curve(points, nTimes=1000)
	plt.plot(xVals, yVals)

	plt.plot(xPoints, yPoints, "ro")
	for nr in range(len(points)):
		plt.text(points[nr][0], points[nr][1], nr)

	plt.show()
    plt.savefig("hw10_bezier.png")

