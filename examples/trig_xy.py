import numpy as np
import math

def xcos(x):
    x=x%(2.e0*np.pi)
    i=0
    s,sold=0.e0,0.e0

    for i in range(10000):
        sold=s
        s+=float(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        if sold==s: break
    return s
