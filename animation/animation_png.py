import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
x = np.arange(0, 10, 0.1)

ims = []
for a in range(50):
    y = np.sin(x - a)
    im = plt.plot(x, y, "r")
    file_path = "./png/"
    file_name = "test"+str(a).rjust(3,'0')+".png"
    file_save = file_path + file_name
    fig.savefig(file_save, dpi=300)
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims)

plt.show()