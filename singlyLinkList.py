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
            break # Break after inserting the data
        current = current.next # Keep on searching for the value in the linked list

# Write a function that tell if the linked list is palindrome or not
# 1 -> 2 -> 3 -> 2 -> 1
def is_palindrome(head):
    current = head
    stack = []
    while current is not None:
        stack.append(current.data)
        current = current.next
    
    current = head
    while current is not None:
        if current.data != stack.pop():
            return False
        current = current.next
    return True
    


# First Node created
head = Node(2)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(6)

inser_after(head, 3, 8)


print(is_palindrome(head))

def get_max(numbers): # Recursion function
    if len(numbers) == 1:
        return numbers[0]
    else:
        m = get_max(numbers[1:]) # Recursion call to get the max number from the list of numbers starting from index 1 to the end of the list 

        if m > numbers[0]:
            return m
        else:
            return numbers[0]

    # Razi Solution
    # return get_max_helper(arr, 0, arr[0])
    # def get_max_helper(numbers, index, current_max):
    # if index == len(arr):
    #     return current_max 
    
    # if arr[index] > current_max:
    #     current_max = arr[index]

    # return get_max_helper(arr, index + 1, current_max)                      

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        # Use recursion to reverse the string
        return reverse_string(s[1:]) + s[0]
    
    # (s[1:]) + s[0] What is mean? 

print(get_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,15]))

def is_palidrome(s): # Recursion function
    pass

print(is_palidrome("racecar"))