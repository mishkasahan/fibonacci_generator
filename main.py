def generator(n):
    for i in range(1, n+1):
        yield i*i

b = generator(10)
for i in range(10):
    print(next(b))
