import math
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

#ASSIGN the constants
alpha=1
beta=gamma=0.5
delta=2

#define the differential equations
def f(r,t): 
    rabbit = r[0]
    fox = r[1] 
    frabbit = alpha*rabbit-beta*rabbit*fox
    ffox = gamma*rabbit*fox-delta*fox
    return np.array([frabbit,ffox] ,float) 

#set the time space
a = 0.0
b = 30.0
N = 3000
h = (b-a)/N

#create empty array to extract values for later parts
tpoints = np.arange(a,b,h)
rabbit_values = []
fox_values = []

# set the initial conditions. Here we have the fox and rabbit both at 2000 population.
#The values are scaled down by 1000
r = np.array([2,2],float)
for t in tpoints:
    rabbit_values.append(r[0])
    fox_values.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
#make the plot
plt.plot(tpoints,rabbit_values,label='Rabbit population')
plt.plot(tpoints,fox_values,label='Fox population')
plt.ylabel(r'Population($\times$$10^3$)')
plt.legend()
plt.xlabel(r"t/day")
plt.title(r'Predator-Prey model using the Lotka-Volterra equations')
plt.show()