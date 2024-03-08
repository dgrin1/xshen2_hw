import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

def simpson(a, b, f, N):
    if N % 2 == 1:  # Simpson's rule requires an even number of intervals
        print ("N must be an even integer.")
    h = (b - a) / N
    s = f(a) + f(b)

    # Accumulate the four-thirds terms
    for i in range(1, N, 2):
        s += 4 * f(a + i * h)
    # Accumulate the two-thirds terms
    for i in range(2, N-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3

def f(x):
	return x**3+2*x**2

up=np.arange(0,10,0.01)
low=0
solution=np.zeros_like(up)
for i in range(len(up)):
	solution[i]=simpson(low,up[i],f,100)
     
exact_solution = 0.25 * up**4 + 2/3 * up**3
error = np.abs(solution - exact_solution)

plt.figure(figsize=(10,6))
plt.subplot(1, 2, 1)
plt.plot(up,solution,label='Simpson Method')
plt.plot(up,exact_solution,label=r"$\frac{1}{4}x^4+\frac{2}{3}x^3$")
plt.title("Comparison of Simpson's Method with Exact Solution")
plt.legend()
plt.xlabel(r'Upper limit')
plt.ylabel(r'Integration Value')
plt.subplot(1, 2, 2)
plt.plot(up,error,label='Error')
plt.yscale('log')
plt.xlabel(r'Upper limit')
plt.ylabel(r'Error')
plt.title("Error in Simpson's Method")
plt.legend()
plt.show()