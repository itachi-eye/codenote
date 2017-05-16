"""
幂次法则，k越大，Pk越小，而且是幂次减小
"""

import random

p = 1 / 4
MaxCount = 32


def power_low():
    """
    幂次法则，Pk = (1-p)p^(k-1)
    random<p的概率是p，大于p的概率是1-p，Pk即前面k-1次都小于p，直到大于p停止
    """
    c = 1
    while random.random() < p and c < MaxCount:
        c += 1
    return c


def geometric_distribution():
    """
    几何分布，Pk = p(1-p)^(k-1)
    random<p的概率是p，大于p的概率是1-p，Pk即前面k-1次都是大于p，直到小于p停止
    """
    c = 1
    while random.random() > p and c < 10:
        c += 1
    return c


if __name__ == '__main__':
    arr = [0] * (MaxCount + 1)
    for i in range(10000):
        arr[power_low()] += 1
    print(arr)
