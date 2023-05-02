"""
Introduction to animatplot
https://animatplot.readthedocs.io/en/latest/tutorial/getting_started..html#Basic-Animation
"""

import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp


fig = plt.figure()

ax1 = fig.add_subplot(111, title='test', xlabel='t', ylabel='sin(t)', xlim=[0, 1])
ax1.set_xticks(np.linspace(0, 1, 5))
ax1.set_yticks(np.linspace(-1, 1, 5))

xs = np.linspace(0, 2*np.pi, 100)
Xs = [xs[:i] for i in range(24)]
# Ys = np.sin(2 * np.pi * (Xs)) # 前はこれで通っていたと思うのだがうまくいかないので、以下のように修正
ys = np.sin(2 * np.pi * (xs))
Ys = [ys[:i] for i in range(24)]

# animatplotの途中でエラーが出るようになった。そのための修正が以下の２行
Xs = np.asanyarray(Xs, dtype=object)
Ys = np.asanyarray(Ys, dtype=object)

"""
# you can also write
Xs, Ts = np.meshgrid(xs, ts)
Ys = np.sin(2 * np.pi * (Xs + Ts))
"""
block = amp.blocks.Line(Xs, Ys, ax=ax1)
anim = amp.Animation([block])
anim.save_gif("./gif/sin_curve_r3")

plt.show()

