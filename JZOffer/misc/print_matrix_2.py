"""
顺时针，逆时针打印正方形、三角形
"""
N = 5
matrix = [[0] * N for _ in range(N)]


class Point(object):
    def __init__(self, x=0, y=0, val=1):
        self.x = x
        self.y = y
        self.val = val


def to_right(p: Point):
    while p.y < N and matrix[p.x][p.y] == 0:
        matrix[p.x][p.y] = p.val
        p.val += 1
        p.y += 1
    p.y -= 1


def to_left(p: Point):
    while p.y >= 0 and matrix[p.x][p.y] == 0:
        matrix[p.x][p.y] = p.val
        p.val += 1
        p.y -= 1
    p.y += 1


def to_down(p: Point):
    while p.x < N and matrix[p.x][p.y] == 0:
        matrix[p.x][p.y] = p.val
        p.val += 1
        p.x += 1
    p.x -= 1


def to_up(p: Point):
    while p.x >= 0 and matrix[p.x][p.y] == 0:
        matrix[p.x][p.y] = p.val
        p.val += 1
        p.x -= 1
    p.x += 1


def clockwise_matrix():
    p = Point(0, -1, 1)
    while True:
        p.y += 1
        to_right(p)
        p.x += 1
        to_down(p)
        p.y -= 1
        to_left(p)
        p.x -= 1
        to_up(p)
        if p.val > N * N:
            break
    for row in matrix:
        print(row)


if __name__ == '__main__':
    clockwise_matrix()
