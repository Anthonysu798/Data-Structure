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
        self.front = None
        self.back = None

    def push_front(self, data):
        # Create the first Node
        node = self.Node(data, self.front)

        # When linked list is empty
        # In case of the first node, both front and back will point to the same node
        if self.front is None:
            self.back = node 
        # If we already have some nodes
        else: 
            self.front.pre = node
        
        self.front = node
    
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





    
