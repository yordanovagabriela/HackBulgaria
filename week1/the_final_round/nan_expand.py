def nan_expand(times):
    if times != 0:
        text = " Not a " * times + "NaN "
        return (" \"%s\" " % text)
    else:
        return " \"\""
print(nan_expand(0))
