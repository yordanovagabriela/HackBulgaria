from math import sqrt


def fib_number(n):
    list_of_numbers = [int(((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))) for i in range(1, n+1)]
    return "".join(map(str, list_of_numbers))
print(fib_number(3))
