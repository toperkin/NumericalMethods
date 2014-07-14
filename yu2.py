
#!/usr/bin/python
#
# Tony Perkins 2014
#


'''
  Based off http://tonysyu.github.io/animating-particles-in-a-flow.html

  We take a simpler approach to generating particles and plotting which
    directly creats an .avi file.  Mencoder required for the animation.


'''


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

from matplotlib import mlab



#
# Print the version information for the machine, OS,
# Python interpreter, and matplotlib.  The version of
# Mencoder is printed when it is called.
#
print('Executing on', os.name )
print('Python version', sys.version)
print('matplotlib version', matplotlib.__version__)

def cylinder_stream_function(U=1, R=1):
    r = sympy.sqrt(x**2 + y**2)
    theta = sympy.atan2(y, x)
    return U * (r - R**2 / r) * sympy.sin(theta)

def velocity_field(psi):
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    return u, v


def plot_streamlines(ax, u, v, xlim=(-1, 1), ylim=(-1, 1)):
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='cornflowerblue')

print('Initializing data set...')   # Let the user know what's happening.

numberOfTimeSteps = 100   # Number of frames we want in the movie.

nTimes = 200

dt = 0.05

nParticles = 2
particleRADIUS = 0.07
particles = [ [-3, random.random()*6.0-3] for n in range(nParticles)]


for t in np.linspace(0, 1, nTimes):

    #### Set up the figure
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.title('Tony Perkins', fontsize=20)

    ############### background ################
    psi = cylinder_stream_function()
    u, v = velocity_field(psi)

    xlim = ylim = (-3, 3)
    plot_streamlines(ax, u, v, xlim, ylim)

    c = plt.Circle((0, 0), radius=1, facecolor='none')
    ax.add_patch(c)

    ############## draw particles ############

    for p in particles:
        ## draw it
        if ( (p[0]<-3) or (p[0]>3) or (p[1]<-3) or (p[1]>3) ):
            particles.remove(p)
            continue
        c = plt.Circle((p[0], p[1]), radius=particleRADIUS, facecolor='red')
        ax.add_patch(c)

        ## update position
        vx =  dt*u(p[0], p[1])
        vy =  dt*v(p[0], p[1])
        p[0]+=vx
        p[1]+=vy


    #add some new particles
    for n in range(random.randint(0, nParticles)):
        particles.append([-3, random.random()*6.0-3])

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
           'particle.avi')
           #'output.avi')

#os.spawnvp(os.P_WAIT, 'mencoder', command)

print("\n\nabout to execute:\n%s\n\n" % ' '.join(command))
subprocess.check_call(command)

print("\n\n The movie was written to 'particle.avi'")

print("\n\n You may want to delete *.png now.\n\n")
