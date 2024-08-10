class Node:
    def __init__(self,data):
        self.data =data
        self.pointer=None

class LinkedList:
    def __init__(self):
        self.head=None

    def adding(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return

        current=self.head
        while current.pointer:
            current=current.pointer
        current.pointer=newnode

    def display(self):
        current=self.head
        while current:
            print(current.data,end="--->" if current.pointer else "\n")
            current= current.pointer

ll = LinkedList()
ll.adding(10)
ll.adding(20)
ll.adding(30)
ll.display()

