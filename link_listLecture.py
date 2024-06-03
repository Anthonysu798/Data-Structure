class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def toString(self):
        return "Name " + self.name + " " + str(self.cgpa)


class Node:
    def __init__(self, student, next=None, pre=None):
        self.data = student
        self.next = next
        self.pre = pre


class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def push_front(self, data):
        node = Node(data, self.front)

        if self.front is None:
            self.back = node
        else:
            self.front.pre = node

        self.front = node

    def push_back(self, data):
        node = Node(data, None, self.back)

        # Check if sometime in the link list or not
        if self.back is None:
            self.front = node
        else:
            self.back.next = node
        
        self.back = node

    def pop_front(self):
        if self.front is None:
            print("Linked List is empty")
            return
        # Check if there is only one element in the linked list
        elif self.front == self.back:
            # Remove the only element in the linked list
            rm = self.front
            # Set the front and back to None
            self.front = self.back = None
            del rm
        else:
            rm = self.front
            self.front = self.front.next
            self.front.pre = None
            del rm 
    
    def pop_back(self):
        # Check the edge cases
        if self.back is None:
            print("Linked List is empty")
            return 
        # Check if there is only one element in the linked list
        elif self.front == self.back:
            # Remove the only element in the linked list
            rm = self.back
            # Set the front and back to None
            self.front = self.back = None
            del rm
        else:
            rm = self.back # point to which node we want to remove 
            self.back = self.back.pre
            self.back.next = None
            del rm

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

    # Return number of nodes in the linked list
    def length(self):
        current = self.front
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count
    
    def search_by_name(self, name):
        # return -1 if student not found
        current = self.front
        index = 0
        while current is not None:
            if current.data.name == name:
                return index
            index += 1
            current = current.next
        return -1
    
    def get_max_cgpa(self):
        pass

    def get_avg_cgpa(self):
        pass
            
            
        

        
    



lsk = LinkedList()
lsk.push_front(Student("John", 3.5))
lsk.push_front(Student("Steve", 3.8))
lsk.push_front(Student("Bill", 3.2))
lsk.display_front()

# Call the length method
print("\nLength of the linked list is: ", lsk.length())


lsk.pop_back()
print("\nAfter Removal\n")
lsk.display_front()

# Call the length method
print("\nLength of the linked list is: ", lsk.length())

# Call the search_by_name method
print("\nSearch by name at index : ", lsk.search_by_name("Steve"))



