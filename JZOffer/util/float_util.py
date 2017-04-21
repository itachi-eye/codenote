e = 1.0E-10


def fequal(a, b):
    if -1.0 * e <= a - b <= e:
        return True
    else:
        return False


def fcompare(a: float, b: float):
    d = a - b
    if d > e:
        return 1
    elif d < -1.0 * e:
        return -1
    else:
        return 0
