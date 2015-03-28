from math import factorial
def factorial_digits(number):
    return sum([factorial(int(x)) for x in list(str(number))])
print(func(999))

