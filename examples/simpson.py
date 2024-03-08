from scipy import constants as constants
import numpy as np
#Define number of points and limits
N=34

epsilon=1.e-10
#start integral close to x=0 because integrand still dierges
a=epsilon
b=1.-epsilon

def f(x):
    import numpy as np
    f=1/(1+np.exp((x-1.5)/2))
    return f

def simpson(a,b,f,N):
#stepsize
	h=(b-a)/N
#End points
	s=(f(a)+f(b))*1/3*h
#Accumulate and normal sum by simpson formula
	for i in range(1,N,2):
		s+=4.*f(a+i*h)*h
		for i in range(2,N,2):
			s+=2.*f(a+i*h)*h

	return s
