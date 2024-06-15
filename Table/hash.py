# Hash Table Code

# Create an Node Class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def get_key(self):
        return self.key
    
    def set_value(self, value):
        self.value = value
    
    def set_key(self, key):
        self.key = key

# Creating the HashMap table
class HashMap:
    # Size of an array
    def __init__(self, size):
        self.size = size
        self.table = [None] * size # table is a list
    
    # Insert into the hash     # Key --> value
    def put(self, key, value): # 21 --> 115
        # Apply the hash function first = key % 10
        hash_value = key % self.size
        node = self.table[hash_value] # self.tabel index 1 then fetch it

        if node is None: 
            self.table[hash_value] = Node(key, value) # Take the key and value and insert it into the node from the table
        else:
            while node.next is not None: # Keep on going until the next node is not None
                if node.get_key() == key:
                    node.set_value(value)
                    return
                node = node.next # Keep on going to the next node
            
            # Only Modify the first node 
            if node.get_key() == key:
                node.set_value(value)
                return
            node.next = Node(key, value)

    def get(self, key):
        hash_value = key % self.size
        node = self.table[hash_value]
        
        while node is not None: # Keep on going until the next node is not None
            if node.get_key() == key: # If the key is found
                return node.get_value() # Return the value
            node = node.next
        
        return -1 # If the key is not found
    
    def display(self):
        for i in range(self.size):
            node = self.table[i]

            while node is not None:
                print("Key: {}, Value: {}".format(node.get_key(), node.get_value()))
                node = node.next

haashMap = HashMap(10)
haashMap.put(11, 25)
haashMap.put(2, 38)
haashMap.put(3, 25)
haashMap.put(4, 25)
haashMap.put(5, 25)
haashMap.put(1, 20)

haashMap.display()
print(haashMap.get(1))

# Theratical question 

# Explain what is a hash map 
# What is Linear?

# Two Part Question
# Five Step analysis

# Filling the code
# Giving some code and some line of code are remove 

# Fix the error in the code


# Third Question
# Giviven a scenario and ask to write a code for that scenario
# Insert a value into the middle of a linked list for example

# Recursion
# Write a code for recursion

# 5 Marks out of 50
# Ask you something and answer in plain english
# What is quick sort for example 

# 10 marks
# Second part
# 5 step analysis

# Second part
# Given some code, logic errors, compile errors. Fixing code

# Give some function
# Fill out some line of the function, rewrite the whole function

# 15 marks - Programming part
# Write python code for it
# One Recursion question # 7 marks

# Linked list 8 marks. Given a scenairo code it out in a linked list


H(i) = i % 10

When collision occur use this function
H(i,j) = (H) +(j+2) % 10 - set j+2 which prevent collision
j = probing

one collision is occur so j is 1
H(26, 1) = (6 + (1 + 2)) % 10 - |6 from the previous hash function|   -- second collision occur

H(26, 2) = (6 + (2 + 2)) % 10 - | go to index of 0 which is occupied 

H(26, 3) = (6 + (3 + 2)) % 10 

i = 8, 9, 10, 16, 26, 36

0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | - index 
10| 26|   |   |   |   |16 |   | 8 | 9 | - value

set the probing to 2 which is j + 2

36 % 10 = 6 since 6 already have an value so use the second hash function

H(36, 1) = (6 + (1 + 2)) % 10 - 9 sinch 9 also have a value go agaain
H(36, 2) = (6 + (2 + 2)) % 10 = 0 which 0 index have a value it go again
H(36, 3) = (6 + (3 + 2)) % 10 = 2 which empty so it insert into index of 2

0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | - index 
10| 26| 36|   |   |   |16 |   | 8 | 9 | - value

h(x) = i % 10
H(i,j) = i + j + 2 % 10 

