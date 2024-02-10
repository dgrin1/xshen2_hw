#Exercise 2.2 part b
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

T=input("what period T you would like to?")
T=float(T)
G=6.67e-11
M=5.97e24
R=6.371e6
pi=np.pi
height=(G*M*T**2/(4*pi**2))**(1/3)-R
print("the altitude of the satellite is", height)

#part c
a= 24*3600
b=90*60
c=45*60
for Tc in (a,b,c):
    height=(G*M*Tc**2/(4*pi**2))**(1/3)-R
    print("the altitude of the satellite for",Tc,"seconds is",height, "meters.")

#part d
Ta= 24*3600
Tb= 23.93*3600
ha=(G*M*Ta**2/(4*pi**2))**(1/3)-R
hb=(G*M*Tb**2/(4*pi**2))**(1/3)-R
print("the discrepancy for a sidereal day is",ha-hb,"meters")

#for fun
Ts = np.linspace(1, 100000, 500)
heights = (G * M * Ts**2 / (4 * pi**2))**(1/3) - R
plt.plot(Ts, heights)
plt.xlabel(r'Period'+r'$~T~$'+'(seconds)')
plt.ylabel(r'Altitude'+r'$~H~$'+'(meters)')
plt.title(r'Satellite Altitude for Various Periods')
plt.grid(True)
plt.show()
