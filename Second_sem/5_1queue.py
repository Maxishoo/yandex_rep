class Queue:
    def __init__(self):
        self.mass = []

    def push(self, obj):
        self.mass.append(obj)

    def pop(self):
        a = self.mass.pop(0)
        return a

    def is_empty(self):
        return True if len(self.mass) == 0 else False

