def separate_func(x) -> bool:
    return True if x % 3 else False


def separate_odd_and_even(arr: list):
    """
    将数组奇数在前，偶数在后，不考虑顺序，
    时间O(n)，空间O(1)
    """
    i, j = 0, len(arr) - 1
    while i < j:
        while i < j and separate_func(arr[i]):
            i += 1
        while i < j and not separate_func(arr[j]):
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def _rotate(arr, s, r):
    while s < r:
        arr[s], arr[r] = arr[r], arr[s]
        s += 1
        r -= 1


def _merge(arr, s, m, r):
    i, j = s, m + 1
    while i <= m and separate_func(arr[i]):
        i += 1
    while j <= r and separate_func(arr[j]):
        j += 1
    _rotate(arr, i, j - 1)
    _rotate(arr, i, i + j - m - 2)
    _rotate(arr, i + j - m - 1, j - 1)


def recv_separate(arr, s, r):
    """
    归并法，将数组奇数在前，偶数在后，相对位置不变
    时间O(nlgn)，空间O(1)
    """
    if s < r:
        m = (s + r) >> 1
        recv_separate(arr, s, m)
        recv_separate(arr, m + 1, r)
        _merge(arr, s, m, r)


if __name__ == '__main__':
    a = [5, 2, 1, 3, 4, 69, 6, 8]
    recv_separate(a, 0, len(a) - 1)
    print(a)
