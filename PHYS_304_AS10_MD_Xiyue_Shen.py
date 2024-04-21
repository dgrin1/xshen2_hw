#Xiyue Shen

#import all libraries and constants
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import Boltzmann
mass_of_argon = 39.948 # amu

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{bm}'
plt.rcParams['pgf.texsystem'] = 'pdflatex'  # or 'latex'
plt.rcParams.update({'font.size': 15})

def lj_force(r, epsilon, sigma):
     """
    Implementation of the Lennard-Jones potential 
    to calculate the force of the interaction.
    
    Parameters
    ----------
    r: float
        Distance between two particles (Å)
    epsilon: float 
        Potential energy at the equilibrium bond 
        length (eV)
    sigma: float 
        Distance at which the potential energy is 
        zero (Å)
    
    Returns
    -------
    float
        Force of the van der Waals interaction (eV/Å)
    """
     return 48 * epsilon * np.power(
        sigma, 12) / np.power(
        r, 13) - 24 * epsilon * np.power(
        sigma, 6) / np.power(r, 7)

def init_velocity(T, number_of_particles):
    """
    Initialise the velocities for a series of 
    particles.
    
    Parameters
    ----------
    T: float
        Temperature of the system at 
        initialisation (K)
    number_of_particles: int
        Number of particles in the system
    
    Returns
    -------
    ndarray of floats
        Initial velocities for a series of 
        particles (eVs/Åamu)
    """
    R = np.random.rand(number_of_particles) - 0.5
    #R=1+np.arange(number_of_particles)
    return R * np.sqrt(Boltzmann * T / (
        mass_of_argon * 1.602e-19))

# print(init_velocity(300,5))

def get_accelerations(positionsx, positionsy): # Add another input for y axis 
    """
    Calculate the acceleration on each particle
    as a  result of each other particle. 
    N.B. We use the Python convention of 
    numbering from 0.
    
    Parameters
    ----------
    positions: ndarray of floats
        The positions, in a single dimension, 
        for all of the particles
        
    Returns
    -------
    ndarray of floats
        The acceleration on each
        particle (eV/Åamu)
    """
    accel_x = np.zeros((positionsx.size, positionsx.size))
    accel_y = np.zeros((positionsy.size, positionsy.size)) # add one more array for y axis to make this as two dimension
    
    for i in range(0, positionsx.size - 1):
        for j in range(i + 1, positionsy.size):
            r_x = positionsx[j] - positionsx[i]
            r_y = positionsy[j] - positionsy[i] # add an array for ry

            rmag = np.sqrt(r_x**2 + r_y**2)
            force_scalar = lj_force(rmag, 0.0103, 3.4)

            force_x = force_scalar * r_x / rmag
            force_y = force_scalar * r_y / rmag # add an array for force on y axis

            accel_x[i,j] = force_x / mass_of_argon
            accel_x[j,i] = - force_x / mass_of_argon
            accel_y[i,j] = force_y / mass_of_argon # calculate acceleration on y 
            accel_y[j,i] = - force_y / mass_of_argon
    
    return np.sum(accel_x,axis=0),np.sum(accel_y,axis=0) #return two array on acceleration one for x and one for y

def update_pos(x, v, a, dt):
    """
    Update the particle positions.
    
    Parameters
    ----------
    x: ndarray of floats
        The positions of the particles in a 
        single dimension
    v: ndarray of floats
        The velocities of the particles in a 
        single dimension
    a: ndarray of floats
        The accelerations of the particles in a 
        single dimension
    dt: float
        The timestep length
    
    Returns
    -------
    ndarray of floats:
        New positions of the particles in a single 
        dimension
    """
    return x + v * dt + 0.5 * a * dt * dt

def update_velo(v, a, a1, dt):
    """
    Update the particle velocities.
    
    Parameters
    ----------
    v: ndarray of floats
        The velocities of the particles in a 
        single dimension (eVs/Åamu)
    a: ndarray of floats
        The accelerations of the particles in a 
        single dimension at the previous 
        timestep (eV/Åamu)
    a1: ndarray of floats
        The accelerations of the particles in a
        single dimension at the current 
        timestep (eV/Åamu)
    dt: float
        The timestep length
    
    Returns
    -------
    ndarray of floats:
        New velocities of the particles in a
        single dimension (eVs/Åamu)
    """
    return v + 0.5 * (a + a1) * dt

def run_md(dt, number_of_steps, initial_temp,snaptime, x,y, number_of_atoms): #add parameters for snaptime and number_of_atoms
    """
    Run a MD simulation.
    
    Parameters
    ----------
    dt: float
        The timestep length (s)
    number_of_steps: int
        Number of iterations in the simulation
    initial_temp: float
        Temperature of the system at 
        initialisation (K)
    x: ndarray of floats
        The initial positions of the particles in a 
        single dimension (Å)
        
    Returns
    -------
    ndarray of floats
        The positions for all of the particles 
        throughout the simulation (Å)
    """
    file = open('traj1.xyz', 'w') # create a file to save the data


    # create empty array for positions and velocity along x and y
    velocityx = np.zeros((number_of_steps, number_of_atoms))
    velocityy= np.zeros((number_of_steps, number_of_atoms))
    positionsx = np.zeros((number_of_steps, number_of_atoms))
    positionsy= np.zeros((number_of_steps, number_of_atoms))
 
    vx = init_velocity(initial_temp, number_of_atoms)
    vy = init_velocity(initial_temp, number_of_atoms)
    ax, ay = get_accelerations(x,y)

    # we update the loop for y dimension by adding more array
    for i in range(number_of_steps):

        x = update_pos(x, vx, ax, dt)
        y = update_pos(y, vy, ay, dt)

        a1x=get_accelerations(x,y)[0]
        a1y=get_accelerations(x,y)[1]


        vx = update_velo(vx, ax, a1x, dt)
        vy = update_velo(vy, ay, a1y, dt)

    
        positionsx[i, :] = x
        positionsy[i, :] = y

        velocityx[i, :] = vx
        velocityy[i, :] = vy

        
        if i%snaptime == 0: # save the data every (number_of_steps/snaptime) times
            file.write(str(number_of_atoms)+"\n")
            file.write("#\n")
            for atom in range(number_of_atoms):
                file.write("A\t" + str(x[atom])+ "\t" +str(y[atom]) +"\t0.0\n") # save data for x and y 
    
        
        
    return positionsx, positionsy, velocityx,velocityy

number_of_atoms = 5 # set 5 atoms for the test
x=1+5*np.arange(number_of_atoms) # initiate the position on x dimension
y=1+3*np.arange(number_of_atoms) # initiate the position on y dimension
sim_pos_x, sim_pos_y, vx, vy= run_md(0.1, 10000, 300, 200, x,y,number_of_atoms)
    

# Plot the x and y positions
for i in range(sim_pos_x.shape[1]):
    plt.plot(sim_pos_x[:, i], '.', label=r'atom {} x'.format(i+1))
    plt.plot(sim_pos_y[:, i], '.', label=r'atom {} y'.format(i+1))
plt.xlabel(r'Step')
plt.ylabel(r'Position/Å')
plt.title(r'Position of atoms')
plt.legend(frameon=False)
plt.show()


# Plot the velocity in two dimensions
for i in range(sim_pos_x.shape[1]):
    plt.plot(vx[:, i], '.', label='atom {} x'.format(i+1))
    plt.plot(vy[:, i], '.', label='atom {} y'.format(i+1))
plt.xlabel(r'Step')
plt.ylabel(r'Velocity(Å/s)')
plt.title(r'Velocity of atoms')
plt.legend(frameon=False)
plt.show()