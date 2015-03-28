def count_words(arr):
    result = {}
    for i in arr:
        result[i] = arr.count(i)
    return result
print(count_words([1, 1, 1, "a", "a", "b"]))
