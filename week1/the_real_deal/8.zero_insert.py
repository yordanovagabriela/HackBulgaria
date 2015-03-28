def zero_insert(n):
    list_digits = [int(i) for i in str(n)]
    size = len(list_digits)
    i = 0
    while(i < size-1):
        if list_digits[i] == list_digits[i+1] or (list_digits[i]+list_digits[i+1])%10 == 0:
            list_digits.insert(i+1, 0)
            size = size+1
        i = i+1
    return "".join(map(str, list_digits))
print(zero_insert(1))






