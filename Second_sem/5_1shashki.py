class Checkers:
    def __init__(self):
        self.doska = []
        for i in range(8):
            a = []
            for j in range(8):
                if j < 3:
                    if (i + j) % 2 != 0:
                        a.append(Cell("X"))
                    else:
                        a.append(Cell("W"))
                elif j > 4:
                    if (i + j) % 2 != 0:
                        a.append(Cell("X"))
                    else:
                        a.append(Cell("B"))
                else:
                    a.append(Cell("X"))
            self.doska.append(a)

    def ind_coord(self, pos):
        p = ord(pos[0]) - ord('A')
        q = int(pos[1])
        return p, q - 1

    def move(self, f, t):
        p1 = self.ind_coord(f)
        p2 = self.ind_coord(t)
        self.doska[p2[0]][p2[1]].sost = self.doska[p1[0]][p1[1]].sost
        self.doska[p1[0]][p1[1]].sost = "X"

    def get_cell(self, p):
        p1 = self.ind_coord(p)
        return self.doska[p1[0]][p1[1]]


class Cell:
    def __init__(self, st):
        self.sost = st

    def status(self):
        return self.sost


# checkers = Checkers()

checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
