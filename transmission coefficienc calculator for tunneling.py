import numpy as np

def transmission_coefficient(E, U, L):
    h_bar = 6.626e-34 / (2 * np.pi)  # Reduced Planck constant (Joule second)
    m = 9.109e-31  # Electron mass (kg)
    e = 1.602e-19  # Elementary charge (Coulombs)

    # Energy of the particle in joules
    E_joules = E * e

    # Barrier height in joules
    U_joules = U * e

    # Barrier width in meters
    L_meters = L * 1e-9

    # Wave numbers inside and outside the barrier
    k1 = np.sqrt(2 * m * E_joules) / h_bar
    k2 = np.sqrt(2 * m * (U_joules - E_joules)) / h_bar

    # Transmission coefficient
    T = 1 / (1 + 0.25 * (((k1**2 + k2**2) / (k1 * k2))) * (np.sinh(k2 * L_meters)**2))
    
    return T

# Parameters
E1 = 12  # Energy of the particle in electronvolts
E2 = 16
U = 20  # Height of the potential barrier in electronvolts
L = 1  # Width of the potential barrier in nanometers

# Calculate transmission coefficients
T1 = transmission_coefficient(E1, U, L)
T2 = transmission_coefficient(E2, U, L)

# Print results
print(f"Transmission coefficient for E1 = {E1} eV: {T1:}")
print(f"Transmission coefficient for E2 = {E2} eV: {T2:}")
