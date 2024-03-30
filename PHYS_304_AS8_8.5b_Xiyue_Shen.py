# Import all libraries
import math
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

# Set constants
g = 9.81 
l = 0.1 
C=2
Omega_range=np.linspace(5,30,100) #Instead of giving Omega a single value, I put a range of values here.
#Later I'll set up a loop to find how the amplitude of the oscialltion within this range of Omega

#Define the differential equations
def f(r,t): 
    theta = r[0]
    omega = r[1] 
    ftheta = omega 
    fomega = -(g/l)*math.sin(theta) + C*math.cos(theta)*math.sin(Omega*t)
    return np.array([ftheta,fomega] ,float) 

#set time steps
a = 0.0
b = 100.0
N = 3000
h = (b-a)/N


#set an empty array
max_theta_value=[]

#Here's the loop for every Omega driving frequency
for Omega in Omega_range:
    tpoints = np.arange(a,b,h)
    theta_values = []
    omega_values = []
    r = np.array([0.0,0.0],float)
    for t in tpoints: #inside the Omega, we set another loop to run the fourth-order Runge-Kutta method
        theta_values.append(r[0])
        omega_values.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    max_theta=max(theta_values) #A adjustment is that we extract the max value from each run and assign it to the max array
    max_theta_value.append(max_theta)

# Find the exact value of max displacement with the corresponding driving frequency 
max_theta_index = np.argmax(max_theta_value)
print(Omega_range[max_theta_index],max(max_theta_value))

#Make a plot
plt.plot(Omega_range,max_theta_value)
plt.xlabel(r"$\Omega$/$s^{-1}$")
plt.title(r"Amplitude of angle $\theta$ versus the driving frequency")
plt.ylabel(r"$\theta$/degree")
plt.show()

# Part II
# Set constants
g = 9.81 
l = 0.1 
C=2
Omega=9.545454545454547#Instead of giving Omega a single value, I put a range of values here.
#Later I'll set up a loop to find how the amplitude of the oscialltion within this range of Omega

#Define the differential equations
def f(r,t): 
    theta = r[0]
    omega = r[1] 
    ftheta = omega 
    fomega = -(g/l)*math.sin(theta) + C*math.cos(theta)*math.sin(Omega*t)
    return np.array([ftheta,fomega] ,float) 

#set time steps
a = 0.0
b = 100.0
N = 3000
h = (b-a)/N



#Here's the loop for every Omega driving frequency
tpoints1 = np.arange(a,b,h)
theta_values1 = []
omega_values1 = []
r = np.array([0.0,0.0],float)
for t in tpoints1: #inside the Omega, we set another loop to run the fourth-order Runge-Kutta method
    theta_values1.append(r[0])
    omega_values1.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints1,theta_values1)
plt.xlabel(r"t/s")
plt.title(r"Angle $\theta$ of displacement with a sinusoidal driving force and $\Omega=9.54s^{-1}$")
plt.ylabel(r"$\theta$/degree")
plt.show()
