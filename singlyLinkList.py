class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# Print only even number
def print_even(head):
    current = head
    while current is not None:
        if current.data % 2 == 0:
            print(current.data)
        current = current.next

def inser_after(head, value, data):
    current = head

    while current is not None:
        if current.data == value: # If the value is found then insert the data after the value node
            new_node = Node(data) # Create a new node
            new_node.next = current.next  # Point the current next to the new node next
            current.next = new_node # Point the new node to the current next
        current = current.next # Keep on searching for the value in the linked list

# First Node created
head = Node(2)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(6)

inser_after(head, 3, 8)

print_list(head)
