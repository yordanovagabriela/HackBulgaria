def palindrome(obj):
    return str(obj) == str(obj)[::-1]
def odd_ones(binary):
    return (bin(binary).count("1")) % 2 != 0
def next_hack(n):
    i = n + 1
    while(n):
        if n == 0:
            return 1
        elif palindrome(bin(i)[2:]) and odd_ones(i):
            return i
            break
        else:
            i += 1
print(next_hack(99))
