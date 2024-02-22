import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

import numpy as np


#N = np.arange(0.,100.)  #Rnage of j,k,l number

# Calculate the Madelung constant
def madelung(N):
    M = 0
    for j in range(-N, N+1):
        for k in range(-N, N+1):
            for l in range(-N, N+1):
                if j == k == l == 0:
                    continue  # Skip the term where j, k, and l are all zero to avoid division by zero
                M += ((-1)**(j+k+l)) / np.sqrt(j**2 + k**2 + l**2)

    return M

#print("Madelung constant for N =", N, "is:", M) #print out the value for madelung constant given a state number
N=np.arange(1,100)
plt.plot(N,np.vectorize(madelung)(N))
plt.show()