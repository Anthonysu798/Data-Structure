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
