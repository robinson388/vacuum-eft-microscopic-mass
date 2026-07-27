import numpy as np
import matplotlib.pyplot as plt

# Redshift array covering the transition era
z = np.linspace(0, 5, 1000)

# 1. Standard Cosmological Constant (Lambda CDM)
w_lambda = -1.0 * np.ones_like(z)

# 2. Traditional Quintessence (smooth evolution CPL)
w_cpl = -1.0 + 0.2 * (z / (1.0 + z))

# 3. Robinson's Hysteresis Vacua (The Transient Phase Step)
# Represents a sudden topological freezing near z ~ 2.5 governed by f_hyst
z_crit = 2.5
delta_z = 0.4
f_hyst = 0.6718  # Your exact boundary factor

# Mathematical description of the non-equilibrium step and rebound
w_robinson = -1.0 + (1.0 - f_hyst) * np.exp(-((z - z_crit)/delta_z)**2) * np.sin(np.pi * (z - z_crit))

# Generate the prediction plot
plt.figure(figsize=(9, 6), dpi=300)
plt.axhline(y=-1.0, color='gray', linestyle=':', alpha=0.7, label=r'Standard $\Lambda$ (Einstein): $w = -1$')
plt.plot(z, w_cpl, '--', color='tab:blue', alpha=0.7, label=r'Standard Quintessence (Smooth Scalar)')
plt.plot(z, w_robinson, '-', color='black', linewidth=2.5, label=r"Robinson's EFT Pred: $w(z)$ Hysteresis Loop")

# Mark the critical transition region
plt.axvspan(z_crit - delta_z, z_crit + delta_z, color='tab:red', alpha=0.1, label='Primordial Freezing Domain')
plt.scatter([z_crit], [-1.0], color='tab:red', zorder=5, s=60)

plt.title('Transient Energy State w(z) Activation vs. Hysteresis Freezing', fontsize=12)
plt.xlabel('Redshift ($z$)', fontsize=11)
plt.ylabel(r'Dark Energy Equation of State $w(z)$', fontsize=11)
plt.xlim(0, 4.5)
plt.ylim(-1.1, -0.6)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right', fontsize=10)
plt.tight_layout()

plt.savefig('vacuum_prediction.png')
print("[SUCCESS] Extreme cosmological prediction graph saved as 'vacuum_prediction.png'")
