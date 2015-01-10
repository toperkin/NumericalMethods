import numpy as np
from scipy.misc import comb
from matplotlib import pyplot as plt


def bernstein_poly(i, n, t):
    """
    The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * (t**(n-i)) * (1 - t)**i


def bezier_curve(points, nTimes=1000):
    """
    Given a set of control points, return the
    bezier curve defined by the control points.
    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)])

    xVals = np.dot(xPoints, polynomial_array)
    yVals = np.dot(yPoints, polynomial_array)

    return xVals, yVals

if __name__ == "__main__":
    nPoints = 4
    points = np.random.rand(nPoints, 2)*200
    xPoints = [p[0] for p in points]
    yPoints = [p[1] for p in points]

    xVals, yVals = bezier_curve(points, nTimes=1000)

    # TODO : Change my name to yours
    plt.title('Tony Perkins')
    plt.plot(xVals, yVals)
    plt.plot(xPoints, yPoints, "ro")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)

    plt.show()