import numpy as np#type:ignore
import matplotlib.pyplot as plt#type:ignore
from scipy.stats import norm#type:ignore
 
# Gegeven gegevens
n = 100  # aantal partijen
p_wit = 0.42  # kans op winst met wit
p_zwart = 0.29  # kans op winst met zwart
p_remise = 0.29  # kans op remise

# Verwachte kansen
p_verwacht_wit = 0.40  # verwachte kans op winst met wit
p_verwacht_zwart = 0.30  # verwachte kans op winst met zwart
p_verwacht_remise = 0.30  # verwachte kans op remise

# Berekeningen voor de normale verdeling
mu_wit = n * p_verwacht_wit
sigma_wit = np.sqrt(n * p_verwacht_wit * (1 - p_verwacht_wit))

mu_zwart = n * p_verwacht_zwart
sigma_zwart = np.sqrt(n * p_verwacht_zwart * (1 - p_verwacht_zwart))

mu_remise = n * p_verwacht_remise
sigma_remise = np.sqrt(n * p_verwacht_remise * (1 - p_verwacht_remise))

# x-waarden voor de normale verdeling
x_wit = np.linspace(mu_wit - 4 * sigma_wit, mu_wit + 4 * sigma_wit, 100)
y_wit = norm.pdf(x_wit, mu_wit, sigma_wit)

x_zwart = np.linspace(mu_zwart - 4 * sigma_zwart, mu_zwart + 4 * sigma_zwart, 100)
y_zwart = norm.pdf(x_zwart, mu_zwart, sigma_zwart)

x_remise = np.linspace(mu_remise - 4 * sigma_remise, mu_remise + 4 * sigma_remise, 100)
y_remise = norm.pdf(x_remise, mu_remise, sigma_remise)

# Plot de normale verdelingen
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

plt.plot(x_wit, y_wit, label='Normale verdeling Winst met Wit', color='blue')
plt.plot(x_zwart, y_zwart, label='Normale verdeling Winst met Zwart', color='red')
plt.plot(x_remise, y_remise, label='Normale verdeling Remise', color='green')

# Voeg gemiddelde en werkelijke resultaten toe
plt.axvline(mu_wit, color='blue', linestyle='--', label='Gemiddelde Winst met Wit (40)')
plt.axvline(mu_zwart, color='red', linestyle='--', label='Gemiddelde Winst met Zwart (30)')
plt.axvline(mu_remise, color='green', linestyle='--', label='Gemiddelde Remise (30)')

plt.axvline(n * p_wit, color='blue', linestyle=':', label='Werkelijke Winst met Wit (42)')
plt.axvline(n * p_zwart, color='red', linestyle=':', label='Werkelijke Winst met Zwart (29)')
plt.axvline(n * p_remise, color='green', linestyle=':', label='Werkelijke Remise (29)')

plt.title('Normale Verdeling van Schaakresultaten')
plt.xlabel('Aantal Partijen')
plt.ylabel('Kansdichtheid')
plt.legend()
plt.grid()
plt.show()
input("Druk op Enter om af te sluiten...")
