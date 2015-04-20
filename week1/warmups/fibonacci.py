from math import sqrt


def fibonacci(n):
    list_of_numbers = [int(((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))) for i in range(1, n+1)]
    return list_of_numbers
