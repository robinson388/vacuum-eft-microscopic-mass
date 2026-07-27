import numpy as np
import matplotlib.pyplot as plt

# Physical constants (SI units)
hbar = 1.054571817e-34      # Reduced Planck constant (J*s)
c = 299792458               # Speed of light (m/s)
alpha = 1.0 / 137.035999    # Fine-structure constant
me = 9.1093837015e-31       # Electron mass (kg)

# Reduced Compton wavelength (Attractor Radius r_*)
r_star = hbar / (me * c)    # ~ 3.86e-13 m

# Derived surface tension sigma_eff
sigma_eff = (alpha / (8 * np.pi)) * (me**3 * c**5) / (hbar**2)

# Range of radii around the Compton scale (0.2 r_* to 3.0 r_*)
r = np.linspace(0.2 * r_star, 3.0 * r_star, 1000)

# Energy components in Joules
E_bulk = (alpha * hbar * c) / r
E_surf = 4 * np.pi * sigma_eff * (r**2)
E_tot = E_bulk + E_surf

# Convert energy to MeV for plotting
Joules_to_MeV = 1.602176634e-13
E_bulk_MeV = E_bulk / Joules_to_MeV
E_surf_MeV = E_surf / Joules_to_MeV
E_tot_MeV = E_tot / Joules_to_MeV
me_MeV = (me * c**2) / Joules_to_MeV # ~ 0.511 MeV

# Plotting the attractor profile
plt.figure(figsize=(8, 6), dpi=300)
plt.plot(r / r_star, E_bulk_MeV, '--', color='tab:red', label=r'$E_{\mathrm{bulk}}(r)$ (3D Self-Energy)')
plt.plot(r / r_star, E_surf_MeV, '--', color='tab:blue', label=r'$E_{\mathrm{surf}}(r)$ (2D Boundary Tension)')
plt.plot(r / r_star, E_tot_MeV, '-', color='black', linewidth=2, label=r'$E_{\mathrm{tot}}(r)$ (Effective Attractor)')

# Mark the attractor minimum (electron mass)
plt.axvline(x=1.0, color='gray', linestyle=':', alpha=0.7)
plt.scatter([1.0], [me_MeV], color='tab:green', zorder=5, s=80,
            label=rf'Attractor Minimum: $r_* = \lambda_c$' + '\n' + f'$E_{{min}} = {me_MeV:.3f}$ MeV')


plt.title('Vacuum Response Local Attractor: Electron Rest Mass', fontsize=12)
plt.xlabel(r'Normalized Radius ($r / \lambda_c$)', fontsize=11)
plt.ylabel('Energy (MeV)', fontsize=11)
plt.ylim(0, 2.0)
plt.xlim(0.2, 3.0)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()

# Save plot for LaTeX
plt.savefig('attractor_profile.png')
print("[SUCCESS] Graph successfully generated and saved as 'attractor_profile.png'")
