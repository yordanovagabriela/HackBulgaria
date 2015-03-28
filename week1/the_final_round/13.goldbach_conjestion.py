def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def goldbach(n):
    result = []
    list_num = [x for x in range(2, n) if is_prime(x)]
    for i in list_num:
        for j in list_num:
            if i + j == n:
                result.append((i, j))
                list_num.remove(i)
                list_num.remove(j)
    return result
print(goldbach(100))
