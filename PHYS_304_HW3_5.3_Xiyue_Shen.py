from scipy import constants as constants
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

#Define number of points and limits
N=30

epsilon=1.e-10
#start integral close to x=0 because integrand still dierges
a=0
b=1.-epsilon

def f(t):
	#enter the funtion 
    f=np.exp(-t**2)
    return f

def g(z):
	g=np.exp(-z**2/(1-z)**2)/(1-z)**2
	return g
	

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

z=np.arange(0.5,1,0.03)
s_value=np.zeros_like(z)
s_better=np.zeros_like(z)
for i in range(len(z)):
	s=(simpson(a,1,f,N)+simpson(1/2,z[i],g,N))
	s_value[i]=s
	N*=2
	better_s=(simpson(a,1,f,N)+simpson(1/2,z[i],g,N))
	s_better[i]=better_s
	print('finish',z[i])

plt.plot(z,s_value,label='N=30')
plt.plot(z,s_better,label='N=60')
plt.axvline(x=3/4,label='x=3')
plt.xlabel("z")
plt.ylabel("Integrand Value")
plt.legend()
plt.show()
