################################################################################
#
#  	hw9
#
#	Fill in TODO to implement Catmull-Rom splines
#
#       
#
#################################################################################


import numpy as np
import random
from matplotlib import pyplot as plt


# TODO :: fill in the function below to calculate the
#  catmull rom spline through four consecutive points
def cr( p1, p2, p3, p4, nTimes=100 ):


if __name__ == "__main__":
	nPoints = 10

	xPoints = [j  for j in range(nPoints)]
	yPoints = [random.random()*100 for j in range(nPoints)]
	points = [[xPoints[j], yPoints[j]]  for j in range(nPoints)]

	# TODO :: Change my name to yours
	plt.title('Tony Perkins')
	for i in range(nPoints - 3):
		xVals, yVals = cr( points[0+i], points[1+i], points[2+i], points[3+i], nTimes=100)
		plt.plot(xVals, yVals)

	plt.plot(xPoints, yPoints, "ro")
	for nr in range(len(points)):
		plt.text(points[nr][0], points[nr][1], nr)

	plt.show()
    plt.savefig("hw9_cr.png")
