#import everything 
import math
import numpy as np
import matplotlib.pyplot as plt

#set the latex font
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

#set the constants
g = 9.81 
l = 0.1 

#define the differential equations
def f(r,t): 
    theta = r[0] #assign the first term inside r to be theta
    omega = r[1] # assign the second term in r to be omega
    ftheta = omega # the division of a second order differential equation to a first-order one
    fomega = -(g/l)*math.sin(theta) # the second first order differential equation in the division
    return np.array([ftheta,fomega] ,float) 

#set the time steps
a = 0.0
b = 100.0
N = 3000 #suppose we use 3000 data points
h = (b-a)/N


tpoints = np.arange(a,b,h) #form an array of time
#initial empty arrays for theta and omega
theta_values = [] 
omega_values = []


r = np.array([179.0,0.0],float)#initial values to start the differentiation
for t in tpoints: #set up a loop 
    theta_values.append(r[0]) #each time we get a new theta/omega, we add it to the array
    omega_values.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6 #we use the fourth-order Runge-Kutta method as shown in the book
plt.plot(tpoints,theta_values) #make a plot
plt.xlabel(r"t/s")
plt.title(r"Angle $\theta$ of displacement")
plt.ylabel(r"$\theta$/degree")
plt.show()

