"""
动态规划

问题：
    钢条切割，求最大收益

递推式:
    r{n} = max(p{i}, r{n-i}), i = 1->n
"""


def cut_rod(p, n):
    """
    递归实现
    时间复杂度：
        O(2^n)
    """
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def cut_rod_dp(p, n):
    """
    利用数组记录之前算过的最大收益，避免重复计算
    时间复杂度：
        O(n^2)
    空间复杂度：
        O(n)
    """
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        q = 0
        for j in range(1, i + 1):
            q = max(q, p[j] + r[i - j])
        r[i] = q
    return r[n]


def cut_rod_dp_exp(p, n):
    """
    类似上面的dp算法，区别是返回两个数组：
        r：最大收益数组
        s：对应的第一段的长度
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        q, a = 0, 0
        for j in range(1, i + 1):
            t = p[j] + r[i - j]
            if q < t:
                q = t  # 赋予q较大值
                a = j  # 对应最大收益的第一段，最短的那段
        r[i], s[i] = q, a
    return r, s


def cut_rod_dp_print(p, n):
    """
    重构一个解
    """
    r, s = cut_rod_dp_exp(p, n)
    solu = []
    while n > 0:
        solu.append(s[n])
        n -= s[n]
    return solu


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    solution = cut_rod_dp_print(price, 5)
    print(solution)
