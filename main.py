import math


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        if denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        if isinstance(other, Fraction):
            lcm = math.lcm(self.denominator, other.denominator)
            return Fraction(self.numerator * lcm // self.denominator + other.numerator * lcm // other.denominator, lcm)
        raise TypeError("operation should be performed with int or fraction")

    def __sub__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator - other * self.denominator, self.denominator)
        if isinstance(other, Fraction):
            lcm = math.lcm(self.denominator, other.denominator)
            return Fraction(self.numerator * lcm // self.denominator - other.numerator * lcm // other.denominator, lcm)
        raise TypeError("operation should be performed with int or fraction")

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        raise TypeError("operation should be performed with int or fraction")

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        raise TypeError("operation should be performed with int or fraction")

    def __pow__(self, power, modulo=None):
        if not isinstance(power, int):
            raise TypeError("power operation should be performed with int")
        return Fraction(self.numerator ** power, self.denominator ** power)

    def simplify(self):
        gcd = math.gcd(abs(self.numerator), self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def decimalize(self):
        return self.numerator / self.denominator


if __name__ == "__main__":
    print(Fraction(3, 4))
    print(Fraction(3, -4))
    print(Fraction(2, 3) + 2)
    print(Fraction(1, 3) + Fraction(3, 4))
    print(Fraction(2, 3) - 2)
    print(Fraction(1, 3) - Fraction(3, 4))
    print(Fraction(7, 8) * Fraction(4, 3))
    print(Fraction(7, 8) / Fraction(4, 3))
    print(Fraction(3, 5) ** 3)
    print(Fraction(8, 6).simplify())
    print(Fraction(8, 6).decimalize())