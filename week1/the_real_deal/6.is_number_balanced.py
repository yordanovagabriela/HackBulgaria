def is_balanced(n):
    digits=[int(i) for i in str(n)]
    size=len(list(digits))
    if size%2!=0:
        return sum(digits[0:size//2])==sum(digits[size//2+1:size])
    else:
        return sum(digits[0:size//2])==sum(digits[size//2:size])
print(is_balanced(1238033))
