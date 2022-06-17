def prime_number(number):
    count = 0

    for x in range(1, number+1):
        if number % x == 0:
            count+=1

    if count == 2:
        return number

primes = []

for x in range (1, 100):
    if prime_number(x) != None:
       primes.append(x)

print(primes)