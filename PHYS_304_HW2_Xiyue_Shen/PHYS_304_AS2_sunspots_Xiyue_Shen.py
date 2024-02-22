#a
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

data = np.loadtxt("E:/Spring 2024/Phys H304/xshen2_hw/PHYS_304_HW2_Xiyue_Shen/sunspots.txt", float)
#Here I put the path of the file. This is specific to my computer. 
#You need to change it when downloading to your own computer.
plt.plot(data[:,0],data[:,1],'.')
plt.title(r"Sunspot Plot")
plt.xlabel(r'Time/Day')
plt.ylabel(r'Number of sunspots')
#plt.show()

#b
plt.figure()#create a new figure.
plt.plot(data[:1000, 0],data[:1000, 1],'.') #plot only the first 1000 data points
plt.title(r"Sunspot Plot")
plt.xlabel(r'Time/Day')
plt.ylabel(r'Number of sunspots')
plt.show()

#c
sunspots = data[:1000,1] #define a set of data

def Yave(x): #define a function which will calculate the average
    r=5
    for i in range(-r,r+1):
        Y=x+i 
    return (1/2*r)*Y #enter the function given in the textbook


plt.plot(data[:1000,0], sunspots, label='Original Data') #make a plot of original data
plt.plot(data[:1000,0], Yave(sunspots), label='Running Average') #plot the averaged data points on the same graph

plt.title("Sunspot Running Average")
plt.xlabel("Time/Day")
plt.ylabel("Number of Sunspots")
plt.legend()

plt.show()
