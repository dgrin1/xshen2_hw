import numpy as np
import matplotlib.pyplot as plt
from random import randrange, random

# Simulation parameters
N = 20  # Lattice size
J = 1   # Interaction energy scale
k = 1   # Boltzmann constant
steps = 10000
Temp = np.arange(0.2, 1.6, 0.1)

# Initialize the lattice with all spins aligned (theta_i = 0)
config = np.zeros((N, N))

def energy(config):
    """Compute the total energy of the lattice."""
    total_energy = 0
    for i in range(N):
        for j in range(N):
            next_i = (i + 1) % N
            next_j = (j + 1) % N
            total_energy += -J * (np.cos(config[i][j] - config[i][next_j]) + np.cos(config[i][j] - config[next_i][j]))
    return total_energy

def metropolis_step(config, T):
    """Perform one Metropolis update step."""
    i, j = randrange(N), randrange(N)
    current_angle = config[i][j]
    proposed_angle = current_angle + np.random.uniform(-np.pi, np.pi)
    config[i][j] = proposed_angle

    dE = energy(config) - energy(np.copy(config))
    if dE > 0 and np.exp(-dE / (k * T)) < random():
        config[i][j] = current_angle  # reject change

def run_simulation():
    """Run the simulation across temperatures and plot energy."""
    average_energies = []
    for T in Temp:
        config = np.zeros((N, N))  # reset lattice for each temperature
        # Equilibrate
        for _ in range(int(steps/10)):
            metropolis_step(config, T)
        # Measurement
        energy_samples = []
        for _ in range(steps - int(steps/10)):
            metropolis_step(config, T)
            if _ % 100 == 0:  # sample energy every 100 steps
                energy_samples.append(energy(config))
        average_energies.append(np.mean(energy_samples))

    plt.plot(Temp, average_energies, marker='o')
    plt.xlabel('Temperature')
    plt.ylabel('Average Energy')
    plt.title('Average Energy vs Temperature for a $20\\times20$ XY Model')
    plt.grid(True)
    plt.show()

run_simulation()
