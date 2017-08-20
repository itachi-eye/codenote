def euclid(a, b):
    """
    欧几里得辗转相除法
    """
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    euclid(1000, 128)
