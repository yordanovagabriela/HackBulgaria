def fact(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
