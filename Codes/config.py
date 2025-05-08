import numpy as np
from scipy.constants import e, m_e

# Simulation parameters
dt = 1e-3
num_steps = 1000
num_particles = 100000000

# Medium bounds
x_min, x_max = 0, 0.1e-3
y_min, y_max = 0, 1.6e-3

# Plotting ranges
x_plot_range = (-1e-3, 1.15e-3)
y_plot_range = (-1e-2, 1e-2)

# Constants
epsilon_0 = 8.854e-12
epsilon_r = 4
particle_radius = 0.3225e-9
R = 8.314
T = 298
F = 96485
I = 29.69287731
E_field = np.array([1e3, 0])  # Constant electric field in x-direction

# Derived values
D = epsilon_0 * epsilon_r
phi_0 = e / (4 * np.pi * D * particle_radius)
d = np.sqrt((D * R * T) / (2 * F**2 * I))
k = 1 / d
x_bins = np.linspace(x_min, x_max, 200)

# Surface areas
surface_area_flat = y_max - y_min
surface_area_enhanced = 1.7154e-3

# Particle properties (per particle)
charges = np.full(num_particles, e)     # Charge of each particle
masses = np.full(num_particles, m_e)    # Mass of each particle
