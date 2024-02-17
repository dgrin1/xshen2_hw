import numpy as np
import math

def gsin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s

def xcos(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(10000):
        sold=s
        s+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if sold==s: break
    return s

def xtan(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0
    h,hold=0.e0,0.e0

    for i in range(1000):
        sold=s
        s+=float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s:break

    for i in range(10000):
        hold=h
        h+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if hold==h: break

    return s/h

def xcsc(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(1000):
        sold=s
        s+=float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s:break

    return 1/s

def xsec(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(1000):
        sold=s
        s+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if sold==s:break

    return 1/s

def xcot(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0
    h,hold=0.e0,0.e0

    for i in range(1000):
        sold=s
        s+=float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s:break

    for i in range(10000):
        hold=h
        h+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if hold==h: break

    return h/s

