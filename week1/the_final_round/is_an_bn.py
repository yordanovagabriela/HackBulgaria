def is_an_bn(word):
    count = 0
    for i in word:
        if i != 'a' and i != 'b':
            return False
        if i != 'a':
            break
        else:
            count += 1
    if count == word.count('a') and count == word.count('b') and word:
        return True
    else:
        return False
print(is_an_bn("aaacbbb"))
