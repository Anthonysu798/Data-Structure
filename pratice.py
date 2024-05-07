# # name = input("Enter your name: ")
# # age = int(input("Enter your age: "))

# # print(f"Hello {name} you are {age} years old");

# # if else statement that check if the user is an adult or a minor
# if (age >= 18):
#     print("You are an adult")
#     print("You can drink alcohol")
# else:
#     print("You are a minor")
#     print("You cannot drink alcohol")

x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

# Assignment multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"


print(x) # Orange
print(y) # Banana
print(z) # cherry


print(f"\nOne value to multiple variables",end = "\n\n")
x = y = z = "Orange"
print(f"x = {x}") # Orange
print(f"y = {y}") # Orange
print(f"z = {z}") # Orange

print(f"\nUnpack a collection",end = "\n\n")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(f"fruits = {fruits}")
print(f"x, y, z = fruits")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# Define a function that check user age
def check_user_age():
    global age # Make the variable global
    age = int(input("Enter your age: "))
    if (age >= 18):
        print("You are an adult")
        print("You can drink alcohol")
    else:
        print("You are a minor")
        print("You cannot drink alcohol")

# Define a function that ask the user first name, last name and age
def get_user_info():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    check_user_age()
    print(f"Hello {firstName}{lastName} welcome to this python course and you are {age} years old")

get_user_info()

# Multiple line string
multiline = """\n\nThis is a multiple line string
that can be written in multiple lines
and it will be printed in multiple lines"""

print(multiline)

ageOfUser = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

for age in ageOfUser:
    # print all the ages in the list

    ageOfUser.reverse()
    print(age, end=' ')

# Slicing
# What is slicing?
# Slicing is a way to extract a range of elements from a list
# Syntax: list[start:end:increment]

# print the first 5 elements from the list
print("\n",ageOfUser[:5])

# create a class Person

class Person:
    def __init__(self, name, age): # defaul constructor
        self.name = name
        self.age = age
    
    def __str__(self): # print the object
        return f"Name: {self.name} Age: {self.age}"
    
    def myfunc(self):
        print(f"Hello my name is {self.name}\n\n")

class Student: # Default constructor
    def __init__(self, studentId, studentEmail, studentFirstName, studentLastName):
        self.studentId = studentId
        self.studentEmail = studentEmail
        self.studentFirstName = studentFirstName
        self.studentLastName = studentLastName

    def __str__(self): # print the object just calling p1, p2, p3, p4 for example
        return f"""Student ID: {self.studentId}
Student Email: {self.studentEmail}
Student First Name: {self.studentFirstName}
Student Last Name: {self.studentLastName}\n"""
    


p1 = Person("John", 19)
p2 = Person("Steve", 20)
p3 = Person("Bill", 21)
p4 = Person("Mike", 22)

print(p1)
p1.myfunc()

print(p2)
p2.myfunc()

print(p3)
p3.myfunc()

print(p4)
p4.myfunc()

s1 = Student(142714229, "asu21@myseneca.ca", "Anthony", "Su")
s2 = Student(142714230, "Hohnhuang@myseneca.ca", "John", "Huang")
s3 = Student(142714231, "BillSmit@myseneca.ca ", "Bill", "Smith") 

print(s1)
print(s2)
print(s3)