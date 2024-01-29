class Stack:
    def __init__(self):
        self.mass = []

    def push(self, obj):
        self.mass.append(obj)

    def pop(self):
        a = self.mass.pop()
        return a

    def is_empty(self):
        return True if len(self.mass) == 0 else False


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
