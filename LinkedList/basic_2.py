class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addlist(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def printer(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.pointer

# Example Usage
linkedlist = LinkedList()
linkedlist.addlist(10)
linkedlist.addlist(9)
linkedlist.addlist(8)
linkedlist.addlist(7)
linkedlist.printer()  # Output: 10 9 8 7
