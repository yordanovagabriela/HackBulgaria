def count_vowels(str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in list(str):
            if char.lower() in vowels:
                count = count+1
    return count
print(count_vowels("grrrrgh!"))
