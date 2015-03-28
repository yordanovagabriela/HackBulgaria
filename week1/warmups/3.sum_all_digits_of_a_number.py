def sum_of_digits(n):
    if n < 0:
        return sum(map(int, str(-n)))
    else:
        return sum(map(int, str(n)))
print (sum_of_digits(-4634))
