def gcd(a: int, b: int) -> int:
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    if a < b:
        a, b = b, a
    r = 1
    while b != 0:
        if a & 1 == 0 and b & 1 == 0:
            r *= 2
            a >>= 1
            b >>= 1
        elif a & 1 == 0 and b & 1 == 1:
            while a & 1 == 0:
                a >>= 1
            if a < b:
                a, b = b, a
        elif a & 1 == 1 and b & 1 == 0:
            while b & 1 == 0:
                b >>= 1
        else:
            a, b = b, a - b
            if a < b:
                a, b = b, a
    return r * a


class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator
        g = gcd(self.numerator, self.denominator)
        if g > 1:
            self.numerator = self.numerator // g
            self.denominator = self.denominator // g
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self):
        if self.numerator == 0:
            return "0"
        else:
            return "{a}/{b}".format(a=self.numerator, b=self.denominator)

    def __add__(self, other):
        if type(other) == Fraction:
            num = self.numerator * other.denominator + self.denominator * other.numerator
            deno = self.denominator * other.denominator
            if num == 0:
                return Fraction()
            else:
                g = gcd(num, deno)
                return Fraction(num // g, deno // g)
        elif type(other) == int:
            num = self.numerator + self.denominator * other
            return Fraction(num, self.denominator)

    def __sub__(self, other):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        deno = self.denominator * other.denominator
        if num == 0:
            return Fraction()
        else:
            g = gcd(num, deno)
            return Fraction(num // g, deno // g)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        deno = self.denominator * other.denominator
        if num == 0:
            return Fraction()
        else:
            g = gcd(num, deno)
            return Fraction(num // g, deno // g)


def f(x):
    return x * x * x - x * x + x


if __name__ == '__main__':
    t = Fraction(1, 3)
    print(t + 3)
