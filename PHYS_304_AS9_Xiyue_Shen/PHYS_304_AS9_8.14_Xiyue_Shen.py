#Xiyue Shen

from numpy import array,arange
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
#plt.rcParams.update({'font.size': 22})

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
N = 1000
V0= 50*e # in j
a=1e-11
h = 20*a/N

def V(x):
    return V0*x**2/a**2 # the potential function

# differential equations
def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# define a function to solve the wavefunction
def solve(E):
    psi = 0.0
    phi = 1
    r = array([psi,phi],float)

    for x in arange(-10*a,10*a,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]

E=[]
# set up a loop for the first three energy states
for n in range(3):
    E1 = 260*n*e #first guess
    E2 = e #second guess
    psi2 = solve(E1)

    target = e/1000 #target accuracy
    while abs(E1-E2)>target: # if the guess is not accurate reassign the values and calculate a new energy by taking average
        psi1,psi2 = psi2,solve(E2)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    E.append(E2/e)

print("For the quantum harmonic oscillator:" "the ground state energy is", E[0],"eV; the first excited state energy is", E[1],"eV; The second excited state energy is ", E[2],"eV")

#part b

def V(x): #change the potential function
    return V0*x**4/a**4

E_newV=[]
# Energy bounds in joules (convert eV to joules)
for n in range(3):
    E1 = 490*n*e
    E2 = e
    psi2 = solve(E1)

    target = e/1000
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    E_newV.append(E2/e)

print("For the quantum anharmonic oscillator:" "the ground state energy is", E_newV[0],"eV; the first excited state energy is", E_newV[1],"eV; The second excited state energy is ", E_newV[2],"eV")

#part c

h = 10*a/N

state_labels = ["The ground state", "The first excited state", "The second excited state"]

for n in range(len(E_newV)): #for each energy state
    E=E_newV[n]*e
    psi = 0.0
    phi = 1
    psi_values=[]
    phi_values=[]
    r = array([psi,phi],float)

    for x in arange(-5*a,5*a,h): #inside the potential wall
        psi_values.append(r[0])
        phi_values.append(r[1])
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6 #calculate the wavefunction at each position

    psivalues=np.array(psi_values)
    psivalues2=psivalues**2

#do a intergal for normalization
    t = 1/2* h* psivalues2[0]+1/2 *h *psivalues2[-1]
    for k in range(1, len(psivalues2)):
        t+=psivalues2[k]*h
    
    Normalization=1/t

    plt.plot(arange(-5*a,5*a,h),Normalization*psivalues, label=state_labels[n])


plt.title(r'The first three state of an anharmonic quantum oscillator')
plt.xlabel(r'Displacement around the origin/m')
plt.ylabel(r'Normalized wavfunctions')
plt.legend()
plt.show()

