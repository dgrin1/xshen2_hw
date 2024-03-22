from math import exp
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
#part a
#Set a value for x
# Initially I chose x=1, then I got a converging point around 0.7968121300200202
# Then I changed x to 0.7968121 for higher accuracy
x = 0.7968121
c = 2 # Set value for c
# Start a loop to calculate new x
for k in range(100):
    x = 1 - exp ( - c * x)

# This is another converging point.
# Only when the initial point is super close to zero. The second answer will appear
x1 = 10 ** -17
c = 2
for k in range(100):
    x1 = 1 - exp ( - c * x1)

print(x,x1)

#part b
# Given a set of numbers for c, we create an array with the same size but every entry equal to 1
c = np.arange(0.,3.01,0.01)
x = np.ones_like(c)

#  Set two loops
for i in range(len(x)): # For every x in the array
    for k in range(1000): # For 1000 steps calculations
        x[i] = 1 - exp ( - c[i] * x[i])

# Make the plot
plt.plot(c,x)
plt.xlabel(r'c')
plt.ylabel(r'x')
plt.title(r'Relaxation Method for $x=1-e^{-cx}$')
plt.show()


