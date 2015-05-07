from matrix_sum import sum_matrix


import copy


NEIGHBOURS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def is_neighbour(m, position):
    if position[0] < 0 or position[1] >= len(m):
        return False

    if position[1] < 0 or position[1] >= len(m[0]):
        return False
    return True


def bomb(m, at):
    if not is_neighbour(m, at):
        return m

    target = m[at[0]][at[1]]

    for position in NEIGHBOURS:
        position = (position[0] + at[0], position[1] + at[1])
        if is_neighbour(m, position):
            if m[position[0]][position[1]] - target < 0:
                m[position[0]][position[1]] = 0
            else:
                m[position[0]][position[1]] -= target
    return m


def matrix_bombing_plan(m):
    plan = {}
    for row in range(0, len(m)):
        for column in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (row, column))
            plan[(row, column)] = sum_matrix(bombed)

    return plan
