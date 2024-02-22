import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

# Define the r values and set up x values
r_values = np.arange(0, 4, 0.01)
x=np.ones_like(r_values)*0.5 # set a array of x with the same size of r

#write a loop to run all values of r for x
for r in r_values:
    x=r_values*x*(1-x)
    plt.scatter(r_values, x, s=0.5, color='k', marker='o')
plt.xlabel(r'Constant/r')
plt.ylabel(r'Position/x')
plt.show()





