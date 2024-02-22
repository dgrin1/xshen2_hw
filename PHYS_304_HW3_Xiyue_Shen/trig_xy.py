import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

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

def xsin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(20):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s

def gcos(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(10000):
        sold=s
        s+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if sold==s: break
    return s

def xcos(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(20):
        sold=s
        s+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if sold==s: break
    return s

def gtan(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0
    h,hold=0.e0,0.e0

    for i in range(10000):
        sold=s
        s+=float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s:break

    for i in range(10000):
        hold=h
        h+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if hold==h: break

    return s/h

def xtan(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0
    h,hold=0.e0,0.e0

    for i in range(20):
        sold=s
        s+=float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s:break

    for i in range(20):
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

x=np.linspace(1, 30,100)

#plt.plot(x,np.vectorize(gsin)(x),label=r'$sin(x)$')
# plt.plot(x,np.vectorize(gcos)(x),label=r'$cos(x)$')
# plt.plot(x,np.vectorize(gtan)(x),label=r'$tan(x)$')

plt.plot(x,np.vectorize(xsin)(x),label=r'$sin(x)$')
plt.plot(x,np.vectorize(xcos)(x),label=r'$cos(x)$')
plt.plot(x,np.vectorize(xtan)(x),label=r'$tan(x)$')

plt.xlabel(r'$x$')
plt.ylim(-1.5,+1.5)
plt.legend()
plt.ylabel(r'Trig Functions')
plt.show()

plt.figure
plt.plot(x,(np.vectorize(xsin)(x)-np.vectorize(gsin)(x))/(np.vectorize(gsin)(x)),label=r'$sin(x)$')
plt.plot(x,(np.vectorize(xcos)(x)-np.vectorize(gcos)(x))/np.vectorize(gcos)(x),label=r'$cos(x)$')
plt.plot(x,(np.vectorize(xtan)(x)-np.vectorize(gtan)(x))/np.vectorize(gtan)(x),label=r'$tan(x)$')
plt.legend()
plt.show()
