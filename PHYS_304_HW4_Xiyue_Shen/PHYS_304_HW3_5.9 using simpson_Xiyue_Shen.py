import numpy as np
from gaussxw import gaussxw
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
T=500
N=50
Cv_c=9*V*rho*k_B*(T/theta_D)**3
upper_bound=theta_D/T
lower_bound=1e-10

def simpson(a,b,f,N):
#stepsize
	h=(b-a)/N
#End points
	s=(f(a)+f(b))*h/3
#Accumulate and normal sum by simpson formula
	for i in range(1,N,2):
		s+=4.*f(a+i*h)*h
	for i in range(2,N,2):
		s+=2.*f(a+i*h)*h
	return s

s=Cv_c*(simpson(lower_bound,upper_bound,Cv,N))
print(s)

V=0.01
T=np.arange(5,500,1)
N=50
import matplotlib.pyplot as plt
#performing the integral
s=np.zeros_like(T)
u=np.zeros_like(T)
integral=0.0
for i in range(len(T)):
    upper_bound=theta_D/T[i]
    lower_bound=1e-10
    u[i]=upper_bound
    Cv_c=9*V*rho*k_B*(T[i]/theta_D)**3
    s[i]=Cv_c*(simpson(lower_bound,upper_bound,Cv,N))
# plt.plot(T,u)
# plt.show()
# import matplotlib.pyplot as plt
plt.plot(T,s)
plt.yscale("log")
plt.xscale("log")
# plt.xlim([1e-5,1e3])
plt.xlabel('Temperature(K)')
plt.ylabel("Heat Capacity(J/K)")
plt.title('Simpson Method')
plt.show()
print(T)