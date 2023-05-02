import numpy as np

l = list(range(1, 101))
print(l)

le1 = [i%5 for i in l]
print(le1)

le2 = [i for i in l if i%5==1]
print(le2)

for j in range(5):
    le3 = [i for i in l if i%5==j]
    print(le3)

le4 = []
for i in range(5):
    le4.append(l[i])
print(le4)

numExt = 10
le5_mean = []
for i in range(90):
    le5 = []
    for j in range(numExt):
        le5.append(l[i+j])
    le5_mean.append(np.mean(le5))
print(le5_mean)