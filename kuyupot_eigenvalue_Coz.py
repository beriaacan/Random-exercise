import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Potansiyel enerji fonksiyonu (kuyu potansiyeli örneği)
def potential_energy(x, a, V0):
    return np.piecewise(x, [x < -a/2, (x >= -a/2) & (x <= a/2), x > a/2], [lambda x: 0, lambda x: -V0, lambda x: 0])

# Schrödinger denkleminin sağ tarafı
def schrodinger_eq(y, x, energy, a, V0):
    h_bar = 1  # Planck sabiti / (2*pi)
    m = 1      # Parçacığın kütlesi

    V = potential_energy(x, a, V0)
    return [y[1], (2 * m / h_bar**2) * (V - energy) * y[0]]

# Enerji özdeğerlerini bulmak için bir fonksiyon
def find_eigenvalues(energy_guess, x, a, V0):
    eigenvalues = []

    for guess in energy_guess:
        solution = odeint(schrodinger_eq, [0, 1], x, args=(guess, a, V0))
        eigenvalues.append(solution[-1, 0])

    return eigenvalues

# x değer aralığını belirle
a = 2
V0 = 10
x = np.linspace(-a, a, 1000)

# Enerji özdeğerlerini tahmin et
energy_guess = np.linspace(-V0, 0, 10)

# Enerji özdeğerlerini bul
eigenvalues = find_eigenvalues(energy_guess, x, a, V0)

# Grafikle göster
plt.plot(energy_guess, eigenvalues, 'bo-')
plt.xlabel('Enerji Özdeğeri Tahmini')
plt.ylabel('Dalga Fonksiyonu Sınır Şartı')
plt.title('Enerji Özdeğerleri')
plt.grid(True)
plt.show()
