# Create an node class
class Node:
    # Define the default constructor for the node class
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # Get value
    def get_value(self):
        return self.value
    
    # Get key
    def get_key(self):
        return self.key
    
    # Set Value
    def set_value(self, value):
        self.value = value
    
    # Set Key
    def set_key(self, key):
        self.key = key

# Creating the hashmap table
class HashMap:
    # Size for the hash table
    def __init__(self, size):
        self.size = size
        self.table = [None] * size # will create [None] * Size

    # Insert into the hash
    def put(self, key, value):
        hash_value = key % self.size

        node = self.table[hash_value]

        if node is None:
            # If node is none then create the first node in the table
            self.table[hash_value] = Node(key, value)
        
        else:
            while node.next is not None:
                if node.get_key() == key:
                    node.set_value(value)
                    return 
                node = node.next
        
            # Only Modify the first node
            if node.get_key() == key:
                node.set_value(value)
                return
            node.next = Node(key, value)

    def get(self, key):
        hash_value = key % self.size
        node = self.table[hash_value]

        while node is not None:
            if node.get_key() == key:
                return node.get_key()
            node = node.next

        # Return -1 if no key is found
        return -1
    
    def display(self):
        for i in range(self.size):
            node = self.table[i]

            while node is not None:
                print(f"Key: {node.get_key()}, Value: {node.get_value()}")
                node = node.next
    

        
haashMap = HashMap(10)
haashMap.put(11, 25)
haashMap.put(2, 38)
haashMap.put(3, 25)
haashMap.put(4, 25)
haashMap.put(5, 25)
        
haashMap.display()

print(haashMap.get(6))