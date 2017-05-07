D = 10000
nlst = [0] * D
dlst = [0] * (D + 1)


def f(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def count():
    cnt = 0
    for d in range(2, D + 1):
        for n in range(1, d):
            g = f(n, d)
            n2 = n // g
            d2 = d // g
            if nlst[n2] != 0 and dlst[d2] != 0:
                continue
            else:
                cnt += 1
                nlst[n2] = n2
        dlst[d] = d
    return cnt


if __name__ == '__main__':
    print(count())
