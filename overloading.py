import math


class Rational:

    def __init__(self, a: int, b: int):
        if b == 0:
            raise ValueError
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)
        elif isinstance(other, int):
            return Rational(self.a + self.b * other, self.b)
        else:
            raise TypeError

    def __radd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        else:
            return Rational(self.a + self.b * other, self.b)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.a, other.b * self.b)
        elif isinstance(other, int):
            return Rational(self.a * other, self.b)
        else:
            raise TypeError

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        else:
            return Rational(self.a * other, self.b)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)
        elif isinstance(other, int):
            return Rational(self.a - self.b * other, self.b)
        else:
            raise TypeError

    def __rsub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        else:
            return Rational(self.a - self.b * other, self.b)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b, other.b * self.a)
        elif isinstance(other, int):
            return Rational(self.a, self.b * other)
        else:
            raise TypeError

    def __rtruediv__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        elif isinstance(other, int):
            return Rational(self.b, self.a * other)
        else:
            raise TypeError

    def __str__(self):
        tmp = math.gcd(self.a, self.b)
        self.a //= tmp
        self.b //= tmp
        if self.a == 0 or self.a / self.b == 0:
            return f"{self.a}"
        if self.b < 0 and self.a < 0:
            self.b *= -1
            self.a *= -1
        if self.b < 0:
            self.b = abs(self.b)
            self.a *= -1
        if self.b == 1:
            return f"{self.a}"
        elif abs(self.a / self.b).__round__() >= 1:
            return f"{(self.a / self.b).__round__()} + ({self.a - (((self.a / self.b).__round__()) * self.b)} / {self.b})"
        else:
            return f'{self.a} / {self.b}'


x = Rational(1, 1)
y = Rational(1, 4)
# z = x + y
# print(z)
print(x + y)
print(x + 1)
print(2 + x)
print(2 * x)
print(y - 2)
print(2 / x)
