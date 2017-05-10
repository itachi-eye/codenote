def is_post(seq):
    """
    判断是否是平衡二叉树的后序遍历
    """
    return _recv_is_post(seq, 0, len(seq) - 1)


def _recv_is_post(seq, p, r):
    if p < r:
        x = seq[r]
        i = p
        while i < r and seq[i] < x:
            i += 1
        j = i - 1
        while i < r:
            if seq[i] <= x:
                return False
            i += 1
        return _recv_is_post(seq, p, j) and _recv_is_post(seq, j + 1, r - 1)
    else:
        return True


if __name__ == '__main__':
    print(is_post([5, 7, 6, 9, 11, 10, 8]))
