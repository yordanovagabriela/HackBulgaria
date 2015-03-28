def is_decreasing(seq):
    return seq==sorted(seq, reverse=True)
print(is_decreasing([5,4,3,1]))
