import timeit
import numpy as np

n = 1
L = [[0 for _ in range(10**n)] for _ in range(10**n)]
A = np.array(L)

def func1(a):
    for i in range(10**n):
        for j in range(10**n):
            a[i][j]

def func2(a):
    for i in range(10**n):
        for j in range(10**n):
            a[i,j]

print(timeit.timeit(lambda :func1(L), number=100))
print(timeit.timeit(lambda :func1(A), number=100))
print(timeit.timeit(lambda :func2(A), number=100))
