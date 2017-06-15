def Euclid_gcd(a, b):
    if a == b or b == 1:
        return b
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


def Euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = Euclid_ext(b, a % b)
    return d, y, x - (a // b) * y


if __name__ == '__main__':
    print(Euclid_ext(1008, 120))
