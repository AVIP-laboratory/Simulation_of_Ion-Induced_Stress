import matplotlib.pyplot as plt
import numpy as np
import os

def plot_distances(bin_centers, avg_d, min_d, max_d, title=""):
    plt.plot(bin_centers, avg_d, label="Average")
    plt.plot(bin_centers, min_d, linestyle="--", label="Min")
    plt.plot(bin_centers, max_d, linestyle=":", label="Max")
    plt.xlabel("Y position (m)")
    plt.ylabel("Distance (m)")
    plt.legend()
    plt.title(title)
    plt.show()

def plot_stress_bar(y_bins, stress1, stress2, label1="A", label2="B", ylabel="Stress (N/m²)"):
    plt.bar(y_bins, stress1, width=(y_bins[1] - y_bins[0]), color='red', label=label1, align='edge')
    plt.bar(y_bins, stress2, width=(y_bins[1] - y_bins[0]), color='green', alpha=0.5, label=label2, align='edge')
    plt.xlabel("Y position (m)")
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(f"{ylabel} Distribution")
    plt.show()

def save_data(prefix, bin_centers, avg_d, min_d, max_d, counts):
    os.makedirs("result", exist_ok=True)
    np.savetxt(f"result/{prefix}_bin_centers.txt", bin_centers, delimiter=",")
    np.savetxt(f"result/{prefix}_average_distance.txt", avg_d, delimiter=",")
    np.savetxt(f"result/{prefix}_min_distance.txt", min_d, delimiter=",")
    np.savetxt(f"result/{prefix}_max_distance.txt", max_d, delimiter=",")
    np.savetxt(f"result/{prefix}_counts.txt", counts, delimiter=",")