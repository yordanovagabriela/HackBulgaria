def unique_words(arr):
    sum = 0
    for i in arr:
        if arr.count(i) == 1:
            sum += 1
    return sum
print(unique_words([1, 2, 3, 3, 4, 5]))
