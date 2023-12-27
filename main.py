def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator(10)
for i in range(10):
    print(next(fib_gen))
