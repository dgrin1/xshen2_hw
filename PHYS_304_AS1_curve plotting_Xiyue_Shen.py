
#Import all packages
from math import pi,cos,sin
from pylab import plot,xlabel,ylabel,show,title
from numpy import linspace, sin,cos,exp
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

#part a
theta=linspace(0,2*pi,100) #assign a evenly distributed angle numbers
x=2*cos(theta)+cos(2*theta) #set x 
y=2*sin(theta)-sin(2*theta) #set y
plot(x,y)
title(r'Deltoid curve')
xlabel(r'$2\cos(\theta)+\cos(2\theta)$')
ylabel(r'$2\sin(\theta)-\sin(2\theta)$')
show()

#part b
phi=linspace(0,10*pi,100) #to aviod confusion with part a, I use phi instead of theta
r=phi**2
xb=r*cos(phi)
yb=r*sin(phi)
plot(xb,yb)
title(r'Galilean spiral')
xlabel(r'$\phi^2\cos(\phi)$')
ylabel(r'$\phi^2\sin(\phi)$')
show()

#Interesting thing is that need to close the first plot and then the second
#plot will show up

#part c
alpha=linspace(0,10*pi,100)
rc=exp(cos(alpha))-2*cos(4*alpha)+(sin(alpha/12))**5
xc=rc*cos(alpha)
yc=rc*sin(alpha)
plot(xc,yc)
title(r'Fey’s function')
xlabel(r'$(e^{\cos(\alpha)}-2\cos(4\alpha)+\sin^5\left(\frac{\alpha}{12}\right))\cos(\alpha)$')
ylabel(r'$(e^{\cos(\alpha)}-2\cos(4\alpha)+\sin^5\left(\frac{\alpha}{12}\right))\sin(\alpha)$')
show()
