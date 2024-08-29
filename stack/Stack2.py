class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self,items):
        self.top += 1
        if len(self.items) <= self.top:
            self.items.append(None)
        self.items[self.top] = items

    def pop (self):
        if not self.is_empty():
            items =self.items[self.top]
            self.top -= 1
            return items
        else:
            print("Empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]


    def is_empty(self):
        return self.top == -1

    def size(self):
        size=self.top+1
        return size

    def display(self):
        print("Displaying stack")
        for i in range(self.top,-1,-1):
            print(self.items[i])


obj = Stack()
obj.push(10)
obj.push(5)
obj.push(2)
obj.push(205)
print("size -",obj.size())
print("Peek -",obj.peek())
print("Pop -",obj.pop())
print("size after pop  -",obj.size())

obj.display()
