class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args[0], args[1]
        elif len(args) == 1:
            x, y = args[0][0], args[0][1]
        else:
            x, y = 0, 0
        super().__init__(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint" + str(self)

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


first_point = second_point = PatchedPoint((2, -7))
print(first_point)
first_point += (7, 3)
print(first_point)
print(first_point, second_point, first_point is second_point)
