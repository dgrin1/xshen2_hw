# Xiyue Shen
import numpy as np
from random import randint, randrange, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

# part a
def total_energy(N, config):
    s1=0
    for j in range(N):
        for i in range(N-1):
            s1+=config[j][i]*config[j][i+1]


    s2=0
    for j in range(N):
        for i in range(N-1):
            s2+=config[i][j]*config[i+1][j]
            

    return(-(s1+s2))

x = [1,-1]
N=20
my_matrix = [[x[randint(0,1)] for i in range(N)] for j in range(N)]
print(my_matrix)
print(total_energy(N,my_matrix)) 
# The energy here is summation of all sisj without J yet.
# part a doesn;t assign a J value. But, it's not hard to do this

#part b

J=1
T=5
k=1

def flip_local_energy(N,config):
    i=randrange(N) #generate a random number form 0 to N-1
    j=randrange(N)
    s=config[i][j]
    delta_E=0
    if i>0:
        delta_E -= config[i][j] * config [i-1][j]
    if i<N-1:
        delta_E -= config[i][j] * config [i+1][j]
    if j>0:
        delta_E -= config[i][j] * config [i][j-1]
    if j<N-1:
        delta_E -= config[i][j] * config [i][j+1]

    energy=-2*delta_E*J
    
    if energy<0:
        config[i][j] *= -1
    
    if energy>=0:
        if random()<np.exp(-energy/(k*T)):
            config[i][j] *= -1
        else:
            config[i][j] = s
    
    return(energy)


#part c

def magnetization(config, steps):
    M=[]
    for h in range(steps):
        i=randrange(N) #generate a random number form 0 to N-1
        j=randrange(N)
        s=config[i][j]
        delta_E=0
        if i>0:
            delta_E -= config[i][j] * config [i-1][j]
        if i<N-1:
            delta_E -= config[i][j] * config [i+1][j]
        if j>0:
            delta_E -= config[i][j] * config [i][j-1]
        if j<N-1:
            delta_E -= config[i][j] * config [i][j+1]

        energy=-2*delta_E*J

        if energy<0:
            config[i][j] *= -1
        
        if energy>=0:
            if random()<np.exp(-energy/(k*T)):
                config[i][j] *= -1
            else:
                config[i][j] = s
        
        m=0
        m+=np.sum(config)
        M.append(m)
    return(M)

steps=1000000

plt.plot(magnetization(my_matrix, steps),label='T=1')
plt.legend()
plt.xlabel(r'Steps')
plt.ylabel(r'Magnetization/$Am^{-1}$')
plt.title(r'Magnetization of 20 $\times$ 20 Ising Model')
plt.show()

#part e
def animation(frame, img, config):
    """Perform one step of the Ising model update."""
    for _ in range(N**2):  # Update N**2 spins per frame
        i = randrange(N)
        j = randrange(N)
        delta_E = 0
        if i > 0:
            delta_E -= config[i][j] * config[i-1][j]
        if i < N-1:
            delta_E -= config[i][j] * config[i+1][j]
        if j > 0:
            delta_E -= config[i][j] * config[i][j-1]
        if j < N-1:
            delta_E -= config[i][j] * config[i][j+1]

        energy = - 2 * delta_E * J

        if energy < 0 or random() < np.exp(-energy/(k*T)):
            config[i][j] *= -1

    img.set_data(config)
    return (img,)

#Setup the plot
fig, ax = plt.subplots()
img = ax.imshow(my_matrix)
ax.set_title(r"2D Ising Model at T=3")
plt.colorbar(img, ax=ax)
animation = FuncAnimation(fig, animation, fargs=(img, my_matrix), frames=2000000, interval=50, blit=True)
plt.show()




    