import numpy as np
from random import randint, randrange, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N=3
k=1
steps=200000
Temp=np.linspace(0.2,4.0,88)
x = [1,-1]
spin = [[x[randint(0,1)] for i in range(N)] for j in range(N)]
print(spin)


def total_energy(config):
    s1=0
    for j in range(N):
        for i in range(N-1):
            s1+=config[j][i]*config[j][i+1]


    s2=0
    for j in range(N):
        for i in range(N-1):
            s2+=config[i][j]*config[i+1][j]
            

    return(-(s1+s2))

def runmcmcmc(config):
    for h in range(steps):
        i, j = randrange(N), randrange(N)
        current_spin = config[i][j]
        proposed_spin = current_spin*(-1)
        copy=np.copy(config)
        config[i][j] = proposed_spin
        delta_E = total_energy(config)-total_energy(copy)

        if delta_E > 0 and random() >= np.exp(-delta_E / (k * T)):
            config[i][j] = current_spin
    return(config)

M=[]
for i in range(len(Temp)):
    T=Temp[i]     
    m=np.sum(runmcmcmc(spin))
    M.append(m)

plt.plot(Temp,np.abs(M))
plt.show()