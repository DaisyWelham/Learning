import matplotlib.pyplot as plt
import numpy as np

# Data Extraction
agents = [r'$\pi_R$', r'$\pi_P$', r'$\pi_A$', r'$\pi_I$', r'$\pi_F$', '$Q_Q$', '$Q_I$', '$Q_F$']
colors = {'Normal': '#2ecc71', 'Low': '#f39c12', 'High': '#3498db'}

# Overflow Data
normal_ov = [0.0324, 0.1006, 0.0000, 0.0044, 0.0040, 0.0000, 0.0150, 0.0146]
normal_ov_err = [0.0103, 0.0030, 0.0000, 0.0020, 0.0015, 0.011, 0.0048, 0.0061]
low_ov = [0.0098, 0.0672, 0.0000, 0.0035, 0.0031, 0.0000, 0.0150, 0.0146]
low_ov_err = [0.0044, 0.0029, 0.0000, 0.0016, 0.0012, 0.0008, 0.0048, 0.0061]
high_ov = [0.1511, 0.1835, 0.0000, 0.0069, 0.0060, 0.0000, 0.0706, 0.0790]
high_ov_err = [0.0154, 0.0022, 0.0000, 0.0027, 0.0025, 0.0018, 0.0088, 0.0095]

# Pump Data
normal_p = [1.0385, 1.0445, 1.4856, 0.8473, 0.8467, 1.0907, 0.9684, 0.9588]
normal_p_err = [0.0409, 0.0069, 0.0032, 0.0012, 0.0009, 0.0741, 0.0350, 0.0301]
low_p = [1.0385, 1.0445, 1.4854, 0.8453, 0.8448, 1.0166, 0.9684, 0.9588]
low_p_err = [0.0409, 0.0069, 0.0032, 0.0012, 0.0009, 0.0820, 0.0350, 0.0301]
high_p = [1.0385, 1.0445, 1.4876, 1.0031, 1.0032, 1.0701, 1.0336, 1.0421]
high_p_err = [0.0409, 0.0069, 0.0031, 0.0003, 0.0002, 0.0568, 0.0337, 0.0279]

y = np.arange(len(agents))
height = 0.25

# Constants for huge font sizes
TITLE_SIZE = 110
TICK_SIZE = 90
LABEL_SIZE = 100
LEGEND_SIZE = 100

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(80, 32))

# Plot 1: Overflow
ax1.barh(y + height, normal_ov, height, xerr=normal_ov_err, label='Normal Rain', color=colors['Normal'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax1.barh(y, low_ov, height, xerr=low_ov_err, label='Low Rain', color=colors['Low'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax1.barh(y - height, high_ov, height, xerr=high_ov_err, label='High Rain', color=colors['High'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax1.set_title(r'Overflow Rate ($m^3/s$)', fontsize=TITLE_SIZE, pad=60)
ax1.set_yticks(y)
ax1.set_yticklabels(agents, fontsize=LABEL_SIZE)
ax1.tick_params(axis='x', labelsize=TICK_SIZE)

# Plot 2: Pump Use
ax2.barh(y + height, normal_p, height, xerr=normal_p_err, color=colors['Normal'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax2.barh(y, low_p, height, xerr=low_p_err, color=colors['Low'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax2.barh(y - height, high_p, height, xerr=high_p_err, color=colors['High'], capsize=20, error_kw={'elinewidth':5, 'markeredgewidth':5})
ax2.set_title(r'Pump Use ($m^3/s$)', fontsize=TITLE_SIZE, pad=60)
ax2.set_yticks(y)
ax2.set_yticklabels(agents, fontsize=LABEL_SIZE)
ax2.tick_params(axis='x', labelsize=TICK_SIZE)

# Shared Legend
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=3, fontsize=LEGEND_SIZE, frameon=False, bbox_to_anchor=(0.5, -0.08))

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save as EPS
plt.savefig('wastewater_performance.eps', format='eps', bbox_inches='tight')
plt.close()