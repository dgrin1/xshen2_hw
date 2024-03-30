#import all necessary libraries
import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

#set the constant
g = 9.81 
l = 0.1 
C=2
Omega=5

#define the differential equations
def f(r,t): 
    theta = r[0]
    omega = r[1] 
    ftheta = omega 
    fomega = -(g/l)*math.sin(theta) + C*math.cos(theta)*math.sin(Omega*t) #the difference between here and exercise 8.4
    #is that we have an extra driving force
    return np.array([ftheta,fomega] ,float) 

#set the time steps
a = 0.0
b = 100.0
N = 3000
h = (b-a)/N

tpoints = np.arange(a,b,h)
theta_values = []
omega_values = []

#Set the initial conditions and appply the fourth-order Runge-Kutta method
r = np.array([0.0,0.0],float)
for t in tpoints:
    theta_values.append(r[0])
    omega_values.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plt.plot(tpoints,theta_values)
plt.xlabel(r"t/s")
plt.title(r"Angle $\theta$ of displacement with a sinusoidal driving force")
plt.ylabel(r"$\theta$/degree")
plt.show()


