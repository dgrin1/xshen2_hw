import numpy as np

import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

# Set all constants
hbar = 1.0545718e-34  # Planck constant / 2*pi
eV = 1.602e-19  # Electron volt in Joules
M = 9.1094e-31  # Electron mass
L = 5e-10  # Quantum wall width
a = 10 * eV  # Given a in Joules

#part b
# Define a way to compute H_mn 
def H_mn(m, n, L, a):
    if m != n:
        if (m % 2 == 0 and n % 2 == 0) or (m % 2 == 1 and n % 2 == 1):
            return 0
        else:
            return -8*a / (np.pi) ** 2 * (m * n) / (m ** 2 - n ** 2) ** 2
    else:
        return hbar **2 /(2 * M) * (np.pi * n / L)**2 + a / 2

#part c
# Set up an empty matrix
size = 10  # Number of columns and rows of the matrix
H_matrix = np.zeros((size, size))

# Fill the matrix with numerical values
for i in range(size):
    for j in range(size):
        H_matrix[i, j] = H_mn(i+1, j+1, L, a)  # i+1 and j+1 to avoid zero 

# Use np.linalg to find the eigenvalues and eignvectors
eigenvalues, eigenvectors = np.linalg.eigh(H_matrix)
energies = eigenvalues / eV  # Convert to eV 

print("The energy levels for the first 10 states are (m,n=10):", energies)

#part d
# Set up an empty matrix
# Use 100 * 100 array matrix for higher accuracy
size = 100  # Number of columns and rows of the matrix
H_matrix = np.zeros((size, size))

# Fill the matrix with numerical values
for i in range(size):
    for j in range(size):
        H_matrix[i, j] = H_mn(i+1, j+1, L, a)  # i+1 and j+1 to avoid zero 

# Use np.linalg to find the eigenvalues and eignvectors
eigenvalues, eigenvectors = np.linalg.eigh(H_matrix)
energies = eigenvalues / eV  # Convert to eV 

print("The energy levels for the first 10 states are (m,n=100):", energies[:10])

#part e
#The wavefunctions are the combinations of eigenstates of the matrix

# Define a set of values for x
x=np.linspace(0,L,1000)

# Set up the first three wavfunction
psi1=np.zeros_like(x)
psi2=np.zeros_like(x)
psi3=np.zeros_like(x)

# Set up a loop to fill in values
# For nth wavefunction, we only want the nth row which represents the coeffcient of eigenstate in that wavefucntion
for n in range(size):
    psi1 += eigenvectors[n][0] * np.sin(np.pi * n * x / L)
    psi2 += eigenvectors[n][1] * np.sin(np.pi * n * x / L)
    psi3 += eigenvectors[n][2] * np.sin(np.pi * n * x / L)

# Make the plot
plt.plot(x,psi1 , label=r'The Ground Satet')
plt.plot(x,psi2 , label=r'The First Excited Satet')
plt.plot(x,psi3 , label=r'The Second Excited Satet')
plt.title(r"Probability Density in an Asymmetric Quantum Well")
plt.xlabel(r'Position')
plt.ylabel(r'Probability Density $|\psi(x)|^2$')
plt.legend()
plt.show()


