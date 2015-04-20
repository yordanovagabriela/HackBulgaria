def prime_number_of_divisors(n):
    sum = 0
    bool_p = True
#Finds the number of divisors
    for i in range(1, n+1):
        if n % i == 0:
            sum = sum+1
#Checks if this number is prime
    for i in range(2, sum):
        if sum % i == 0:
            bool_p = False
            break
        else:
            bool_p = True
    return bool_p
