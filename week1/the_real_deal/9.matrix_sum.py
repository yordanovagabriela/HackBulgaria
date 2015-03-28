def sum_matrix(m):
    sum = 0
    for row in m:
        for elm in row:
            sum = sum + elm
    return sum
print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
