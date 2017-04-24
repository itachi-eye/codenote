def odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def not_divided(n):
    return lambda x: x % n > 0


def prime_gnt():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divided(n), it)


def z_iter():
    n = 1
    while True:
        n += 1
        yield n


def ugly_gnt():
    zit = z_iter()
    z = next(zit)
    while z < 7:
        yield z
        z = next(zit)
    primes = prime_gnt()
    p = next(primes)
    while p < 7:
        p = next(primes)
    while True:
        if z == p:
            zit = filter(not_divided(p), zit)
            z = next(zit)
            p = next(primes)
        else:
            yield z
            z = next(zit)


def ugly_array(n: int):
    arr = [0] * n
    arr[0] = 2
    arr[1] = 3
    arr[2] = 4
    arr[3] = 5
    p1, p2, p3 = 0, 0, 0
    for i in range(4, n):
        m = arr[i - 1]
        for j in range(i):
            p1 = 2 * arr[j]
            if p1 > m:
                break
        for j in range(i):
            p2 = 3 * arr[j]
            if p2 > m:
                break
        for j in range(i):
            p3 = 5 * arr[j]
            if p3 > m:
                break
        arr[i] = min(p1, p2, p3)
    print(arr)


if __name__ == '__main__':
    ugly_array(1500)
