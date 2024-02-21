j=1.60218e-19
E=10*j
m=9.11e-31
V=9*j
h=6.62607015e-34
k1=((2*m*E)**(1/2))/h
k2=((2*m*(E-V))**(1/2))/h
T=4*k1*k2/(k1+k2)**2
R=((k1-k2)/(k1+k2))**2
print("The transmission coefficient is",T, "and the reflection coefficient is", R)
