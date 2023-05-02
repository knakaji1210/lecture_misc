import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
from pylab import rcParams

fs = 40000.0
fc = 40.0
fm = 4.0

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)

for ax in [ax1, ax2, ax3, ax4]:
    ax.axis('off')

time = np.arange(fs) / fs
ts = np.linspace(0, 1, 100)
Xs, Ts = np.meshgrid(time, ts)

Y_modulator = np.sin(2.0 * np.pi * fm * (Ts + Xs))
Y_carrier = np.sin(2.0 * np.pi * fc * (Ts + Xs))
Y_am = np.sin(2. * np.pi * fc * (Ts + Xs)) * (1 + 0.9 * np.cos(2.0 * np.pi * fm * (Ts + Xs)))
Y_fm = np.sin(2. * np.pi * (fc * (Ts + Xs) + Y_modulator))

B_modulator = amp.blocks.Line(Xs, Y_modulator, ax=ax1)
B_carrier = amp.blocks.Line(Xs, Y_carrier, ax=ax2)
B_am = amp.blocks.Line(Xs, Y_am, ax=ax3)
B_fm = amp.blocks.Line(Xs, Y_fm, ax=ax4)

anim = amp.Animation([B_modulator, B_carrier, B_am, B_fm])
anim.save_gif("./gif/am_fm")

plt.show()