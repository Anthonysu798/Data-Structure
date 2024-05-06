# Array = Lists
# List of elements - it can be any data type

fruits = ["Apple", "Orange", "Banana", "Grapes", "Mango"]

fruits.remove("Banana") # Remove element from the list

fruits.pop(0) # Remove element from the list (index) 

fruits.append("Pine Apple") # Add element to the list at the end 

print (fruits[0].upper()) # type: ignore

fruits.sort() # Sort the list in ascending order
print (fruits)

fruits.reverse() # Reverse the list descending order
print (fruits)

nums = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]

# Print all the even numbers from the list
# 2, 4, 6, 8, 10
for i in range(0, len(nums)): 
    if (nums[i] % 2 == 0):
        print(nums[i])

# High level of doing it
for i in nums:
    if i % 2 == 0:
        print(i)

# Print the first 5 elements from the list
# Slicing
# print(nums[:5]) no need 0 | third parameter is the increment by the value you want to skip
print(nums[0:10:2]) # increment by 1 by default now it increments by 2

print(nums[::-1]) # Reverse the list

# Dictionary
students = {"name": ["Steve", "John", "Bill"], "age": [30, 21, 20]}

# If you just want the name to be printed you can do this
print (students["name"])

# Print the name elements from the dictionary
print (students["name"][0]) # Steve
print (students["name"][1]) # John
print (students["name"][2]) # Bill