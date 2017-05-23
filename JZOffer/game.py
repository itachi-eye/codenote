def dice(n):
    """
    投掷n个骰子，和为[n, 6n]，求每种可能出现的次数
    动态分布：
    f(n, s)表示：n个骰子、和为s的出现次数
    f(n+1, s)表示：再投一个骰子、和为s的次数，
    再投的一个骰子可能出现1-6，
    故，f(n+1, s) = f(n, s-1) + f(n, s-2) + ... + f(n, s-6)
    """
    rst = [0] * (6 * n + 1)
    tmp = [0] * (6 * n + 1)
    for i in range(1, 7):
        tmp[i] = 1
    for m in range(2, n + 1):
        for s in range(m, 6 * m + 1):
            a = 0
            for i in range(1, 7):
                if s - i > 0:
                    a += tmp[s - i]
            rst[s] = a
        rst[:m] = [0] * m
        rst, tmp = tmp, rst
    print(tmp[n:])


if __name__ == '__main__':
    dice(10)
