#!/usr/bin/python
#
# Tony Perkins 2012
#

from __future__ import print_function

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt   # For plotting graphs.
from matplotlib import animation
import numpy as np
import subprocess                 # For issuing commands to the OS.
import os
import sys                        # For determining the Python version.
import random
import seaborn as sns



#
# Print the version information for the machine, OS,
# Python interpreter, and matplotlib.  The version of
# Mencoder is printed when it is called.
#
print('Executing on', os.name )
print('Python version', sys.version)
print('matplotlib version', matplotlib.__version__)

'''
not_found_msg = """
The mencoder command was not found;
mencoder is used by this script to make an avi file from a set of pngs.
It is typically not installed by default on linux distros because of
legal restrictions, but it is widely available.
"""

try:
    subprocess.check_call(['mencoder'])
except subprocess.CalledProcessError:
    print("mencoder command was found")
    pass # mencoder is found, but returns non-zero exit as expected
    # This is a quick and dirty check; it leaves some spurious output
    # for the user to puzzle over.
except OSError:
    print(not_found_msg)
    sys.exit("quitting\n")
'''

#
# First, let's create some data to work with.  In this example
# we'll use a normalized Gaussian waveform whose mean and
# standard deviation both increase linearly with time.  Such a
# waveform can be thought of as a propagating system that loses
# coherence over time, as might happen to the probability
# distribution of a clock subjected to independent, identically
# distributed Gaussian noise at each time step.
#

print('Initializing data set...')   # Let the user know what's happening.

# Initialize variables needed to create and store the example data set.
numberOfTimeSteps = 100   # Number of frames we want in the movie.


#sns.set(style="whitegrid")


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
    #plt.ylabel('time = %.2f'%(t))
    #plt.xlabel('probability density function')

    plt.title('Tony Perkins', fontsize=20)

    #
    # The file name indicates how the image will be saved and the
    # order it will appear in the movie.  If you actually wanted each
    # graph to be displayed on the screen, you would include commands
    # such as show() and draw() here.  See the matplotlib
    # documentation for details.  In this case, we are saving the
    # images directly to a file without displaying them.
    #
    filename = str('%03d' % int(t*nTimes)) + '.png'
    plt.savefig(filename, dpi=100)

    #
    # Let the user know what's happening.
    #
    print('Wrote file', filename)

    #
    # Clear the figure to make way for the next image.
    #
    plt.clf()

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
		   #'libx264',
		   'bez.avi')
           #'output.avi')

#os.spawnvp(os.P_WAIT, 'mencoder', command)

print("\n\nabout to execute:\n%s\n\n" % ' '.join(command))
subprocess.check_call(command)

print("\n\n The movie was written to 'output.avi'")

print("\n\n You may want to delete *.png now.\n\n")
