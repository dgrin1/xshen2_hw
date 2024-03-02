import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
#set sample points
N=50.

#define constant
rho=6.022E28
theta_D=428
k_B=1.380649E-23

def Cv(x):
    Cv=x**4*np.exp(x)/(np.exp(x)-1)**2
    return Cv


#Part a
V=0.01
T=10
N=50
Cv_c=9*V*rho*k_B*(T/theta_D)**3
upper_bound=theta_D/T
lower_bound=0
x,w=gaussxw(N)
xp = 0.5*(upper_bound-lower_bound)*x + 0.5*(upper_bound+lower_bound)
wp = 0.5*(upper_bound-lower_bound)*w

#performing the integral
s=0.0
for k in range (N):
    s+=wp[k]*Cv(xp[k])

print(Cv_c*s)

#part b

V=0.01
T=np.arange(5,500,1)
N=50
import matplotlib.pyplot as plt
#performing the integral
s=np.zeros_like(T)
u=np.zeros_like(T)
for i in range(len(T)):
    upper_bound=theta_D/T[i]
    lower_bound=0
    u[i]=upper_bound
    Cv_c=9*V*rho*k_B*(T[i]/theta_D)**3
    x,w=gaussxw(N)
    xp = 0.5*(upper_bound-lower_bound)*x + 0.5*(upper_bound+lower_bound)
    wp = 0.5*(upper_bound-lower_bound)*w
    integral=0.0
    for k in range (N):
        integral+=wp[k]*Cv(xp[k])
    s[i]=Cv_c*integral

plt.plot(T,s)
plt.yscale("log")
plt.xscale("log")
plt.title('Gaussian Quadrature Method')
plt.xlabel('Temperature(K)')
plt.ylabel("Heat Capacity(J/K)")
plt.show()
