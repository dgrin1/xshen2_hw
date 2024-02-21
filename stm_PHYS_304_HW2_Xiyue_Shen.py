from numpy import loadtxt
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

data=loadtxt("stm.txt",float)
vmin_value = data.min()  # or set a specific value
vmax_value = data.max()  # or set a specific value
plt.imshow(data, origin="lower", interpolation='nearest', vmin=vmin_value, vmax=vmax_value)
plt.gray()
plt.colorbar()
plt.title(r"STM Density Plot")
plt.show()

data=loadtxt("stm.txt",float)
vmin_value = data.min()  # or set a specific value
vmax_value = data.max()  # or set a specific value
plt.imshow(data, origin="lower", interpolation='nearest', vmin=vmin_value, vmax=vmax_value)
plt.colorbar()
plt.title(r"STM Density Plot")
plt.jet()
plt.show()

vmin_value = data.min()  # or set a specific value
vmax_value = data.max()  # or set a specific value
plt.imshow(data, origin="lower", cmap='viridis', interpolation='nearest', vmin=vmin_value, vmax=vmax_value)
plt.viridis()
plt.title(r"STM Density Plot")
plt.show()

from mpl_toolkits.mplot3d import Axes3D

