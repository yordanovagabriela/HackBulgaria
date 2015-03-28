def transformation(number):
    list_of_digits = [int(x) for x in str(number)]
    nwl = []
    i = len(list_of_digits) - 1
    while(i >= 0):
        if i % 2 != 0:
            list_of_digits[i] *= 2
        i -= 1
    num = int(''.join(map(str, list_of_digits)))
    nwl = list(map(int, str(num)))
    if sum(nwl) % 10 == 0 and len(nwl) % 2 != 0:
        return True
    else:
        return False
print(transformation(79927398713))
