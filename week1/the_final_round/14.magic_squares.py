def magic_square(matrix):
    left_diag = 0
    right_diag =0
    rows = [0 for i in range(len(matrix))]
    cols = [0 for i in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                left_diag += matrix[row][col]
            if row + col == len(matrix) -1:
                right_diag += matrix[row][col]
            cols[col] += matrix[col][row]
        rows[row] = sum(matrix[row])
    if left_diag != right_diag:
        return False
    if set(rows) == set(cols):
        return True
    else:
        return False

print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
