#Xiyue Shen

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
#plt.rcParams.update({'font.size': 22})

G = 6.6743e-11
m = 1.98892e30

def f(r,t): 
    x = r[0]
    v_x = r[1] 
    y = r[2]
    v_y = r[3]
    fx = v_x 
    fv_x = -G*m*x/((x**2+y**2)**(1.5)) 
    fy=v_y
    fv_y= -G*m*y/((x**2+y**2)**(1.5)) 
    return np.array([fx,fv_x,fy,fv_y] ,float)
 

#Initial values and initial step size
a = 0.0
b = 2e9
N = 1e6
h0 = (b-a)/N
h=h0
i=0
t=a
delta=3.1688e-5 #This is 1km per year. I transfer the unit into second per meter.


#empty arraties 
xpoints=[]
ypoints=[]
vxpoints=[]
vypoints=[]
tpoints=[]
dxarr=[] 
dyarr=[]
harray=[]

#arrays for initial values
r = np.array([4e12,0,0,500],float)


#grab first value
xpoints.append(r[0])
vxpoints.append(r[1])
ypoints.append(r[2])
vypoints.append(r[3])
tpoints.append(t)
dxarr.append(0)
dyarr.append(0)
harray.append(h)

while t<b: #condition on time
	r1= np.copy(r)
	r2= np.copy(r)	
	i+=1 #increment to count steps
	#RK4 used throughout
	#One large step
	k1 = 2.*h*f(r1,t)
	k2 = 2.*h*f(r1+0.5*k1,t+h)
	k3 = 2.*h*f(r1+0.5*k2,t+h)
	k4 = 2.*h*f(r1+k3,t+2*h)
	r1 += (k1+2*k2+2*k3+k4)/6
	# Two small steps
	
	k1 = h*f(r2,t)
	k2 = h*f(r2+0.5*k1,t+0.5*h)
	k3 = h*f(r2+0.5*k2,t+0.5*h)
	k4 = h*f(r2+k3,t+h)
	r2 += (k1+2*k2+2*k3+k4)/6
	
	k1 = h*f(r2,t)
	k2 = h*f(r2+0.5*k1,t+0.5*h)
	k3 = h*f(r2+0.5*k2,t+0.5*h)
	k4 = h*f(r2+k3,t+h)
	r2 += (k1+2*k2+2*k3+k4)/6

	#Calculate rho value and assess error
	dx=r1[0]-r2[0]
	dy=r1[2]-r2[2]
	epsilon=1e-7
	error = np.sqrt(dx**2+dy**2)
	rho = 30. * h * delta / (abs(dx))
	#adjust step size
	if rho>=1.0:
		t+=2*h
		h*=min(rho**0.25,1.001)
		r=r2
		xpoints.append(r[0])
		vxpoints.append(r[1])
		ypoints.append(r[2])
		vypoints.append(r[3])
		tpoints.append(t)
		dxarr.append(dx)
		dyarr.append(dy)
		harray.append(h)
	else:
		h*=rho**0.25
		# adapt the step size
	#after we adapt the setp size, we also want to keep the r value
 #so that we don't make our code run into endless loop
		r2=np.copy(r)
		k1 = h*f(r2,t)
		k2 = h*f(r2+0.5*k1,t+0.5*h)
		k3 = h*f(r2+0.5*k2,t+0.5*h)
		k4 = h*f(r2+k3,t+h)
		r2 += (k1+2*k2+2*k3+k4)/6
		
		k1 = h*f(r2,t)
		k2 = h*f(r2+0.5*k1,t+0.5*h)
		k3 = h*f(r2+0.5*k2,t+0.5*h)
		k4 = h*f(r2+k3,t+h)
		r2 += (k1+2*k2+2*k3+k4)/6
		harray.append(2*h)

#make a plot
plt.plot(xpoints,ypoints)
plt.title(r'Comet Trajectory')
plt.xlabel(r'x coordinate distance from the sun (meter)')
plt.ylabel(r'y coordinate distance from the sun (meter)')

plt.show()

plt.scatter(xpoints[::20],ypoints[::20],s=2)
plt.title(r'Comet Trajectory')
plt.xlabel(r'x coordinate distance from the sun (meter)')
plt.ylabel(r'y coordinate distance from the sun (meter)')

plt.show()
