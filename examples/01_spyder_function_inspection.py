"""Inspect local/global random data generation in Spyder. Requires NumPy."""

import numpy as np


def generate_data_local(N_TRAIN, NOISE_STD):
    """Return x and noisy exp(-x/2), each shaped (N_TRAIN, 1).

    N_TRAIN is a positive integer; NOISE_STD is a nonnegative scalar.
    A fresh Generator seeded with 5 is created on every call.
    """
    rng = np.random.default_rng(5)  # BREAKPOINT L1: before creating the local RNG
    x = rng.uniform(0.0, 6.0, size=(N_TRAIN, 1))  # BREAKPOINT L2: inspect rng
    y_true = np.exp(-x / 2.0)
    noise = rng.normal(0.0, NOISE_STD, size=(N_TRAIN, 1))
    y = y_true + noise
    return x, y  # BREAKPOINT L3: inspect x, y_true, noise, and y


def generate_data_global(N_TRAIN, NOISE_STD):
    """Generate the same model using NumPy's legacy global RandomState.

    This demonstration resets and advances the global random state.
    """
    np.random.seed(5)  # BREAKPOINT G1: before resetting global state
    x = np.random.uniform(0.0, 6.0, size=(N_TRAIN, 1))
    y_true = np.exp(-x / 2.0)
    noise = np.random.normal(0.0, NOISE_STD, size=(N_TRAIN, 1))
    y = y_true + noise
    return x, y  # BREAKPOINT G2: inspect the global-RNG version's local variables


if __name__ == "__main__":
    # Distinct caller names keep both results available in Variable Explorer.
    x_local, y_local = generate_data_local(10, 4 * 0.03)
    print("Local Generator")
    print("x^T =", x_local.T)  # (1, 10); x_local itself remains (10, 1)
    print("y^T =", y_local.T)

    x_global, y_global = generate_data_global(10, 4 * 0.03)
    print("Global RandomState")
    print("x^T =", x_global.T)  # (1, 10); x_global itself remains (10, 1)
    print("y^T =", y_global.T)
    print("Same x arrays:", np.array_equal(x_local, x_global))
