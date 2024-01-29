class Rectangle:
    def __init__(self, left, right):
        self.xy1 = (min(left[0], right[0]), min(left[1], right[1]))
        self.xy2 = (max(left[0], right[0]), max(left[1], right[1]))

    def perimeter(self):
        st1 = abs(self.xy1[0] - self.xy2[0])
        st2 = abs(self.xy1[1] - self.xy2[1])
        return round(2 * st1 + 2 * st2, 2)

    def area(self):
        st1 = abs(self.xy1[0] - self.xy2[0])
        st2 = abs(self.xy1[1] - self.xy2[1])
        return round(st1 * st2, 2)

    def get_pos(self):
        return round(self.xy1[0], 2), round(self.xy2[1], 2)

    def get_size(self):
        st1 = abs(self.xy1[0] - self.xy2[0])
        st2 = abs(self.xy1[1] - self.xy2[1])
        return round(st1, 2), round(st2, 2)

    def move(self, dx, dy):
        self.xy1 = (self.xy1[0] + dx, self.xy1[1] + dy)
        self.xy2 = (self.xy2[0] + dx, self.xy2[1] + dy)

    def resize(self, width, height):
        lengl = self.get_pos()
        self.xy1 = (lengl[0], lengl[1] - height)
        self.xy2 = (lengl[0] + width, lengl[1])

    def turn(self):
        coords = self.get_size()
        center = ((self.xy1[0] + self.xy2[0]) / 2, (self.xy1[1] + self.xy2[1]) / 2)
        self.xy1 = (round(center[0] - coords[1] / 2, 2), round(center[1] - coords[0] / 2, 2))
        self.xy2 = (round(center[0] + coords[1] / 2, 2), round(center[1] + coords[0] / 2, 2))

    def scale(self, factor=1):
        coords = self.get_size()
        center = (self.xy1[0] + self.xy2[0]) / 2, (self.xy1[1] + self.xy2[1]) / 2
        self.xy1 = (center[0] - coords[0] * factor / 2, center[1] - coords[1] * factor / 2)
        self.xy2 = (center[0] + coords[0] * factor / 2, center[1] + coords[1] * factor / 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.area(), sep='\n')
rect.turn()
rect.scale(4)
print(rect.get_pos(), rect.area(), sep='\n')
