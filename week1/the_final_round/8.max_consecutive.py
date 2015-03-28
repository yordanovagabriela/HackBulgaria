def group(lst):
    op = []
    result = []
    op.append(lst[0])
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i + 1]:
            op.append(lst[i])
        else:
            result.append(op)
            op = []
            op.append(lst[i + 1])
    result.append(op)
    return result


def max_consecutive(seq):
    return max(len(l) for l in group(seq))
print(max_consecutive([1, 1, 1, 1, 2, 3]))
