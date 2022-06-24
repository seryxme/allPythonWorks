def fibonacci(number):
    x = 0
    y = 1
    fib_seq = [x, y]
    count = 0

    while count <= number:
        fib_seq.append(fib_seq[x] + fib_seq[y])
        x += 1
        y += 1
        count += 1
    return fib_seq

print(fibonacci(5))
