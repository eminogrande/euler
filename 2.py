def fibonacci(stop):
    a, b, s = 0, 1, 0
    while b < stop:
        b, a = a + b, b
        if b % 2 == 0:
            s += b
        if b >= stop:
            break
    return s


print(fibonacci(4000000))
