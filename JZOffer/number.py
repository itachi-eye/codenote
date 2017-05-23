import heapq


def more_than_half(arr: list):
    """
    超过一半的数
    """
    a, times = 0, 0
    for n in arr:
        if times == 0:
            a = n
            times = 1
        elif n == a:
            times += 1
        else:
            times -= 1
        print(n, a, times)


def partition(arr: list, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def median(arr):
    """
    中位数，待优化
    """
    lth = len(arr)
    middle = lth >> 1
    start, end = 0, lth - 1
    i = (arr, start, end)
    while i != middle:
        if i < middle:
            start = i + 1
        else:
            end = i - 1
        i = partition(arr, start, end)
    if lth & 1 == 0:
        start, end = 0, middle - 1
        i = partition(arr, start, end)
        while i != middle - 1:
            if i < middle - 1:
                start = i + 1
            else:
                end = i - 1
            i = partition(arr, start, end)
        return (arr[middle] + arr[middle - 1]) / 2
    else:
        return arr[middle]


def min_k_use_partition(arr, k):
    """
    数组中最小的k个数，使用partition，
    partition第k-1个位置，左边的都比第k-1个小，右边都大
    """
    start, end = 0, len(arr) - 1
    i = partition(arr, start, end)
    while i != k - 1:
        if i < k - 1:
            start = i + 1
        else:
            end = i - 1
        i = partition(arr, start, end)
    print(arr[:k])


def max_k_use_partition(arr, k):
    lth = len(arr)
    start, end = 0, lth - 1
    i = partition(arr, start, end)
    while i != lth - k:
        if i < lth - k:
            start = i + 1
        else:
            end = i - 1
        i = partition(arr, start, end)
    print(arr[-k:])


def min_k_use_heap(arr, k):
    # heapq.heapify(seq)
    print(heapq.nsmallest(k, arr))
    print(heapq.nlargest(k, arr))


def count_k(num, k):
    """
    1-num自然数中数字k的个数
    """
    t = 1
    cnt = 0
    while t <= num:
        h = num // t // 10
        c = num // t % 10
        l = num % t
        print(num, t, h, c, l)
        if h != 0:
            if c >= k:
                cnt += h * t + l + 1
            else:
                cnt += h * t
        else:
            if c > k:
                cnt += t
            elif c == k:
                cnt += l + 1
            else:
                pass
        print(cnt)
        t *= 10


def check_count_k(num, k):
    cnt = 0
    for n in range(1, num + 1):
        while n:
            if n % 10 == k:
                cnt += 1
            n //= 10
    print(cnt)


import functools


def cmp_func(m, n):
    """
    排序函数，比较拼接起来的两个数mn和nm的大小
    """
    return int(str(m) + str(n)) - int(str(n) + str(m))


def make_minimum_number(arr):
    """
    将数组arr中的数字组成一个最小的多位数
    """
    r = sorted(arr, key=functools.cmp_to_key(cmp_func))
    print(''.join(map(lambda x: str(x), r)))


if __name__ == '__main__':
    seq = [42, 45, 1, 39, 29]
    make_minimum_number(seq)
