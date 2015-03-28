def count_consonants(str):
    count = 0
    constants = "bcdfghjklmnpqrstvexz"
    for letter in list(str):
            if letter.lower() in constants:
                count = count + 1
    return count
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

