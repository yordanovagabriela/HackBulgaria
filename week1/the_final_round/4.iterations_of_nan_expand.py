def iterations_of_nan_expand(expanded):
    list_nan = expanded.split()
    n = 0
    a = 0
    if not list_nan or list_nan[0] != 'Not' or list_nan[len(list_nan) - 1] != "NaN":
        return(False)
    for i in list_nan:
        if i == "a":
            a = a + 1
        elif i == "Not":
            n = n + 1
        elif i != list_nan[len(list_nan) - 1]:
            return(False)
    if a == n:
        return n
    else:
        return False
print(iterations_of_nan_expand("Not a bf NaN"))
