'''
  Based off http://tonysyu.github.io/plotting-streamlines-with-matplotlib-and-sympy.html





'''



import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy.abc import x, y



def corner_stream_function(n=1, A=1):
  r = sympy.sqrt(x**2 + y**2)
  theta = sympy.atan2(y, x)
  return A * r**n * sympy.sin(n * theta)



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

### fig 1
psi = cylinder_stream_function()
u, v = velocity_field(psi)

xlim = ylim = (-3, 3)
fig1, ax1 = plt.subplots(figsize=(5, 5))
plot_streamlines(ax1, u, v, xlim, ylim)

c = plt.Circle((0, 0), radius=1, facecolor='none')
ax1.add_patch(c)

ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)

fig1.savefig("yu1-1.png")


#format_axes(ax)  #Not working at the moment

### fig 2
rho = corner_stream_function(n=2)
u2, v2 = velocity_field(rho)

xlim =(-3, 3)
ylim = (0, 3)
fig2, ax2 = plt.subplots(figsize=(5, 5))
plot_streamlines(ax2, u2, v2, xlim, ylim)

ax2.plot([0, 0], [0, 3], 'k-', lw=1)

fig2.savefig("yu1-2.png")



### fig 3
eta = corner_stream_function(n=3/2)
u3, v3 = velocity_field(eta)


xlim =(-3, 3)
ylim = (0, 3)

fig3, ax3 = plt.subplots(figsize=(5, 5))
plot_streamlines(ax3, u3, v3, xlim, ylim)

ax3.plot([0, -1.7], [0, 3], 'k-', lw=1)

fig3.savefig("yu1-3.png")



### fig 4
eta = corner_stream_function(n=-2)
u4, v4 = velocity_field(eta)


xlim =(-3, 3)
ylim = (-3, 3)

fig4, ax4 = plt.subplots(figsize=(5, 5))
plot_streamlines(ax4, u4, v4, xlim, ylim)

ax4.axes.xaxis.set_visible(False)
ax4.axes.yaxis.set_visible(False)

fig4.savefig("yu1-4.png")

plt.show()
