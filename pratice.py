# Define Student class
class Student:
    # Define constructor
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
    
    def toString(self):
        return f"Name: {self.name} CGPA: {self.cgpa}"
    
# Create a Node class
class Node:
    # Define constructor
    def __init__(self, student, next=None, pre=None):
        self.data = student 
        self.next = next
        self.pre = pre 

class LinkedList:
    # Define constructor
    def __init__(self):
        self.front = None
        self.back = None
    
    # Define push_front method
    def push_front(self, data):
        node = Node(data, self.front)

        # Check if the list is empty or not, set the self.back to the new node
        if self.front is None:
            self.back = node
        else:
            # If the list is not empty then set the current front node to the new node
            self.front.pre = node

        # After that then set the self.front to the new node
        self.front = node

    def push_back(self, data):
        node = Node(data, None, self.back)

        # Check if the list is empty or not,
        if self.front is None:
            self.front = node
        else:
            self.back.next = node
    
        self.back = node


    
    def display_front(self):
        current = self.front

        while current is not None:
            print(current.data.toString())
            current = current.next
    
    def display_back(self):
        current = self.back

        while current is not None:
            print(current.data.toString())
            current = current.pre

lsk = LinkedList()
lsk.push_back(Student("Bill", 3.2))
lsk.push_back(Student("Toni798", 3.2))
lsk.push_back(Student("John", 3.2))
lsk.display_front()

print("\n ------------\n")

lsk.display_back()

        
        

     