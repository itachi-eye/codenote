from pprint import pprint

N = 9
su = [[0, 8, 4, 0, 0, 5, 0, 0, 0],
      [3, 0, 0, 0, 0, 9, 0, 6, 0],
      [1, 0, 0, 0, 8, 0, 9, 0, 0],

      [0, 0, 0, 7, 0, 6, 0, 1, 2],
      [0, 0, 3, 0, 0, 0, 4, 0, 0],
      [2, 1, 0, 9, 0, 8, 0, 0, 0],

      [0, 0, 1, 0, 7, 0, 0, 0, 3],
      [0, 4, 0, 8, 0, 0, 0, 0, 9],
      [0, 0, 0, 5, 0, 0, 6, 2, 0]]

trace = []


def check(i, j, n):
    if n in su[i]:  # check row
        return False
    for k in range(N):  # check column
        if su[k][j] == n:
            return False
    a = i // 3 * 3  # check block
    b = j // 3 * 3
    for x in [a, a + 1, a + 2]:
        for y in [b, b + 1, b + 2]:
            if su[x][y] == n:
                return False
    return True


def next_cell(i, j):
    j += 1
    if j == N:
        i += 1
        j = 0
    return i, j


r, c = 0, 0
while True:
    print(r, c)
    if r == 8 and c == 8:
        break
    if su[r][c] != 0:
        r, c = next_cell(r, c)
    else:
        has_one = False
        for a in range(1, N + 1):
            if check(r, c, a):
                has_one = True
                su[r][c] = a
                trace.append((r, c, a))
                r, c = next_cell(r, c)
                break
        if not has_one:
            while not has_one:
                r, c, a = trace.pop()
                for b in range(a + 1, N + 1):
                    if check(r, c, b):
                        has_one = True
                        su[r][c] = b
                        trace.append((r, c, b))
                        r, c = next_cell(r, c)
                        break
                if not has_one:
                    su[r][c] = 0

pprint(su)
