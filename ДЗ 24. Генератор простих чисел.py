def prime_generator(end):
    sieve = [True] * (end + 1)
    sieve[0:2] = [False, False]

    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = False

    for i in range(2, end + 1):
        if sieve[i]:
            yield i


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
print(list(prime_generator(10)))