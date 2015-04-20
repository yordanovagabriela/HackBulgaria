def sum_of_divisors(n):
    sum_of_divisors = 0
    if n < 0:
        n = -n
    for i in range(1, n+1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
