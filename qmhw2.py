import numpy as np
import matplotlib.pyplot as plt

e = 1.6e-19  # eV to Joules
V = 10 * e
L = 1.8e-9 / 2
m = 9.11e-31
h_bar = (6.63e-34) / (2 * np.pi)
a = (np.sqrt(2 * m) * L) / h_bar
E = np.arange(0, V + 0.01 * e, 0.01 * e)

alpha_by_k = np.sqrt((V - E) / E)

# Handle divide by zero for tan and cot
with np.errstate(divide='ignore', invalid='ignore'):
    y1 = np.tan(a * np.sqrt(E))
    y2 = -1 / np.tan(a * np.sqrt(E))

# Back to eV
E = E / e
y3 = y1
y4 = y2
alphaK = alpha_by_k

plt.figure('Transmission Coefficient vs Energy')
plt.plot(E, alphaK, label='Transmission Coefficient (alpha/k)')
plt.plot(E, y3, label='tan(a*sqrt(E))', color='red', linestyle='--')
plt.plot(E, y4, label='-cot(a*sqrt(E))', color='green', linestyle='--')
plt.axhline(0, color='red', linewidth=0.5)
plt.axvline(0, color='red', linewidth=0.5)

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlim([0, 10])
plt.ylim([0, 10])  # Adjusted y-axis limits to accommodate infinity
plt.xlabel('Energy (eV)')
plt.ylabel('Values')
plt.title('Transmission Coefficient and Trigonometric Functions vs Energy')
plt.legend()
plt.show()
