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
print(group([1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5]))
