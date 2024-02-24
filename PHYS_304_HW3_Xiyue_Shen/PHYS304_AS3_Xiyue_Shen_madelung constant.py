import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

import numpy as np


#N = np.arange(0.,100.)  #Rnage of j,k,l number

# # Calculate the Madelung constant
def madelung(N):
    M = 0
    for j in range(-N, N+1):
        for k in range(-N, N+1):
            for l in range(-N, N+1):
                if j == k == l == 0:
                    continue  # Skip the term where j, k, and l are all zero to avoid division by zero
                M += ((-1)**(j+k+l)) / np.sqrt(j**2 + k**2 + l**2)

    return M

N=np.arange(1,100)
plt.plot(N,np.vectorize(madelung)(N))
plt.xlabel(r"N")
plt.ylabel(r'Madelung Constant')
plt.show()

#sech madelung constant
def sech(x):
    return 2 / (np.exp(x) + np.exp(-x))

def madelung_sech(N):
    M = 0
    for m in range(1, N, 2):
        for n in range(1, N, 2):
            M += sech(np.pi/2 * np.sqrt(m**2 + n**2))**2
    return 12 * np.pi * M

N = range(1, 10)  
M_sech = [madelung_sech(N) for N in N]

plt.figure()
plt.plot(N, M_sech, label='Analytical Approximation', marker='x')
plt.xlabel(r"N")
plt.ylabel(r'Madelung Constant')
plt.show()

#My own madelung constant
def csch(x):
    return 1/(np.sinh(x))
print("finished")
def madelung_csch(N):
    M=0
    for u in range(-N,N):
        for v in range(-N,N):
            if u == 0 and v == 0:  # Skip the term where u and v are both zero
                continue
            M+=(-1)**v*csch(np.pi*((u**2+v**2)**(1/2)))/((u**2+v**2)**(1/2))
    return np.abs(-np.pi/2+3*M)
print("finished1")
N = range(1, 10)  
M_csch = [madelung_csch(N) for N in N]
print("finished2")
plt.figure()
plt.plot(N, M_csch, label='Analytical Approximation', marker='x')
plt.xlabel(r"N")
plt.ylabel(r'Madelung Constant')
plt.show()
print('finished3')


