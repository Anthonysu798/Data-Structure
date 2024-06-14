class Node:
    def __init__ (self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next
    
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert at the back
    def add_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            # If current.next is None or empty then assigned the new_node to the current.next
            current.next = new_node
                


LL1 = LinkedList()
LL1.add_back(100)

LL1.print_LinkedList()