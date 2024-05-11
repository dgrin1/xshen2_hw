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
        s1+=config[j][N-1]*config[j][-N]


    s2=0
    for j in range(N):
        for i in range(N-1):
            s2+=config[i][j]*config[i+1][j]
        s2+=spin[N-1][j]*spin[-N][j]
            

    return(-(s1+s2))

def calcEnergy(config, N):
    """ Energy of a given configuration """
    energy = 0
    for i in range(N):
        for j in range(N):
            S = config[i][j]
            nb = config[(i+1)%N] [j] + config[i] [(j+1)%N] + \
                 config[(i-1)%N] [j] + config[i] [(j-1)%N]
            energy += -S * nb
    return energy / 2.

print(total_energy(spin),calcEnergy(spin,N))

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

# M=[]
# for i in range(len(Temp)):
#     T=Temp[i]     
#     m=np.sum(runmcmcmc(spin))
#     m1=m/(steps*N*N)
#     M.append(m1)

# plt.plot(Temp,np.abs(M),'.')
# plt.show()