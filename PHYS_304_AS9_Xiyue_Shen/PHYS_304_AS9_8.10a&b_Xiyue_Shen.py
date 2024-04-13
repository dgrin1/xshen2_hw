#Xiyue Shen
#import all necessary libraries
import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
plt.rcParams.update({'font.size': 22})

#set the constant
G = 6.6743e-11
m = 1.98892e30

#define the differential equations
def f(r,t): 
    x = r[0]
    v_x = r[1] 
    y = r[2]
    v_y = r[3]
    fx = v_x 
    fv_x = -G*m*x/(x**2+y**2)**(3/2) 
    fy=v_y
    fv_y= -G*m*y/(x**2+y**2)**(3/2) 
    return np.array([fx,fv_x,fy,fv_y] ,float) 

#set the time steps
a = 0.0
# b = 1e10
# N = 1e6
b=1e10
N=1e6
h = (b-a)/N

tpoints = np.arange(a,b,h)
x_values = []
v_x_values = []
y_values = []
v_y_values = []

#Set the initial conditions and appply the fourth-order Runge-Kutta method
r = np.array([4e12,0,0,500],float)
for t in tpoints:
    x_values.append(r[0])
    v_x_values.append(r[1])
    y_values.append(r[2])
    v_y_values.append(r[3])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


plt.suptitle(r"Trajectory of the comet")
plt.subplot(1, 2, 1)
plt.plot(tpoints,x_values, label=r'x trajectory')
plt.plot(tpoints,y_values,label=r'y trajectory')
plt.xlabel(r'time/s')
plt.ylabel(r'Trajectory/m')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values,y_values,'ro')
plt.xlabel(r"x trajectory")
plt.ylabel(r"y trajectory")

plt.show()



