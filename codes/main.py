from config import *
from simulation import run_simulation
from stress_analysis import (
    compute_nearest_neighbor_distances_by_y_bin,
    compute_stress,
    compute_stress_by_repulsion_chunked
)
from utils import plot_distances, plot_stress_bar, save_data
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import e, m_e

# Initialize
np.random.seed(42)
total_start = time.time()

# Particle properties
charges = np.full(num_particles, e)
masses = np.full(num_particles, m_e)

# Generate initial positions
initial_positions = np.column_stack((
    np.random.uniform(x_min, x_max, num_particles),
    np.random.uniform(y_min, y_max, num_particles)
))

# Run simulations
sim_start = time.time()
positions_flat, _ = run_simulation("flat", initial_positions)
positions_enhanced, y_splits = run_simulation("surface_enhanced", initial_positions)
print(f"✅ Simulation Time: {time.time() - sim_start:.2f} seconds")

# Compute inter-particle distances
bin_centers, avg_d, min_d, max_d, counts = compute_nearest_neighbor_distances_by_y_bin(positions_flat)
bin_centers_en, avg_d_en, min_d_en, max_d_en, counts_en = compute_nearest_neighbor_distances_by_y_bin(positions_enhanced)

# Save distance data
save_data("flat", bin_centers, avg_d, min_d, max_d, counts)
save_data("enhanced", bin_centers_en, avg_d_en, min_d_en, max_d_en, counts_en)

# Plot distances
plot_distances(bin_centers, avg_d, min_d, max_d, title="Flat Medium")
plot_distances(bin_centers_en, avg_d_en, min_d_en, max_d_en, title="Enhanced Medium")

# Compute stress
stress_start = time.time()
y_bins_flat, stress_flat = compute_stress(positions_flat, charges, surface_area_flat)
y_bins_enhanced, stress_enhanced = compute_stress(positions_enhanced, charges, surface_area_enhanced)

y_bins = np.linspace(y_min, y_max, 300)
stress_y_flat, = compute_stress_by_repulsion_chunked(positions_flat, particle_radius, surface_area_flat, x_bins, y_bins)
stress_y_enh, = compute_stress_by_repulsion_chunked(positions_enhanced, particle_radius, surface_area_enhanced, x_bins, y_bins)
print(f"✅ Stress Calculation Time: {time.time() - stress_start:.2f} seconds")

# Plot stress
plot_stress_bar(y_bins[:-1], stress_y_flat, stress_y_enh, label1="Flat", label2="Enhanced", ylabel="Repulsive Stress (N/m²)")
plot_stress_bar(y_bins_flat, stress_flat, stress_enhanced, label1="Flat", label2="Enhanced", ylabel="Electric Stress (N/m²)")

# Print summary
print(f"Repulsion Stress (Flat): {np.sum(stress_y_flat)/num_particles:.2e} N/m²")
print(f"Repulsion Stress (Enhanced): {np.sum(stress_y_enh)/num_particles:.2e} N/m²")

total_end = time.time()
print(f"✅ Total Execution Time: {total_end - total_start:.2f} seconds")