
#!/usr/bin/python
#
# Tony Perkins 2014
#



from __future__ import print_function

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import subprocess                 # For issuing commands to the OS.
import os
import sys                        # For determining the Python version.
import random
import sympy
from sympy.abc import x, y

import seaborn as sns
#sns.set(style="whitegrid")

'''
from matplotlib import mlab
import numpy as np
import datetime
import random
from scipy.misc import comb
'''

print('Executing on', os.name )
print('Python version', sys.version)
print('matplotlib version', matplotlib.__version__)


def perceptron_training_adjust(w0, w1, w2, redfish, bluefish, eta, n):
  if n%2==0:
    p = redfish[n%len(redfish)]
    a = curve(w0, w1, w2, p[0], p[1])
    if a>0:
      o = 1
    else:
      o = -1
    w0 += eta*(1-o)
    w1 += eta*(1-o)*p[0]
    w2 += eta*(1-o)*p[1]
  else:
    p = bluefish[n%len(bluefish)]
    a = curve(w0, w1, w2, p[0], p[1])
    if a>0:
      o = 1
    else:
      o = -1
    w0 += eta*(-1-o)
    w1 += eta*(-1-o)*p[0]
    w2 += eta*(-1-o)*p[1]

  return w0, w1, w2

def curve(w0, w1, w2, x, y):
  return w0+w1*x+w2*y

def make_curve(w0, w1, w2, xmin, xmax, nTimes = 1000):
	xvals = []
	yvals = []
	for t in np.linspace(0, 1, nTimes):
		x = xmin + (xmax - xmin)*t
		y =  -(w0+w1*x)/w2
		xvals.append(x)
		yvals.append(y)
	return xvals, yvals


nPoints = 50

    #xpoints = [j  for j in range(nPoints)]
xpoints = [random.random()*20-10  for j in range(nPoints)]
ypoints = [random.random()*19-9.5 for j in range(nPoints)]

redfish = []
bluefish = []
for i in range(nPoints):
    if (ypoints[i] > (-1.2*xpoints[i]+2)):
        redfish.append([xpoints[i], ypoints[i]+.25])
    else:
        bluefish.append([xpoints[i], ypoints[i]-.25])

eta = 0.1
w0 = 2
w1 = 1
w2 = 0

#redfish = [[0, 4], [4, 2], [6,3], [8,4], [-9,9]]
redfish_x = []
redfish_y = []
for p in redfish:
    redfish_x.append(p[0])
    redfish_y.append(p[1])

#bluefish = [[-2, 4], [1, 2], [-4,0], [-8,3]]
bluefish_x = []
bluefish_y = []
for p in bluefish:
    bluefish_x.append(p[0])
    bluefish_y.append(p[1])

#xmin = min(min(redfish_x), min(bluefish_x))
#xmax = max(max(redfish_x), max(bluefish_x))



print('Initializing data set...')   # Let the user know what's happening.

numberOfTimeSteps = 400   # Number of frames we want in the movie.
repeat = numberOfTimeSteps

for t in np.linspace(0, 1, repeat):

    #### Set up the figure
    fig, ax = plt.subplots(figsize=(5, 5))

    #ax.axes.xaxis.set_visible(False)
    #ax.axes.yaxis.set_visible(False)
    plt.title('Tony Perkins', fontsize=20)

    ############### background ################
    xlim = ylim = (-10, 10)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.scatter(redfish_x, redfish_y , s=50.0, alpha=0.5, c='r')
    plt.scatter(bluefish_x, bluefish_y , s=50.0, alpha=0.5, c='b')



    ############## perceptron ############
    n = int(t*repeat)
    w0, w1, w2 = perceptron_training_adjust(w0, w1, w2, redfish, bluefish, eta, 3*n)
    w0, w1, w2 = perceptron_training_adjust(w0, w1, w2, redfish, bluefish, eta, 3*n+1)
    w0, w1, w2 = perceptron_training_adjust(w0, w1, w2, redfish, bluefish, eta, 3*n+2)

    xvals, yvals = make_curve(w0, w1, w2, xlim[0], xlim[1], nTimes = 1000)
    plt.plot( xvals, yvals, c='g' )

    filename = str('%03d' % int(t*repeat)) + '.png'
    plt.savefig(filename, dpi=100)

    print('Wrote file', filename)

    plt.clf()


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
           'perceptron.avi')


print("\n\nabout to execute:\n%s\n\n" % ' '.join(command))
subprocess.check_call(command)

print("\n\n The movie was written to 'perceptron.avi'")

print("\n\n You may want to delete *.png now.\n\n")
