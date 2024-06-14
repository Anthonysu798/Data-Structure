class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Creating the first Node
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)


# Define a function that print all the data in the LinkedList
def print_LinkedList(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next


# print_LinkedList(head)


# Define a function that only print even numbers in the LinkedList
def print_even(head):
    current = head

    while current is not None:
        if current.data % 2 == 0:
            print(current.data)
        current = current.next


# Define a function that only print odd numbers in the LinkedList
def odd_numbers(head):
    current = head

    while current is not None:
        if current.data % 2 != 0:
            print(current.data)
        current = current.next


# Insert after a function
def insert_after(head, value, data):
    current = head

    # Loop throught the Linked List to find the data if match then insert after
    while current is not None:
        if current.data == value:

            # Create a node node to insert
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next

insert_after(head, 3, 4)

print_LinkedList(head)

