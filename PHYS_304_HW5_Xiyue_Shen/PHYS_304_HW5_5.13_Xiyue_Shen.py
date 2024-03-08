import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

# Define the Hermite polynomials 
def H(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * H(n-1, x) - 2 * (n-1) * H(n-2, x)

H_vector = np.vectorize(H)

# Set the range for x and calculate the wave functions for n = 0, 1, 2, 3
x = np.linspace(-4, 4, 400)

# Now you can plot the harmonic oscillator wavefunctions

for n in range(4):
    wavefunctiona = (1.0 / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi))) * np.exp(-x**2 / 2) * H_vector(n, x)
    plt.plot(x, wavefunctiona, label=f"$\psi_{{{n}}}(x)$")

plt.legend()
plt.title(r"Wavefunctions of the harmonic oscillator")
plt.xlabel(r"x")
plt.ylabel(r"$\psi_n(x)$")
plt.show()


#part b
H_vector2 = np.vectorize(H)

# Set the range for x and calculate the wave functions for n = 0, 1, 2, 3
x = np.linspace(-10, 10, 500)
plt.figure()
# Now you can plot the harmonic oscillator wavefunctions
#for n in range(30):
n=30
wavefunction = (1.0 / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi))) * np.exp(-x**2 / 2) * H_vector2(n, x)
plt.plot(x, wavefunction)

plt.legend()
plt.title(r"Wavefunctions of the harmonic oscillator with n=30")
plt.xlabel(r"x")
plt.ylabel(r"$\psi_30(x)$")
plt.show()

#part c
from numpy import ones,copy,cos,tan,pi,linspace
import math as math

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w
def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def wavefunction(n,x):
    return (1.0 / np.sqrt(2**n * math.factorial(int(n)) * np.sqrt(np.pi))) * np.exp(-x**2 / 2) * H_vector(n, x)

def wavefunctionc(z,n):
    return (np.tan(z)**2 / np.cos(z)**2) * wavefunction(n,np.tan(z))**2
    # return z**2/(1-z**2)**2*1/(2**n*math.factorial(n)*np.sqrt(np.pi))*np.exp(-z**2/(1-z**2)**2)*(H_vector2(n, x))**2*(1+z**2)/(1-z**2)**2

b=np.pi/2
a=-np.pi/2
N=100
x,w=gaussxwab(N,a,b)

n=5
s=0.0
for i in range(N):
    s += w[i]*wavefunctionc(x[i],n)

print(np.sqrt(s))
        





    





