# Xiyue Shen
import numpy as np
from random import randint, randrange, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

N=20
k=1
steps=10000
Temp=np.arange(0.2,1.6,0.1) #set up an array of temperature

spin=np.zeros((N,N)) # the initial state

def energy(config):
    s1=0
    for j in range(N):
        for i in range(N-1):
            s1+=np.cos(config[j][i]-config[j][i+1])


    s2=0
    for j in range(N):
        for i in range(N-1):
            s2+=np.cos(config[i][j]-config[i+1][j])
            

    return(-(s1+s2))

def runmcmcmc(config):
    for h in range(steps):
        i, j = randrange(N), randrange(N)
        current_angle = config[i][j]
        proposed_angle = np.random.uniform(0, 2*np.pi)
        copy=np.copy(config)
        config[i][j] = proposed_angle
        delta_E = energy(config) - energy(copy)

        if delta_E > 0 and random() >= np.exp(-delta_E / (k * T)):
            config[i][j] = current_angle  
    return(config)

T=0.2
print(energy(runmcmcmc(spin)))

Energy=[]
for i in range(len(Temp)):
    T=Temp[i]     
    E=energy(runmcmcmc(spin))
    Energy.append(E)


plt.plot(Temp,Energy)
plt.xlabel(r'Temperature')
plt.ylabel(r'Energy')
plt.title(r'Energy of $20\times20$ Lattice model with varying temperature')
plt.show()

