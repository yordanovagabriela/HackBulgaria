def is_prime(n):
    if n < 0:
        n = - n
    if n == 1 or n == 0:
        return False
    bool_prime = True
    for i in range(2, n//2+1):
        if n % i == 0:
            bool_prime = False
            break
        else:
            bool_prime = True
    return bool_prime
