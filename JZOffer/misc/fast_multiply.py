from util.float_util import fequal


def power(a, n: int):
    if fequal(a, 0):
        if n <= 0:
            return float('nan')
        else:
            return 0.0
    if fequal(a, 1.0) or n == 0:
        return 1.0
    if n < 0:
        return 1.0 / _fast_power(a, -n)
    else:
        return _fast_power(a, n)


def _fast_power(a: float, n: int) -> float:
    rst = a if n & 1 else 1
    t = a ** 2
    n >>= 1
    while n:
        if n & 1:
            rst *= t
        t **= 2
        n >>= 1
    return rst


def fact_matrix(n):
    """
    阶乘的lgn解法
    """
    C = [[1, 1], [1, 0]]
    rst = [[1, 0], [0, 1]]
    if n & 1:
        rst = C.copy()
    t = [[2, 1], [1, 1]]
    n >>= 1
    while n:
        if n & 1:
            rst = _m(rst, t)
        t = _m(t, t)
        n >>= 1
    print(rst)


def _m(A, B):
    rst = [[0, 0], [0, 0]]
    rst[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    rst[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    rst[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    rst[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return rst


if __name__ == '__main__':
    print(fact_matrix(1000))
