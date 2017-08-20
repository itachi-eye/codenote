"""
幂次法则，k越大，Pk越小，而且是幂次减小
"""

import random
import math

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


def normal_distribution():
    """
    近似正态分布，中心极限定理
    """
    x = sum(random.random() for _ in range(6))
    x = math.sqrt(2) * (x - 3)

    a = MaxCount >> 1
    y = int(a * x / 3 + a)
    if y < 1 or y > MaxCount:
        y = 0
    return y


def binomial_distribution():
    """
    二项分布，根据定义，重复试验n次中事件A出现的次数，
    其中，事件A出现的概率为p
    """
    c = 0
    for _ in range(MaxCount):
        if random.random() < p:
            c += 1
    return c


if __name__ == '__main__':
    pass
