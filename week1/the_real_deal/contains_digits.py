def contains_digits(number, digits):
    bool_is = True
    for i in digits:
        if str(i) in str(number):
            bool_is = True
        else:
            bool_is = False
    return bool_is
print(contains_digits(1234, [1, 2]))
