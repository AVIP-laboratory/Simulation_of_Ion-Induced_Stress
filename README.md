# Particle-simulation under electric field

This repository contains a simulation framework for analyzing the behavior of charged particles in Nafion membranes under the influence of an electric field. The model supports both *Smooth-surface* and *Embossed-surface* structures, enabling comparison of particle distributions and stress fields in different morphologies.

---

## Highlights

- Electric field-driven motion of charged particles (2D simulation)
- Custom geometry support: smooth-surface vs. embossed-surface Nafion
- Binning-based analysis of nearest neighbor distances
- Debye-Hückel repulsion modeling for inter-particle stress
- Result saving and visualization (CSV, Matplotlib)

---

## Requirements

- `numpy`
- `scipy`
- `matplotlib`
- `os`

---

## Configurable Parameters

All physical constants and simulation parameters can be found in `config.py`. Key parameters include:

| Parameter        | Description                         | Default Value           |
|------------------|-------------------------------------|--------------------------|
| `num_particles`  | Number of particles                 | `100000000`            |
| `E_field`        | Electric field vector (V/m)         | `np.array([1e3, 0])`     |
| `particle_radius`| Particle radius (m)                 | `0.3225e-9`              |
| `I`              | Ionic strength (mol/L)              | `29.69`                  |
| `epsilon_r`      | Relative permittivity of Nafion     | `4`                      |

---

## Output Description

All results will be saved to a `result/` directory (automatically created).

- `*_bin_centers.txt`: Y-axis bin center positions
- `*_average_distance.txt`: Avg. nearest-neighbor distances per bin
- `*_stress.txt`: Stress per bin from electric field
- `*_stress_repulsion_*.txt`: Stress from particle-particle repulsion

Visualizations include:
- Inter-particle distance trends by bin
- Stress distribution comparisons (smooth vs. embossed)

---

## Analysis result

> Stress distribution along the Y-axis for both membrane types

![image](https://github.com/user-attachments/assets/a640846d-64a8-439f-844f-847252524e1c)

---

## Code Description

| File                | Description |
|---------------------|-------------|
| **`main.py`**       | Main execution script. Runs the simulation for smooth-surface and embossed-surface media, computes particle distances and stress distributions, and visualizes results. |
| **`config.py`**     | Contains all global constants and simulation parameters, such as particle radius, Debye length, electric field, and number of particles. Changing this file customizes the whole simulation. |
| **`simulation.py`** | Defines the particle movement logic under the influence of an electric field. Also includes geometric transformation logic for simulating surface-enhanced (arc-shaped bump) media. |
| **`stress_analysis.py`** | Provides analytical tools for measuring particle interactions. Includes nearest-neighbor distance analysis, electric stress from external field, and mechanical stress from Debye-Hückel repulsion. |
| **`utils.py`**      | Utility functions for plotting graphs and saving simulation results (as `.txt`). Automatically creates output directories as needed. |
