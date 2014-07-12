#!/usr/bin/python
#
#   Tony Perkins 2014
#
#   Makes an animation of Bezier splines
#
#   Animation is saved as bez.avi but must be converted to .ogv to be published on the web
#
#

from __future__ import print_function

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import subprocess
import os
import sys
import random
import seaborn as sns

print('Executing on', os.name )
print('Python version', sys.version)
print('matplotlib version', matplotlib.__version__)

print('Initializing data set...')

numberOfTimeSteps = 100   # Number of frames we want in the movie.

nPoints = 5
nTimes = 200

#xpoints = [j+1  for j in range(nPoints)]
xpoints = [0.1, 7.8, 9.7, 0.4, 2.2]
ypoints = [-4.1, -8.7, 9.7, -3.1, 8.5]
#xpoints = [random.random()*10  for j in range(nPoints)]
#ypoints = [random.random()*10-5 for j in range(nPoints)]
points = [[xpoints[j], ypoints[j]]  for j in range(nPoints)]

xline4 = {}
yline4 = {}
xline3 = {}
yline3 = {}
xline2 = {}
yline2 = {}
xline1 = {}
yline1 = {}


ax = plt.axes()
time_template = 'time = %.2f'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def bezier_interp(t, inpoints, draw):
    npoints = len(inpoints)

    xpoints = np.array([p[0] for p in inpoints])
    ypoints = np.array([p[1] for p in inpoints])

    if (npoints == 4):
        xline4[t] = xpoints
        yline4[t] = ypoints

    if (npoints == 3):
        xline3[t] = xpoints
        yline3[t] = ypoints

    if (npoints == 2):
        xline2[t] = xpoints
        yline2[t] = ypoints

    if (npoints == 1):
        xline1[t] = xpoints
        yline1[t] = ypoints

    if (npoints >1):
        midpoints = [ [(1-t)*xpoints[0+i]+t*xpoints[1+i], (1-t)*ypoints[0+i]+t*ypoints[1+i]] for i in range(npoints-1) ]
        return bezier_interp(t, midpoints, draw)

    return xpoints[0], ypoints[0]

xvals = []
yvals = []
for t in np.linspace(0, 1, nTimes):
	x, y = bezier_interp(t, points, draw = True)
	xvals.append(x)
	yvals.append(y)

for t in np.linspace(0, 1, nTimes):

    plt.plot(xvals[:int(t*nTimes)], yvals[:int(t*nTimes)], linewidth=3)
    plt.plot(xpoints, ypoints, marker='o', linewidth=1)
    plt.plot(xline4[t], yline4[t], marker='o', linewidth=1)
    plt.plot(xline3[t], yline3[t], marker='o', linewidth=1)
    plt.plot(xline2[t], yline2[t], marker='o', linewidth=1)
    p1, = plt.plot(xline1[t], yline1[t], marker='o', linewidth=4)
    plt.legend([p1], ['time = %.2f'%(t)], loc=2)
    plt.axis((0,10,-10,10))
    plt.title('Tony Perkins', fontsize=20)

    filename = str('%03d' % int(t*nTimes)) + '.png'
    plt.savefig(filename, dpi=100)

    print('Wrote file', filename)

    plt.clf() #Clears the figure.  That way we get a new image each loop

#
# Now that we have graphed images of the dataset, we will stitch them
# together using Mencoder to create a movie.  Each image will become
# a single frame in the movie.
#
# We want to use Python to make what would normally be a command line
# call to Mencoder.  Specifically, the command line call we want to
# emulate is (without the initial '#'):
# mencoder mf://*.png -mf type=png:w=800:h=600:fps=25 -ovc lavc -lavcopts vcodec=mpeg4 -oac copy -o output.avi
# See the MPlayer and Mencoder documentation for details.
#

command = ('mencoder',
           'mf://*.png',
           '-mf',
           'type=png:w=800:h=600:fps=25',
           '-ovc',
           'lavc',
           '-lavcopts',
           'vcodec=mpeg4',
           '-oac',
           'copy',
           '-o',
		       'bez.avi')


print("\n\nabout to execute:\n%s\n\n" % ' '.join(command))
subprocess.check_call(command)

print("\n\n The movie was written to 'output.avi'")

print("\n\n You may want to delete *.png now.\n\n")
