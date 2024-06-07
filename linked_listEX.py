# Searching and Linked List

# Create A LinkedList with node class
class LinkedList:
    class Node:
        # Node Constructor
        def __init__(self, data, next=None, pre=None):
            self.data = data
            self.next = next
            self.pre = pre


     # Linked List Constructor   
    def __init__(self):
        self.front = self.Node(None)
        self.back = self.Node(None, None.self.front)
        self.front.next = self.back

    def push_front(self, data):
        node = self.Node(data, self.front.next, self.front)
        self.front.next.pre = node
        self.front.next = node

    def display(self):
        current = self.front 

        while current is not None:
            print(current.data)
            current = current.next

lst = LinkedList()
lst.push_front(2)
lst.push_front(5)
lst.push_front(1)
lst.push_front(3)
lst.push_front(7)
lst.display()





    
