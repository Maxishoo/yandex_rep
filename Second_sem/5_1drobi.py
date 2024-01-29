class Fraction:
    def __init__(self, *args):
        self.num = 1
        self.dem = 1
        if len(args) == 1:
            if type(args[0]) is int:
                self.num, self.dem = args[0], 1
            else:
                if '/' in args[0]:
                    a = args[0].split('/')
                    self.num, self.dem = int(a[0]), int(a[1])
                else:
                    self.num, self.dem = int(args[0]), 1
        elif len(args) == 2:
            self.num, self.dem = args[0], args[1]
        self._reducer()

    def _reducer(self):
        a, b = self.num, self.dem
        znak = a // abs(a) * b // abs(b)
        a, b = abs(a), abs(b)
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        self.num = abs(self.num) // a * znak
        self.dem = abs(self.dem) // a

    def numerator(self, number=None):
        if number:
            self.num = abs(number) * ((self.num // abs(self.num)) * (number // abs(number)))
            self._reducer()
        return abs(self.num)

    def denominator(self, number=None):
        if number:
            self.dem = number
            self._reducer()
        return self.dem

    def __neg__(self):
        return Fraction(-1 * self.num, self.dem)

    def __str__(self):
        return f"{self.num}/{self.dem}"

    def __repr__(self):
        return f"Fraction(" + "'" + f"{self.num}/{self.dem}" + "')"

    def __add__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.dem + self.dem * other.num, self.dem * other.dem)

    def __iadd__(self, other):
        if type(other) is int:
            other = Fraction(other)
        self.num = self.num * other.dem + self.dem * other.num
        self.dem = self.dem * other.dem
        self._reducer()
        return self

    def __sub__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.dem - self.dem * other.num, self.dem * other.dem)

    def __isub__(self, other):
        if type(other) is int:
            other = Fraction(other)
        self.num = self.num * other.dem - self.dem * other.num
        self.dem = self.dem * other.dem
        self._reducer()
        return self

    def __mul__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.num, self.dem * other.dem)

    def __imul__(self, other):
        if type(other) is int:
            other = Fraction(other)
        self.num = self.num * other.num
        self.dem = self.dem * other.dem
        self._reducer()
        return self

    def __truediv__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.dem, self.dem * other.num)

    def __itruediv__(self, other):
        if type(other) is int:
            other = Fraction(other)
        self.num = self.num * other.dem
        self.dem = self.dem * other.num
        self._reducer()
        return self

    def reverse(self):

        return Fraction(self.dem, self.num)

    def __lt__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 < n2 else False

    def __le__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 <= n2 else False

    def __gt__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 > n2 else False

    def __ge__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 >= n2 else False

    def __eq__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 == n2 else False

    def __ne__(self, other):
        if type(other) is int:
            other = Fraction(other)
        n1 = self.num * other.dem
        n2 = self.dem * other.num
        return True if n1 != n2 else False

    def __radd__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.dem + self.dem * other.num, self.dem * other.dem)

    def __rsub__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.dem * other.num - self.num * other.dem, self.dem * other.dem)

    def __rmul__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.num * other.num, self.dem * other.dem)

    def __rtruediv__(self, other):
        if type(other) is int:
            other = Fraction(other)
        return Fraction(self.dem * other.num, self.num * other.dem)


a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (3 - a, 2 / b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
