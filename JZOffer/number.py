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


def first_single_character(seq):
    """
    第一次出现一次的字符
    """
    charr = [0] * 256
    for c in seq:
        charr[ord(c)] += 1
    for i in range(256):
        if charr[i] == 1:
            print(chr(i))
            break


def del_character_in_second(first: str, second: str):
    """
    删除first中second有的字符
    """
    lst = list(first)
    aux = [0] * 256
    for s in second:
        aux[ord(s)] = 1
    for i in range(len(lst)):
        c = first[i]
        if aux[ord(c)] == 1:
            lst[i] = '\0'
    print(''.join(filter(lambda x: x != '\0', lst)))


def inverse_pairs_count_0(arr):
    """
    逆序对的个数
    """
    lth = len(arr)
    cnt = 0
    for i in range(lth):
        for j in range(i + 1, lth):
            if arr[i] > arr[j]:
                cnt += 1
    print(cnt)


def recv_merge(arr, tmp, st, m, end):
    """
    求st-m，m-end的交叉逆序对数，同时将前后段排序
    """
    i, j = st, m + 1
    idx, cnt = st, 0
    while i <= m and j <= end:
        if arr[i] > arr[j]:
            tmp[idx] = arr[j]
            cnt += m - i + 1
            j += 1
        else:
            tmp[idx] = arr[i]
            i += 1
        idx += 1
    while i <= m:
        tmp[idx] = arr[i]
        idx += 1
        i += 1
    while j <= end:
        tmp[idx] = arr[j]
        idx += 1
        j += 1
    print(tmp)
    arr[st:end + 1] = tmp[st: end + 1]
    return cnt


def recv_inverse_pairs(arr, tmp, st, end):
    """
    归并法，分治-合并
    :param arr: 原数组
    :param tmp: 辅助数组
    :param st: 开始位置
    :param end: 结束位置
    :return: st-end段的逆序对数
    """

    if st == end:
        return 0
    else:
        m = (st + end) >> 1
        left = recv_inverse_pairs(arr, tmp, st, m)  # 前半段
        right = recv_inverse_pairs(arr, tmp, m + 1, end)  # 后半段
        inter = recv_merge(arr, tmp, st, m, end)  # 前后段
        return left + right + inter


def inverse_pairs_count_1(arr):
    """
    逆序对的个数，归并法，空间换时间
    时间复杂度O(nlgn)
    空间复杂度O(n)
    """
    tmp = [0] * len(arr)
    count = recv_inverse_pairs(arr, tmp, 0, len(arr) - 1)
    print(count)


if __name__ == '__main__':
    inverse_pairs_count_0([7, 5, 6, 4, 2, 3])
    inverse_pairs_count_1([7, 5, 6, 4, 2, 3])
