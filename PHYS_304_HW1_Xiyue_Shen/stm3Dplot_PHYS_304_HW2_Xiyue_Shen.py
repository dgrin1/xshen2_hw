from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'

data = np.loadtxt("stm.txt", float)
x = np.arange(data.shape[1])
y = np.arange(data.shape[0])
x, y = np.meshgrid(x, y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surfaceplot = ax.plot_surface(x, y, data, cmap='viridis', shade=True)


fig.colorbar(surfaceplot)
plt.title(r"STM"+r"$~3D~$"+r'Plot')
plt.show()