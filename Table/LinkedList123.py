class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add(self, data):
        new_node = Node(data)
        new_node.nex = self.head
        self.head = new_node

    def add_back()

LL1 = LinkedList()
LL1.add(10)
LL1.print_LinkedList()
