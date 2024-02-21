import numpy as np
import math

def xcontant(x):
    i=0
    s,sold=0.e0,0.e0
    h,hold=0.e0,0.e0

    for i in range(x):
        sold=s
        s+=-1/(2*i+1)
        # if sold==s: break

    for i in range(x):
        hold=h
        h+=1/(2*i+2)
        # if hold==h: break

    return s,h

print(xcontant(1))
print(-47/60)
print(-5/6)