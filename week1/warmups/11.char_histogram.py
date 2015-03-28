def char_histogram(string):
    list_str = list(string)
    dict = {}
    for i in list_str:
        dict[i] = list_str.count(i)
    return dict
print(char_histogram("aaab!B"))
