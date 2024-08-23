class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        self.top += 1
        if len(self.items) <= self.top:
            self.items.append(None)
        self.items[self.top] = item

    def pop(self):
        if not self.is_empty():
            item = self.items[self.top]
            self.top -= 1
            return item
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def display(self):

        print("Stack (top to bottom):")
        for i in range(self.top, -1, -1):
            print(self.items[i])


stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)


print("Stack size:", stack.size())
stack.display()

print("Peek:", stack.peek())
print("Pop:", stack.pop())
#
stack.display()
