import timeit

def test(n):
    return sum(range(n))

n = 10000
loop = 1000

# result = timeit.timeit('test(n)', globals=globals(), number=loop)
result = timeit.timeit(lambda: test(n), number=loop)

print(result / loop)