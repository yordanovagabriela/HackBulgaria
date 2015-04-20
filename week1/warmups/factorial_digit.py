from fact import fact


def factorial_digits(number):
    if number < 0:
        return sum([fact(int(x)) for x in list(str(-number))])
    return sum([fact(int(x)) for x in list(str(number))])
