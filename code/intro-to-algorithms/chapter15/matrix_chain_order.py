"""
矩阵链乘法
"""
from pprint import pprint


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * len(p) for _ in range(len(p))]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    pprint(m)


if __name__ == '__main__':
    p = (30, 35, 15, 5, 10, 20, 25)

    matrix_chain_order(p)
