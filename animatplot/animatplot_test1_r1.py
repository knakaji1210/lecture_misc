"""
Introduction to animatplot
https://animatplot.readthedocs.io/en/latest/tutorial/getting_started..html#Basic-Animation
"""

import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp


def main():
    xs = np.linspace(0, 1, 50)
    print(xs)
    ts = np.linspace(0, 1, 20)
    print(ts)
    Xs = np.asarray([xs] * len(ts))
    print(Xs)
    Ys1 = [np.sin(2 * np.pi * (xs + t)) for t in ts]
    Ys2 = [np.cos(2 * np.pi * (xs + t)) for t in ts]
    """
    # you can also write
    Xs, Ts = np.meshgrid(xs, ts)
    Ys = np.sin(2 * np.pi * (Xs + Ts))
    """
    block1 = amp.blocks.Line(Xs, Ys1)
    block2 = amp.blocks.Line(Xs, Ys2)
    anim = amp.Animation([block1, block2])
    anim.save_gif("./gif/sin_curve_r1")
    plt.show()


if __name__ == '__main__':
    main()