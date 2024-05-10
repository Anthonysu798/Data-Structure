mylist = ["apple", "banana", "cherry"]

mylist.append("orange")

mylist.pop(1) # Remove element from the list (index)

# Create a list of 20 students
students = ["Steve", "John", "Bill", "Sam", "Tom", "Jerry", "Mike", "Alex", "Bob", "Sara", "Linda", "Mary", "Sue", "Liz", "Liza", "Mia", "Mina", "Tina", "Tanya", "Tara"]

# slice 
print(students[0:5]) # print the first 5 elements from the list

# Loop through the students list and print all the students in the list
for student in students:
    print(student)

if "John" in students:
    students.remove("John")
    print("John has been removed from the list")

if len(students) > 10:
    print("There are more than 10 students in the list")
else:
    print("There are less than 10 students in the list")

# Change from Steve to Anthony in the index 0
students[0] = "Anthony"

for student in students:
    print(f"\nStudent: {student}")
