import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp

fig = plt.figure()

ax1 = fig.add_subplot(111, title='test', xlabel='X', ylabel='Y',
        xlim=[0, 1], ylim=[-1 , 1])

xs = np.linspace(0, 1, 11).tolist()
ys = [np.sin(2 * np.pi * xs[i]) for i in range(11)]

print(xs)
print(ys)

Xs, Ys = [], []
for i in range(11):
    Xs.append(xs[:i+1])
    Ys.append(ys[:i+1])

# animatplotの途中でエラーが出るようになった。そのための修正が以下の２行
Xs = np.asanyarray(Xs, dtype=object)
Ys = np.asanyarray(Ys, dtype=object)

block = amp.blocks.Line(Xs, Ys, ax=ax1)
anim = amp.Animation([block])
#anim.save_gif("sin_curve")


plt.show()