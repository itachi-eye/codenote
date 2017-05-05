"""
顺时针，逆时针打印正方形、三角形
"""
N = 10
matrix = [[0] * N for _ in range(N)]


def to_right(x, y, st):
    while y < N and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        y += 1
    return x, y - 1, st


def to_down(x, y, st):
    while x < N and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x += 1
    return x - 1, y, st


def to_left(x, y, st):
    while y >= 0 and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        y -= 1
    return x, y + 1, st


def to_up(x, y, st):
    while x >= 0 and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x -= 1
    return x + 1, y, st


def to_right_up(x, y, st):
    while x > -1 and y < N and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x -= 1
        y += 1
    return x + 1, y - 1, st


def to_right_down(x, y, st):
    while x < N and y < N and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x += 1
        y += 1
    return x - 1, y - 1, st


def to_left_up(x, y, st):
    while x > -1 and y > -1 and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x -= 1
        y -= 1
    return x + 1, y + 1, st


def to_left_down(x, y, st):
    while x < N and y > -1 and matrix[x][y] == 0:
        matrix[x][y] = st
        st += 1
        x += 1
        y -= 1
    return x - 1, y + 1, st


def clockwise_matrix():
    x, y, st = 0, -1, 1
    while True:
        x, y, st = to_right(x, y + 1, st)
        x, y, st = to_down(x + 1, y, st)
        x, y, st = to_left(x, y - 1, st)
        x, y, st = to_up(x - 1, y, st)
        if st > N * N:
            break
    for row in matrix:
        print(row)


def anticlockwise_matrix():
    x, y, st = -1, 0, 1
    while True:
        x, y, st = to_down(x + 1, y, st)
        x, y, st = to_right(x, y + 1, st)
        x, y, st = to_up(x - 1, y, st)
        x, y, st = to_left(x, y - 1, st)
        if st > N * N:
            break
    for row in matrix:
        print(row)


def left_lower_triangular_matrix():
    x, y, st = -1, 0, 1
    while True:
        x, y, st = to_down(x + 1, y, st)
        x, y, st = to_right(x, y + 1, st)
        x, y, st = to_left_up(x - 1, y - 1, st)
        if st > (N * (N + 1) >> 1):
            break
    for row in matrix:
        for d in row:
            if d != 0:
                print("%5d" % d, end='')
        print()


def upper_triangular_matrix():
    x, y, st = 0, N, 1
    while True:
        x, y, st = to_left(x, y - 1, st)
        x, y, st = to_right_down(x + 1, y + 1, st)
        x, y, st = to_up(x - 1, y, st)
        if st > (N * (N + 1) >> 1):
            break
    for row in matrix:
        for d in row:
            if d != 0:
                print("%5d" % d, end='')
            else:
                print("%5s" % '', end='')
        print()


if __name__ == '__main__':
    upper_triangular_matrix()
