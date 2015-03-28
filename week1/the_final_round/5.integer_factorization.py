def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def func(n):
    div = []
    listnew = []
    if is_prime(n):
        return [(n, 1)]
    for i in range(2, n):
        if n % i == 0:
            div.append(i)
            n = n // i
            while(n % i == 0):
                div.append(i)
                n = n // i
            listnew.append((i, div.count(i)))
    return listnew
print(func(89))
