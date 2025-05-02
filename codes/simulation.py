import numpy as np
from config import dt, charges, masses, E_field, x_min, x_max, y_min, y_max

def run_simulation(medium_type, initial_positions, batch_size=1_000_000):
    positions = initial_positions.copy()
    velocities = np.zeros_like(positions)

    for _ in range(10):
        for start in range(0, len(positions), batch_size):
            end = min(start + batch_size, len(positions))
            forces = charges[start:end, np.newaxis] * E_field
            accelerations = forces / masses[start:end, np.newaxis]
            velocities[start:end] += accelerations * dt
            positions[start:end] += velocities[start:end] * dt

    positions[:, 0] = np.clip(positions[:, 0], x_min, x_max)

    if medium_type == "surface_enhanced":
        return apply_surface_enhancement(positions)
    return positions, None


def apply_surface_enhancement(positions):
    chord_length = 0.351e-3
    height = 0.145e-3
    R = (height / 2) + (chord_length ** 2) / (8 * height)
    alpha = np.arccos(1 - height / R)

    def arc_positions(N, x_max, y_center):
        theta = np.linspace(-alpha, alpha, N)
        return x_max + R * np.cos(theta) - R * np.cos(alpha), y_center + R * np.sin(theta)

    initial_gap = 0.6245e-3
    repeating_gaps = [0.351e-3, 1.249e-3]

    y_splits = [y_min]
    current = y_min + initial_gap
    y_splits.append(current)

    i = 0
    while current < y_max:
        gap = repeating_gaps[i % 2]
        current += gap
        if current <= y_max:
            y_splits.append(current)
        i += 1

    y_splits = np.array(y_splits)

    for i in range(len(y_splits) - 1):
        y_start, y_end = y_splits[i], y_splits[i + 1]
        y_center = (y_start + y_end) / 2
        indices = (positions[:, 1] >= y_start) & (positions[:, 1] < y_end)

        if np.isclose(y_end - y_start, 1.249e-3, atol=1e-6):
            positions[indices, 0] = x_max
        elif np.isclose(y_end - y_start, 0.351e-3, atol=1e-6):
            N = np.sum(indices)
            if N > 0:
                x_arc, y_arc = arc_positions(N, x_max, y_center)
                positions[indices, 0] = x_arc
                positions[indices, 1] = y_arc

    return positions, y_splits